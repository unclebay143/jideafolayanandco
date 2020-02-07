from django.shortcuts import render

# Create your views here.

#maintainance function
def Maintain(request):
    return render(request, 'maintain.html')

#Home function
def Home(request):
    return render(request, 'index.html')

#About function
def About(request):
    return render(request, 'about.html')

#Ourwork function
def Ourwork(request):
    return render(request, 'ourwork.html')

#Testimony function
def Testimony(request):
    return render(request, 'testimony.html')

#Contact function
def Contact(request):
    return render(request, 'contact.html')

#Team function()
def Team(request):
    return render(request, 'team.html')


#Services function()
def Services(request):
    return render(request, 'services.html')
