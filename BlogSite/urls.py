"""
URL configuration for BlogSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import blog_home, post_detail, create_post, signup, login_view, user_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_home, name='blog_home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('/logout', user_logout, name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



