"""assessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from accounts import views
from tickets import views as ticketviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('new_ticket', ticketviews.new_ticket, name='new_ticket'),
    path('add_ticket', ticketviews.add_ticket, name='add_ticket'),
    path('ticket_added', ticketviews.ticket_added, name='ticket_added'),
    path('view_ticket', ticketviews.GetTickets.as_view(template_name='view_ticket.html'), name='view_ticket'),

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
