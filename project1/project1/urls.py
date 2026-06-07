from django.contrib import admin
from django.urls import path, include
########################### Untuk Media ###########################
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Mengimpor views utama proyek (HAPUS 'artikel_list' dari sini)
from project1.views import index, detail_artikel, kontak, galeri, dashboard
from project1.authentication import login, logout, registrasi

# Mengimpor views langsung dari aplikasi artikel (Tambahkan fungsi user biasa di sini)
from artikel.views import (
    artikel_list,      # <--- SEKARANG DIIMPOR DARI SINI DENGAN BENAR
    artikel_tambah,
    artikel_update,
    artikel_delete,

    admin_kategori_list,
    admin_kategori_tambah,
    admin_kategori_update,
    admin_kategori_delete,
    
    admin_artikel_list,
    admin_artikel_tambah,
    admin_artikel_update,
    admin_artikel_delete,

    admin_management_user_list,
    admin_management_user_edit
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    path('', index),
    path('artikel/<int:id>/', detail_artikel, name='detail_artikel'),
    path('kontak/', kontak, name='kontak'),
    path('galeri/', galeri, name='galeri'),

    # ==================== RUTE API UTAMA ====================
    # Ini akan memanggil file artikel/urls_api.py
    path('api/', include("artikel.urls_api")),

    # ==================== SISTEM DASHBOARD (DIRECT PATH) ====================
    path('dashboard/', dashboard, name='dashboard'),
    
    # Rute Artikel untuk User Biasa (Sekarang mengarah ke fungsi artikel.views yang benar)
    path('dashboard/artikel_list/', artikel_list, name='artikel_list'),
    path('dashboard/artikel/tambah/', artikel_tambah, name='artikel_tambah'),
    path('dashboard/artikel/update/<int:id_artikel>/', artikel_update, name='artikel_update'),
    path('dashboard/artikel/delete/<int:id_artikel>/', artikel_delete, name='artikel_delete'),
    
    # Rute Kategori (Menggunakan struktur dashboard/operator/)
    path('dashboard/operator/kategori/list/', admin_kategori_list, name='admin_kategori_list'),
    path('dashboard/operator/kategori/tambah/', admin_kategori_tambah, name='admin_kategori_tambah'),
    path('dashboard/operator/kategori/update/<int:id_kategori>/', admin_kategori_update, name='admin_kategori_update'),
    path('dashboard/operator/kategori/delete/<int:id_kategori>/', admin_kategori_delete, name='admin_kategori_delete'),

    # Rute Artikel Admin (Menggunakan struktur dashboard/operator/)
    path('dashboard/operator/artikel/list/', admin_artikel_list, name='admin_artikel_list'),
    path('dashboard/operator/artikel/tambah/', admin_artikel_tambah, name='admin_artikel_tambah'),
    path('dashboard/operator/artikel/update/<int:id_artikel>/', admin_artikel_update, name='admin_artikel_update'),
    path('dashboard/operator/artikel/delete/<int:id_artikel>/', admin_artikel_delete, name='admin_artikel_delete'),
    # ========================================================================

    # Rute Management User (Operator)
    path('dashboard/operator/management-user/list/', admin_management_user_list, name='admin_management_user_list'),
    path('dashboard/operator/management-user/edit/<int:user_id>/', admin_management_user_edit, name='admin_management_user_edit'),

########################### Authentication ###########################
    path('auth-login', login, name='login'),
    path('auth-registrasi', registrasi, name='registrasi'),
    path('auth-logout/', logout, name='logout'),
    
########################### CKEditor 5 Upload Path ###########################
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

########################### Untuk Media & Static ###########################
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)