from django.contrib import admin
from django.urls import path
from pima import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('model/', views.Callmodel.as_view()), # "we use as as_view function because in Class-based views, we have to call as_view() function so as to return a callable view that takes a request and returns a response."
    path('patient/', views.Requestdb.as_view())
]
