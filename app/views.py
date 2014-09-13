from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from app.models import User, Edit_Form

def index(request):
    user_list = User.objects.order_by('-id')
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {
        'user_list': user_list,
    })
    return HttpResponse(template.render(context))

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    first = user.first
    last = user.last
    email = user.email
    template = loader.get_template('app/edit.html')
    context = RequestContext(request, {
        'user': user,
        'first': first,
        'last': last,
        'email': email,
    })
    return HttpResponse(template.render(context))

def add(request):
    template = loader.get_template('app/add.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def update(request, user_id):
    user = User.objects.get(id=user_id)
    form = Edit_Form(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/app/')


def create(request):
    form = Edit_Form(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/app/')
    else:
        return

def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect('/app/')

