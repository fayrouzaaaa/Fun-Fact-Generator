from django.shortcuts import render
from add_fact.models import Fact

def likedFacts(request):
    facts = Fact.objects.all()
    likedfacts = []
    for fact in facts:
        if fact.liked:
            likedfacts.append(fact)
    return render(request, 'liked_facts.html', {'facts':likedfacts})

def unlike(request, pk):
    fact = Fact.objects.get(id=pk)
    fact.liked = False
    fact.save()
    return likedFacts(request)