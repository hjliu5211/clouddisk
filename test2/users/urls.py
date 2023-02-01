from django.urls import path
import users.views
urlpatterns = [
    path('hello_world',users.views.HelloworldView)
]