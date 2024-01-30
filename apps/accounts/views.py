from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView


class Login(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('HomeTemplate')
        
        return render(request, 'pages/accounts/login.html')
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('HomeTemplate')

        user = authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('HomeTemplate')

        messages.error(request, 'Email ou senha incorretos!')
        return redirect('login')


class Logout(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        return redirect('/')
