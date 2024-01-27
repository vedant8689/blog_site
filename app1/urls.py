from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static

app_name='user'
urlpatterns = [
    path('admin/', admin.site.urls),
    #specifiying which route will go to blog site when loaded (url site of blog)
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    # class based view to login and logout for user (if not then only admin can log in)
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', users_views.custom_logout, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete>', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
        name='password_reset_complete'),
    path('', include('blog.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
