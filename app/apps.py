from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'


def final():
    print("Django setup completed")
    name = "hello".upper()
    print(name)
    

final()