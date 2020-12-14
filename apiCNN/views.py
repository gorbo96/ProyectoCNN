#CONTROLADOR

from rest_framework import generics #para microservicio
from apiCNN import models
from apiCNN import serializers

from django.shortcuts import render
from apiCNN.Logica import modeloCNN #para utilizar modelo SNN


class Clasificacion():
    #imagen = models.ImageField(upload_to='imagenes')
    #prediccion = models.CharField(max_length=200, blank=True)

    def determinarSobrevivencia(request):

        return render(request, "seleccion.html")

    def predecir(request):        
        resul=modeloCNN.modeloCNN.predecir(modeloCNN.modeloCNN,request.POST.get("Imagen"))
        return render(request, "prediccion.html",{"e":resul})