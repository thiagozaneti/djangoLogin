from django.shortcuts import render, HttpResponse

def Cadastro_page(request):
    if request.method == "POST":
        return render(request, 'cadhome.html')
    else:
        username = request.POST.get('name')
        senha = request.POST.get('password')
        email = request.POST.get('email')
        return HttpResponse(username)
        return render(request, 'cadhome.html', context= {'username':username})

def Login_page(request):
     return render(request, 'loginpage.html')