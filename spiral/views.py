from django.shortcuts import render
from django.utils import timezone
from .models import Person, Address

def persons_list(request):
    persons = Person.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'spiral/persons_list.html', {'persons': persons})
