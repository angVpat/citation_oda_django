from dataclasses import fields
from rest_framework import serializers

from citation.models import *

class AuteurSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = "__all__"

class OeuvreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Oeuvre
        fields = "__all__"

class Citation(serializers.ModelSerializer):
    class Meta:
        model = Citation
        fields = "__all__"

class Theme(serializers.ModelSerializer):
    class Meta:
        model= Theme
        fields = "__all__"

