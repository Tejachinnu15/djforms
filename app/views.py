from django.shortcuts import render

# Create your views here.
from app.forms import * 
from django.http  import HttpResponse
def djforms(request):
    SUFO=singnupform()
    d={'SUFO':SUFO}
    if request.method=='POST':
        SUFDT=singnupform(request.POST)
        if SUFDT.is_valid():
            name=SUFDT.cleaned_data['name']
        
    return render(request,'djforms.html',d)