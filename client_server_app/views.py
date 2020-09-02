from django.shortcuts import render
from client_server_app.models import User, Service_provider
# Create your views here.
def index(request):
    return render(request,'client_server_app/index.html')

def Users(request):
    user_list = User.objects.order_by('service_provider_Type')
    user_dict = {'user' : user_list}
    return render(request,'client_server_app', context = user_dict)