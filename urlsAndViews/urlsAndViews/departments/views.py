from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse("<h1>This is the departments app.</h1>")


def show_departments_by_name(request):
    departments = Department.objects.all()
    context = {
        'departments': departments
    }

    return render(request, 'departments/show_departments_by_name.html', context)


def show_departments_by_id(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return redirect('index')

    context = {
        'department': department
    }

    return render(request, 'departments/show_department_by_id.html', context)
