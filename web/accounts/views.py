from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Talk
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse


def unsecure(request):   
    return render(request,"unsecure.html",{})  

@login_required
def secure(request):   
    return render(request,"secure.html",{}) 

def index(request):
    template = loader.get_template('test/index_test.html')
    return HttpResponse(template.render())

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "regist.html"

def error(request,error_type=404):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
def board(request):
    template = loader.get_template('master.html')
    return HttpResponse(template.render())

##def main(request):
    ##template = loader.get_template('hello.html')
    ##return HttpResponse(template.render())

## @login_required
def hello(request):   
    return render(request,"hello.html",{}) 

## @login_required
def main(request):   
    return render(request,"main.html",{}) 

def talks(request):
  talks = Talk.objects.all().order_by('-posted_date').values()
  template = loader.get_template('all_talks.html')
  context = {
    'talks': talks, 
  }
  return HttpResponse(template.render(context, request))

def talk(request, id):
  talk = Talk.objects.get(id=id)
  template = loader.get_template('talk.html')
  context = {
    'talk': talk, 
  }
  return HttpResponse(template.render(context, request))

# views.py
from django.shortcuts import render
from .forms import TalkForm
from .models import Talk
from django.views.generic import CreateView


class TalkCreateView(CreateView):
  model = Talk
  form_class = TalkForm
  template_name = 'talk_create.html'
  success_url = '/talks/'

from .forms import UploadModelForm


from .models import Photo

def photo(request):
    photos = Photo.objects.all()  #查詢所有資料
    form = UploadModelForm()
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'photos': photos,
        'form': form
    }
    return render(request, 'photo.html', context)
