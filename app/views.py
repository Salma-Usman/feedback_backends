from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

# Create your views here.


@csrf_exempt
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        print(password)
        exists = User.objects.filter(email = email).exists()
        if(exists):
            currentUser = User.objects.get(email = email)
            if(currentUser.password == password): 
                return JsonResponse({'msg':"User Authenticate Sucessfully", 'status':200}, safe=False)
            else:
                return JsonResponse({'msg':"Password Is not Correct", 'status':401}, safe=False)
        else:
            return JsonResponse({'msg' : "User Not Found", 'status': 404}, safe=False)
    else:
        return JsonResponse({'msg' : "Method not Allowed", 'status': 405}, safe=False)


   
def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        username = request.POST["username"]
        exists = User.objects.filter(email = email).exists()
        if exists:
            return JsonResponse({'msg':'User Already Exist', 'status':409})
        elif User.objects.filter(username = username).exists():
            return JsonResponse({'msg':'Username As been taken', 'status':409})
        else:
            user = User(email = email, password = password, username = username)
            user.save()
            return JsonResponse({'msg':'User Created Sucessfully', 'status':201})
    else:
        return JsonResponse({'msg' : "Method not Allowed", 'status': 405}, safe=False)


