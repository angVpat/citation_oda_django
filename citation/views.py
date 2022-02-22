from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models


class suppauteur(APIView):
    def post(self, request):
        bool = True
        _id_auteur = request.data.get('id_auteur')

        try:
            auteur = models.Auteur.objects.get(id_auteur=_id_auteur)
        except:
            return Response({'statusCode': 200, 'response': 'Auteur inexistant'})

        try:
            auteur.delete()
            return Response({'statusCode': 201, 'response': 'Suppression réussie'})
        except:
            return Response({'statusCode': 200, 'response': 'Echec de la suppression'})


class suppoeuvre(APIView):
    def post(self, request):
        bool = True
        _id_oeuvre = request.data.get('id_oeuvre')

        try:
            oeuvre = models.Oeuvre.objects.get(id_oeuvre=_id_oeuvre)
        except:
            return Response({'statusCode': 200, 'response': 'Oeuvre inexistante'})

        try:
            oeuvre.delete()
            return Response({'statusCode': 201, 'response': 'Suppression réussie'})
        except:
            return Response({'statusCode': 200, 'response': 'Echec de la suppression'})


class suppcitation(APIView):
    def post(self, request):
        bool = True
        _id_citation = request.data.get('id_citation')

        try:
            citation = models.Citation.objects.get(id_citation=_id_citation)
        except:
            return Response({'statusCode': 200, 'response': 'Citation inexistante'})

        try:
            citation.delete()
            return Response({'statusCode': 201, 'response': 'Suppression réussie'})
        except:
            return Response({'statusCode': 200, 'response': 'Echec de la suppression'})


class supptheme(APIView):
    def post(self, request):
        bool = True
        _id_theme = request.data.get('id_theme')

        try:
            theme = models.Theme.objects.get(id_theme=_id_theme)
        except:
            return Response({'statusCode': 200, 'response': 'Theme inexistant'})

        try:
            theme.delete()
            return Response({'statusCode': 201, 'response': 'Suppression réussie'})
        except:
            return Response({'statusCode': 200, 'response': 'Echec de la suppression'})
