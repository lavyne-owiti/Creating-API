from dataclasses import fields
from importlib.metadata import MetadataPathFinder
from pyexpat import model
from rest_framework import serializers
from .models import Trsansaction

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model =Trsansaction
        fields =('amount','date','description')

