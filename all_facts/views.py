from django.shortcuts import render
from add_fact.models import Fact

def display(request):
    facts = Fact.objects.all()
    context = {'facts':facts}
    return render(request, 'all_facts.html', context)

def delete(request, pk):
    fact = Fact.objects.get(id=pk)
    fact.delete()
    return display(request)