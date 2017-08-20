from django.shortcuts import render

def people_list(request):
    return render(request, 'spiral/people_list.html', {})
