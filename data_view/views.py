from django.shortcuts import render

# Create your views here.
from django.db import connection
from django.shortcuts import render
import pandas as pd
import json
from data_view.models import immo_bien
from .models import Contact
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Sum, Max, Min, Avg, StdDev
from django.db.models.aggregates import StdDev
from django.views.generic import ListView


def immo_list (request):
    posts = str(immo_bien.objects.exclude(balcony=True).query)
    df = pd.read_sql_query(posts, connection)
    df['prix_m2_ttc'] = df.prix_m2_ttc.replace(',','.', regex=True).values
    df['prix_m2_ttc'] = pd.to_numeric(df['prix_m2_ttc'], downcast = "float")
    total_rows = len(df.id)
    bien_immo = total_rows + 1
    
    json_records = df.reset_index(). to_json(orient = 'records')
    data = []
    data = json.loads(json_records)

    sd = df.groupby('ville')['prix_m2_ttc'].mean()
    mean_records = sd.reset_index().to_json(orient ='records')
    mean = []
    mean = json.loads(mean_records)

    st = df.groupby('ville')['prix_m2_ttc'].std()
    std_records = st.reset_index().to_json(orient ='records')
    std = []
    std = json.loads(std_records)

    d= df.describe()
    smy_records = d.reset_index().to_json(orient ='records')
    describe = []
    describe = json.loads(smy_records)
    

   
    print(posts)
    print(connection.queries)
    if request.method=="POST":
        contact= Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1> THANKS FOR CONTACTING US</h1>")
    if request.method=="POST":
        fromdate= request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=immo_bien.objects.raw('select * from immo_bien where joindate between "'+fromdate+'" and "'+todate+'"')
        return render(request, 'index.html', {"data":searchresult})
    else:
        displaydata=immo_bien.objects.all()

    if request.method=="POST":
        exterieur= request.POST.get('exterieur')
        typologie=request.POST.get('typologie')
        garden=request.POST.get('garden')
        parking=request.POST.get('parking')
        searchresult1=immo_bien.objects.raw('select * from immo_bien where exterieur= "'+exterieur+'" and typologie="'+typologie+'" and garden="'+garden+'"and parking="'+parking+'"')
        return render(request, 'index.html', {"immo_bien":searchresult1})
    else:
        displa=immo_bien.objects.raw('select * from immo_bien')


    return render(request, 'index.html', {'posts': data, 'bien_immo':bien_immo, 'mean':mean, 'std':std, "date":displaydata, "immo_bien": displa})
