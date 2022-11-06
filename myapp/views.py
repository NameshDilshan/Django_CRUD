from django.shortcuts import render, redirect
from myapp.models import Member


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    member = Member(firstName=request.POST['firstname'], lastName=request.POST['lastname'], )
    member.save()
    return redirect('/')


def read(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'result.html', context)


def edit(request, id):
    member = Member.objects.get(id=id)
    context = {'member': member}
    return render(request, 'edit.html', context)


def update(request, id):
    member = Member.objects.get(id=id)
    member.firstName = request.POST['firstname']
    member.lastName = request.POST['lastname']
    member.save()
    return redirect('/')


def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/')
