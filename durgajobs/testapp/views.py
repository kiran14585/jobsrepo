from django.shortcuts import render
from testapp.models import Hydjobs,Bangalorejobs,Punejobs

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')


def hydjobs_view(request):
    jobs_list = Hydjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def bangalorejobs_view(request):
    jobs_list = Hydjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)


def punejobs_view(request):
    jobs_list = Hydjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)
