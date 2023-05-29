from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import User

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Simpan data pengguna ke dalam model User (tb_user)
            id_user = user.id
            nama_user = user.first_name + ' ' + user.last_name
            custom_user = User(id_user=id_user, nama_user=nama_user, username=user.username, password=user.password)
            custom_user.save()

            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

