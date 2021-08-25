
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('detail/<int:id>',views.detail,name='detail'),
    


]
