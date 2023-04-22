# EntregaFinalBlog
Entrega Final Blog Coder House
Participante: Facundo Martin Carrizo

Funciones Activas Actualizadas:
  Registro
  LogIn
  LogOut
  Change Password
  Create Post
  Edit Post
  Delete Post
 
 
Para correr correctamente el TP:
 Python 3.9.13
 django 4.1.7
 python -m venv EntrgaFinal
 Install django packages en el IDE
 python manage.py runserver

 Importante para poder utilizar de manera mas fuida el Pasword change, cambiar en la pagina de views.py de venv/Lib/site-packages/django/contrib/auth/views.py
 Poner en la clase PasswordChangeView la siguiente linea: template_name = "PostViews/home.html"
