from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.template import loader
# Create your views here.
def members(request):
    members= Member.objects.all().values()
    new=Member.objects.all()[3]
    context={'mymembers':members , 'new': new}
    template= loader.get_template("myfirst.html")
    return HttpResponse(template.render(context,request))
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
    'new': new
  }
  return HttpResponse(template.render(context, request))


def main(request):
    template= loader.get_template("main.html")
    return HttpResponse(template.render())