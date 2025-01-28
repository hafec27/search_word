from django.urls import path
from django.urls import path, include  # includeもインポートします
from . import views
from django.contrib import admin


urlpatterns = [path('admin/', admin.site.urls),
    path('', views.search_page, name='search_page'),  # トップページをsearch_pageビューに設定
    path('create/', views.create_post, name='create_post'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # 引数を渡すURLパターン
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
