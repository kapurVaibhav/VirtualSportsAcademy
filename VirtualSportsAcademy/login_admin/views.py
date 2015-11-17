from django.shortcuts import render
from django.template.context_processors import csrf
from django.shortcuts import render ,render_to_response
from django.http import HttpResponse

# Create your views here.
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login_admin/PlayersRegistration.html",c)