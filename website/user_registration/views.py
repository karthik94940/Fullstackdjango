from django.shortcuts import render, HttpResponse, redirect
from user_registration.models import User

from user_registration.forms import UserForm

# Create your views here.


def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'user_registration/home.html', param)
    else:
        return render(request, 'user_registration/home.html')


def sign_up(request):
    # if request.method == 'POST':
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     user_name = request.POST.get('user_name')
    #     user_mail = request.POST.get('user_mail')
    #     mobile_number = request.POST.get('mobile_number')
    #     password = request.POST.get('password')
    #     re_password = request.POST.get('re_password')
    #     if User.objects.filter(user_name=user_name).count() > 0:
    #         return HttpResponse('Username already exists')
    #     else:
    #         user = User(first_name= first_name, last_name=last_name, user_name=user_name, user_mail=user_mail,
    #                     password=password, re_password=re_password, mobile_number=mobile_number).save()
    #         return redirect(login)
    #
    # else:
    #     return render(request, 'user_registration/sign_up.html')
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully Registered!!!")

    context = {
        'form': form,
    }
    return render(request, 'user_registration/sign_up.html', context)

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'user_registration/login.html')

