from django.contrib import admin
from django.urls import path

from .views import HomeView, LoginView, ProfileListView, RegisterView, LegalView, ContactView, logout_view, ProfileDetailView, ProfileUpdateView
from django.conf import settings
from django.conf.urls.static import static
from posts.views import PostCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("legal/", LegalView.as_view(), name="legal"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("profile/list/", ProfileListView.as_view(), name="profile_list"),
    path("profile/<pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/update/<pk>/", ProfileUpdateView.as_view(), name="profile_update"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
