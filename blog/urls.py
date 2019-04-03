from django.urls import path,re_path
from blog import views

app_name = 'Blog'
urlpatterns = [
    path('', views.Index_List.as_view(), name='index_List'),
    path(r'detail/<int:article_id>/', views.detail, name='detail'),
    path(r'category/<int:cate_id>/', views.category, name='cate'),
    path(r'search/', views.Search.as_view(), name='search')
]