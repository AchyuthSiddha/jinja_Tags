from django.shortcuts import render

# Create your views here.
def CskTeam(request):
    d={'name':'Achyuth','age':24}
    return render(request,'CskTeam.html',context=d)