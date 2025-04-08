from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import CourseFeedback
from django.db.models import F, ExpressionWrapper, FloatField, Avg, Count, Sum
from django.db.models import Value
from functools import reduce
from operator import add
import traceback

# Create your views here.


@csrf_exempt
def login(request):
    if request.method == "POST":
        email = request.POST["email"].lower()
        password = request.POST["password"]
        print(email)
        print(password)
        exists = User.objects.filter(email = email).exists()
        print(exists)
        print(email)
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


@csrf_exempt  
def register(request):
    print("We Are in the Register poll")
    if request.method == "POST":
        email = request.POST["email"].lower()
        password = request.POST["password"]
        username = request.POST["username"].lower()
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


@csrf_exempt
def feedbackStat(request):
    rating_fields = [
        'quality',
        'material_structure_clarity',
        'workload_manageability',
        'instructor_quality',
        'instructor_clarity',
        'instructor_responsive',
        'instructor_engagement',
        'resources_availabilty',
        'assinment_impact',
    ]
    rating_sum = reduce(add, (F(field) for field in rating_fields))
    num_ratings = len(rating_fields)
    if request.method == "GET":
        feedback = CourseFeedback.objects.values('course_code').annotate(
            quality_avg=Avg('quality'),
            structure_avg=Avg('material_structure_clarity'),
            workload_avg=Avg('workload_manageability'),
            instructor_quality_avg=Avg('instructor_quality'),
            instructor_clarity_avg=Avg('instructor_clarity'),
            instructor_responsive_avg=Avg('instructor_responsive'),
            instructor_engagement_avg=Avg('instructor_engagement'),
            resources_availability_avg=Avg('resources_availabilty'),
            assignment_impact_avg=Avg('assinment_impact')
            )
        print(type(feedback))
        for item in feedback:
            print(f"Course Code: {item['course_code']}")
            for key, value in item.items():
                if key != 'course_code':  # Skip the course_code, as it's not part of the average ratings
                    print(f"{key}: {value}")
        return JsonResponse({'data':list(feedback), 'status':200}, safe=False)    


@csrf_exempt
def addFeedback(request):
    rating_fields = [
        'quality',
        'material_structure_clarity',
        'workload_manageability',
        'instructor_quality',
        'instructor_clarity',
        'instructor_responsive',
        'instructor_engagement',
        'resources_availabilty',
        'assinment_impact',
        'course_code',
        'instructor_name',
        'course_recommendation',
        'suggestion'
    ]
    if request.method == "POST":
        try:
            feedback = CourseFeedback()
            feedback.quality = request.POST[rating_fields[0]]
            feedback.material_structure_clarity = request.POST[rating_fields[1]]
            feedback.workload_manageability = request.POST[rating_fields[2]]
            feedback.instructor_quality = request.POST[rating_fields[3]]
            feedback.instructor_clarity = request.POST[rating_fields[4]]
            feedback.instructor_responsive = request.POST[rating_fields[5]]
            feedback.instructor_engangement = request.POST[rating_fields[6]]
            feedback.resources_availabilty = request.POST[rating_fields[7]]
            feedback.assinment_impact = request.POST[rating_fields[8]]
            feedback.course_code = request.POST[rating_fields[9]]
            feedback.instructor_name = request.POST[rating_fields[10]]
            feedback.course_recommendation = request.POST[rating_fields[11]]
            feedback.suggestion = request.POST[rating_fields[12]]
            feedback.save()
            return JsonResponse({'msg':'Feedback Suceesfull Saved', 'status':201},safe=False)
        except Exception as e:
            print("Error msg",e)
    
            print("cause ", e.__cause__)
            print("context ", e.__context__)
            print("Chai Another Error")
            traceback.print_exc()
            return JsonResponse({'msg':"Internal Error Pls Try Again Later", 'status':500}, safe=False)
    else:
        return JsonResponse({'msg' : "Method not Allowed", 'status': 405}, safe=False)    


