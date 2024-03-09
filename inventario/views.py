from django.shortcuts import render
from inventario.models import Carro
import plotly.express as px
import pandas as pd 
def saludar(request):

    carros =Carro.objects.all()
    df=pd.DataFrame({
        "marca":["ferrari","volvo", "mercedes"],
        "cantidad":[20,12,14],
        "pais":["colombia", "Venezuela", "peru"]
    })
    grafico = px.bar(df, x="marca", y= "cantidad", color= "pais")
    mihtml=grafico.to_html(full_html=False)
    context = {
        "nombre": "juliana",
        "carros": carros,
        "grafica": mihtml
    }
    return render(request, "inventario/index.html", context)
