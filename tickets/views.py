from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
def new_ticket(request):
    return render(request, 'tickets/ticket.html')

@login_required
def add_ticket(request):
    print(request.user.email)
    print (request.POST)
    return HttpResponse('ticket added')