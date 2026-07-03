from django.shortcuts import render
from add_fact.models import Fact
import random

def generate(request):
    records = list(Fact.objects.values_list('id',flat = True))
    key = random.randrange(0, len(records))
    generatedFact = Fact.objects.get(id=records[key])
    context = { 'id': generatedFact.id,
                'fact' : generatedFact.fact,
               'likedState': generatedFact.liked}
    return render(request, 'generate_fact.html', context)

def add_fact(request):
    return render(request, 'add_fact.html')

def likeButton (request,pk):
    fact = Fact.objects.get(id=pk)
    if fact.liked:
        fact.liked = False
        fact.save()
    else:
        fact.liked = True
        fact.save()
    context = {'id': pk,
               'fact': fact.fact,
               'likedState': fact.liked}
    return render (request, 'generate_fact.html', context)