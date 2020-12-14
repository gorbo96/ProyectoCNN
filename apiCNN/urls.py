# existing imports
from django.urls import path
from django.conf.urls import url
from apiCNN import views


urlpatterns = [
    url(r'^sobrevivencia/$',views.Clasificacion.determinarSobrevivencia),
    url(r'^predecir/',views.Clasificacion.predecir),    
]