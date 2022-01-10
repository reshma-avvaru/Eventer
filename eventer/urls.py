from  . import views
from django.urls import path ,include
urlpatterns=[
    path('',views.all_events,name='all'),
    path('liked/',views.list_liked,name='liked'),
    path('like/',views.like_event,name='like'),
    path('add/',views.add_event, name="add")
]