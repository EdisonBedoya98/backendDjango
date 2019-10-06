from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from machinlearningmodel.models import Clasiffier
from machinlearningmodel.serializers import ClasiffierSerializer
from rest_framework import generics
from joblib import dump, load
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import json
from pathlib import Path


# Create your views here.
@csrf_exempt
def index(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['texto']
    print(content)
    print('esto si está entrando alv')
    rawTweet=[content]
    df = pd.read_csv('machinlearningmodel/DB_tweets_Iphone.txt', delimiter = "\t", error_bad_lines=False,header=None)
    print('pasa segunda prueba')
    df.columns=['texto','sentimiento']
    X=df.iloc[:,0]
    vector=CountVectorizer(ngram_range=(1, 2))
    vector.fit(X)   
    
   

    tweet=vector.transform(rawTweet)
    #Se carga el modelo entrenado en la variable clf
    clf = load('machinlearningmodel/lrmodel.joblib')
    y = clf.predict(tweet)
    print(y) 
    responseData = {
        'feeling': y
        }
    dump=pd.Series(responseData).to_json(orient='values')
    print('llega al final :v')
    return JsonResponse(dump, safe=False)

class ClasiffierListCreate(generics.ListCreateAPIView):
    queryset = Clasiffier.objects.all()
    serializer_class = ClasiffierSerializer