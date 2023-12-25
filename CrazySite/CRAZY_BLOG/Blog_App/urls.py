# from django.contrib import admin
# from django.urls import path

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import AddPostCreateView, ArticleDetailView, Dashboard, imagesView, success, display_images,trendingListView
from . import views

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('', views.HomePage, name='home'),
    path('', views.SignupPage, name='signup'),
    path('login/ ', views.LoginPage, name='login'),
    path('signup/', views.SignupPage, name='signup'),

    path('logout/ ', views.LogoutPage, name='logout'),
    path('Dashboard/ ', Dashboard.as_view(), name='Dashboard'),
    path('trending/ ', trendingListView.as_view(template_name='trending')),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/ ', AddPostCreateView.as_view(), name='add_post'),
    path('context/', views.context, name='context'),

    path('images/', views.imagesView, name='image_upload'),
    path('success', views.success, name='success'),
    path('display_images/', views.display_images, name='display_images'),
    # path('logout/ ', LogOut.as_view(), name='log_out'),
]
