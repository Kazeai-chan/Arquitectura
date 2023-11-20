from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('',home,name="home"),
    path('index.html',views.home,name='home'),
    path('jsonresponse/listaDoc', views.listaDoc, name='listaDoc'),
    path('jsonresponse/listaRes/<id_doc>/<fechaR>', views.listaRes, name='listaRes'),
]