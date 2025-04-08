from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name="login"),
    path('feed',views.feedbackStat,name="feedbackStat"),
    path('addFeed',views.addFeedback,name='addFeedback'),
    path('register',views.register,name="register")
]