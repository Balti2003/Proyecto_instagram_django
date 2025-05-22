from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Usuario")
    image = models.ImageField(upload_to="posts_images/", verbose_name="Imagen")
    caption = models.TextField(max_length=500, blank=True, verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    likes = models.ManyToManyField(User, related_name="liked_post", verbose_name="N° de Likes")
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
    
    def like(self, user):
        self.likes.add(user)
    
    def unlike(self, user):
        self.likes.remove(user)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post al que pertence el comentario", on_delete=models.CASCADE, 
                            related_name="comments")
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(verbose_name="Contenido del comentario", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion del comentario")
    
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"Comento {self.user.username} el post {self.post}"    