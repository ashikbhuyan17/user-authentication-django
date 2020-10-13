from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.forms import TeacherRegistration, StudentRegistration, StudentLoginForm, TeacherLoginForm
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_PROFILE_MODULE


def index(request):
    return render(request, 'index.html')


def teacher_reg_view(request):
    context = {}
    if request.POST:
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect('teacher_reg')
        else:
            context['teacher_reg_form'] = form

    else:
        form = TeacherRegistration()
        context['teacher_reg_form'] = form
    return render(request, 'teacher_reg.html', context)


def student_reg_view(request):
    context = {}
    if request.POST:
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect('student_reg')
        else:
            context['student_reg_form'] = form

    else:
        form = StudentRegistration()
        context['student_reg_form'] = form
    return render(request, 'student_reg.html', context)


def student_login_view(request):
    context = {}
    if request.POST:
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')
                next_url = request.GET.get('next', 'student_dashboard')
                return redirect(next_url)
            else:
                messages.error(request, 'Wrong Credentials!!')
    else:
        form = StudentLoginForm()

    context['student_login_form'] = form
    return render(request, 'student_login.html', context)


def teacher_login_view(request):
    context = {}
    if request.POST:
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect("dashboard")
            else:
                messages.error(request, 'Wrong Credentials!!')
    else:
        form = TeacherLoginForm()

    context['teacher_login'] = form
    return render(request, 'teacher_login.html', context)


def dashboard(request):
    return render(request,'dashboard.html')