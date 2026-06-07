from django.urls import path
from artikel.api import (
    api_artikel_blog_list,
    api_artikel_blog_tambah,
    api_artikel_blog_update,  
    api_artikel_blog_delete  
)

urlpatterns = [
    # GET & POST
    path('artikel/list/', api_artikel_blog_list, name='api_artikel_blog_list'),
    path('artikel/tambah/', api_artikel_blog_tambah, name='api_artikel_blog_tambah'),
    
    # PUT & DELETE (Membutuhkan parameter ID artikel)
    path('artikel/update/<int:id_artikel>/', api_artikel_blog_update, name='api_artikel_blog_update'),
    path('artikel/delete/<int:id_artikel>/', api_artikel_blog_delete, name='api_artikel_blog_delete'),
]