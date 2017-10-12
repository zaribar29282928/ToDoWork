# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import ToDoWork
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

def list(request):
    todowork=ToDoWork.objects.all()

    context={
        'todowork':todowork,

            }
    print context
    return render_to_response('list.html', context)



def create_work(request):
    return render_to_response('create_work.html')



#regester the work
@csrf_exempt
def register_work(request):
    #TODO if user send no thing but submit
    if request.POST.get('title'):
        title=request.POST.get('title')
    else:
        title="no thing"

    if request.POST.get('content'):
        content=request.POST.get('content')
    else:
        content="no thing"


    if content=="no thing" and title=="no thing":
        print "no thing"
    else:
        new_work=ToDoWork(title=title,content=content)
        new_work.save()

    return redirect('/')



def delete(request,work_id):
    if work_id:
        try:
            if ToDoWork.objects.get(id=work_id):
                work=ToDoWork.objects.get(id=work_id)
                work.delete()
        except:
            print "no thing "

    return redirect('/')


#register done or none done
def done(request,work_id):
    if work_id:
        try:
            if ToDoWork.objects.get(id=work_id):
                work=ToDoWork.objects.get(id=work_id)
                if work.done:
                    work.done=False
                    work.save()
                else:
                    work.done=True
                    work.save()

        except:
            print "no thing "

    return redirect('/')

def create_work(request):
    return render_to_response('create_work.html')
