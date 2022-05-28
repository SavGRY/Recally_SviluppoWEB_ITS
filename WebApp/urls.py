from . import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index, name = "home_page"),
    path('privacy/', views.privacy, name = 'privacy'),
    # URL SARA' ..../playlist/--> prendi gli url da playlist.urls
    path('playlist/', include("playlist.urls")),
    path('user_create/', views.UserCreateView.as_view(), name='user_create'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("contact/", include("contact.urls"))
]
