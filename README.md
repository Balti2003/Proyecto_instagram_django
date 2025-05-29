# Instagram Clone - Proyecto Django

![Django](https://img.shields.io/badge/Django-v4.2-green) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Descripción

Este proyecto es una aplicación web tipo **Instagram**, desarrollada con Django. Permite a los usuarios crear perfiles, seguir a otros usuarios, realizar publicaciones, interactuar con me gustas y comentarios en distintas publicaciones y enviar mensajes de contacto.

---

## Funcionalidades

- Registro y autenticación de usuarios.
- Perfiles de usuario con foto, biografía y fecha de nacimiento.
- Sistema de seguidores con modelo personalizado.
- Visualización de lista de perfiles con contador de seguidores.
- Formulario de contacto.
- Sistema de me gustas y comentarios en una publicacion.
- Interfaz limpia y responsiva usando Bootstrap 5.

---

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tuusuario/instagram-clone.git
    cd instagram-clone
    ```

2. Crear y activar entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows
    ```

3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configurar variables de entorno (opcional).

5. Aplicar migraciones:
    ```bash
    python manage.py migrate
    ```

6. Ejecutar el servidor:
    ```bash
    python manage.py runserver
    ```

7. Abrir en el navegador: [http://localhost:8000](http://localhost:8000)

---

## Uso

- Regístrate o inicia sesión para crear tu perfil.
- Sube tu foto, agrega biografía y fecha de nacimiento.
- Explora otros perfiles y sigue a quienes te interesen.
- Interacciona con las publicaciones de otros perfiles.
- Usa el formulario de contacto para enviarnos mensajes o dudas.

---

## Tecnologías

- Python 3.10
- Django 4.x
- Bootstrap 5
- SQLite (por defecto, fácil de cambiar a otra base de datos)

---

## Autor

**Lomello Baltasar** – [baltasarlomello@live.com](mailto:baltasarlomello@live.com)

Sígueme en [GitHub](https://github.com/Balti2003)

---

¡Gracias por visitar el proyecto! 🚀