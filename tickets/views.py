from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .services import get_tickets, post_ticket
import json
# Create your views here.

# @login_required
def new_ticket(request):
    return render(request, 'tickets/ticket.html')

@login_required
def add_ticket(request):

    # print(request.user.email)
    # print (request.POST)

    # data = request.POST

    data = {
            'Department':request.POST.get('Department'),
            'Category':request.POST.get('Category'),
            'Subject':request.POST.get('Subject'),
            'Priority':request.POST.get('Priority'),
            'Name':request.POST.get('Name'),
            'Email':request.POST.get('Email'),
            'Phone':request.POST.get('Phone'),
            'description':request.POST.get('description')
        }

    res_code = post_ticket(data=json.dumps(data))
    
    # print(res_code)

    return HttpResponse(render(request, 'tickets/ticket_added.html', {"msg":"ticket added"}))

# @login_required
def ticket_added(request):
    return render(request, 'tickets/view_ticket.html')

class GetTickets(TemplateView):
    template_name = 'view_ticket.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'tickets' : get_tickets(email = 'niket@codewave.com'),
        }
        return context



