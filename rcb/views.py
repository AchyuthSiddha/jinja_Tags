from django.shortcuts import render

# Create your views here.
def RcbTeam(request):
    d={'name':'ABD','age':'35','identity':'Mr 360'}
    return render(request,'RcbTeam.html',context=d)