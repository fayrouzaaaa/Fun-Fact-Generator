from django.shortcuts import render, redirect
from add_fact.models import Fact

def addButton(request):
    if request.method == "POST":
        fact = request.POST.get('fact')

        Fact.objects.create(fact=fact)

        return redirect('/')
    return render(request, 'add_fact.html')

def generate_fact(request):
    return render(request,'home.html')