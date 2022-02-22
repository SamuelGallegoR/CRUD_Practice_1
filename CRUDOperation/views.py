from django.shortcuts import render
from CRUDOperation.models import EmpModel

def showemp(request):
    showall=EmpModel.objects.all()
    return render(request, 'index.html',{'data':showall})

 