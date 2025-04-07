from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

class CourseFeedback(models.Model):
    course_code = models.CharField(max_length=50)
    instructor_name = models.CharField(max_length=50)
    quality = models.IntegerField(default=0) 
    material_structure_clarity = models.IntegerField(default=1)
    workload_manageability =  models.IntegerField(default=1)
    instructor_quality = models.IntegerField(default=1)
    instructor_clarity = models.IntergerField(default = 1)
    instructor_responsive = models.IntegerField(default = 1)
    instructor_engangement = models.IntegerField(default=1)
    resources_availabilty = models.IntegerField(default=1)
    assinment_impact = models.IntegerField(default=1)
    course_recommendation = models.BooleanField(default=False)
    suggestion = models.CharField(max_length=100)

