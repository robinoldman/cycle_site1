from django import pathfrom . import views

urlpatterns = [
    path ('',views.home,name='home'),
]