from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
    path('age_conf/', views.age_conf, name='age_conf'),
    #path('', views.post_list, name='post_list'),
    path('', views.post_tab, name='post_tab'),
    path('<int:blog_id>/', views.post_detail, name='post_detail'),
]

