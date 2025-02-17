from django.shortcuts import render



def Home(request):
    return render(request, "Home.html")
def About(request):
    return render(request, "About.html")
def Service(request):
    return render(request, "Service.html")
def ServiceDetails(request):
    return render(request, "ServiceDetails.html")
def Signup(request):
    return render(request, "Signup.html")
def Forgot(request):
    return render(request, "ForgotForm.html")
def Core(request):
    return render(request, "CoreTeam.html")
def Contact(request):
    return render(request, "Contact.html")