from django.urls import path 
from . import views

urlpatterns = [
    path("" , views.Home , name="Home"),
    path("book_apt/book_id=<int:id>" , views.Book_apt , name="Book_apt"),
    path("client_side" , views.Client_side , name="Client_side"),
    path('accept_appointment/<int:id>/', views.accept_appointment, name='accept_appointment'),
    path('reject_appointment/<int:id>/', views.reject_appointment, name='reject_appointment'),
    path("all_appointement/" , views.all_appointement , name="all_appointement"),
    path("about/" , views.about , name="about")
]
