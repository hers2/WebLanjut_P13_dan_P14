from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from artikel.models import Kategori, ArtikelBlog
from artikel.forms import KategoriForms, ArtikelForms


# Create your views here.
def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user == 0:
        return False
    else:
        return True
    

######################## user biasa #########################   
@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    context = {
        "kategori":kategori,
        "artikel":artikel,
    }
    return render(request, template_name, context)


@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"

    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES) # Ditambahkan request.FILES untuk menangani upload file

        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "berhasil menambahkan artikel baru") # <--- TAMBAHAN NOTIFIKASI

            return redirect("admin_artikel_list") # <--- DIPERBAIKI MENGGUNAKAN STRING

    forms = ArtikelForms()

    context = {
        "forms": forms
    }

    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"

    artikel = ArtikelBlog.objects.get(id=id_artikel)

    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)

        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "berhasil melakukan update artikel") # <--- TAMBAHAN NOTIFIKASI

            return redirect("admin_artikel_list") # <--- DIPERBAIKI MENGGUNAKAN STRING

    forms = ArtikelForms(instance=artikel)

    context = {
        "forms": forms
    }

    return render(request, template_name, context)


@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):

    try:
        ArtikelBlog.objects.get(id=id_artikel).delete()
        messages.success(request, "berhasil menghapus artikel") # <--- TAMBAHAN NOTIFIKASI

    except:
        pass

    return redirect("admin_artikel_list") # <--- DIPERBAIKI MENGGUNAKAN STRING


########################## admin ##########################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/auth-login')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori": kategori
    }
    return render(request, template_name, context)


@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/auth-login')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "berhasil menambahkan kategori baru") # <--- TAMBAHAN NOTIFIKASI
            return redirect("admin_kategori_list") # <--- DIPERBAIKI MENGGUNAKAN STRING
            
    forms = KategoriForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/auth-login')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori)

    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "berhasil melakukan update kategori") # <--- TAMBAHAN NOTIFIKASI
            return redirect("admin_kategori_list") # <--- DIPERBAIKI MENGGUNAKAN STRING

    forms = KategoriForms(instance=kategori)
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/auth-login')
def admin_kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
        messages.success(request, "berhasil menghapus kategori") # <--- TAMBAHAN NOTIFIKASI
    except:
        pass

    return redirect("admin_kategori_list") # <--- DIPERBAIKI MENGGUNAKAN STRING

######################## artikel blog ########################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/auth-login')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = ArtikelBlog.objects.all()
    context = {
        "artikel": artikel
    }

    return render(request, template_name, context)


@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/auth-login')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"

    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES) # Ditambahkan request.FILES untuk menangani upload file

        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "berhasil menambahkan artikel baru") # <--- TAMBAHAN NOTIFIKASI

            return redirect("admin_artikel_list") # <--- DIPERBAIKI MENGGUNAKAN STRING

    forms = ArtikelForms()

    context = {
        "forms": forms
    }

    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/auth-login')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"

    artikel = ArtikelBlog.objects.get(id=id_artikel)

    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)

        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, "berhasil melakukan update artikel") # <--- TAMBAHAN NOTIFIKASI

            return redirect("admin_artikel_list") # <--- DIPERBAIKI MENGGUNAKAN STRING

    forms = ArtikelForms(instance=artikel)

    context = {
        "forms": forms
    }

    return render(request, template_name, context)


@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/auth-login')
def admin_artikel_delete(request, id_artikel):

    try:
        ArtikelBlog.objects.get(id=id_artikel).delete()
        messages.success(request, "berhasil menghapus artikel") # <--- TAMBAHAN NOTIFIKASI

    except:
        pass

    return redirect("admin_artikel_list") # <--- DIPERBAIKI MENGGUNAKAN STRING

########################## management User oleh operator ##########################
@login_required(login_url='login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"
    daftar_user = User.objects.all()
    context = {
        "daftar_user":daftar_user
    }
    return render(request, template_name, context)





@login_required(login_url='login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_edit(request, user_id):
    template_name = 'dashboard/admin/user_edit.html'
    user = get_object_or_404(User, pk=user_id) # Ambil objek user berdasarkan ID, atau 404 jika tidak ditemukan
    group_user = []
    for group in user.groups.all():
        group_user.append(group.name)

    all_groups = Group.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        is_staff = request.POST.get("is_staff")
        groups_checked = request.POST.getlist('groups')

        if is_staff == None:
            is_staff = False
        else:
            is_staff = True
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.groups.set(Group.objects.filter(id__in=groups_checked))
        user.save()

        messages.success(request, f"berhasil update user {user.username}")
        return redirect(admin_management_user_list) # Redirect ke halaman daftar user setelah berhasil

    context = {
        'user': user,
        'all_groups': all_groups,
        'group_user': group_user
    }
    return render(request, template_name, context)