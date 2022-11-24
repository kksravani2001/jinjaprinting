from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    return render(request,'jinja_print.html',context={'name':'SRAVANI','age':21})
