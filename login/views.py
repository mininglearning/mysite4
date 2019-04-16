from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
from login import models

user_list = []
def index(request):
    # return  HttpResponse('Hello World!')
    # return render(request, "index.html")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        models.UserInfo.objects.create(user = username,pwd=password)
    user_list = models.UserInfo.objects.all()
        # print(username,password)
        # temp = {'user':username,'pwd':password}
        # user_list.append(temp)
    return render(request,'index.html',{'data':user_list})
    #return render(request,'index.html')
