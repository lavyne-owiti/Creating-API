from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import TransactionSerializer
from .models import Trsansaction

# Create your views here.
# def get_transaction(request,id=None):
#     message=f"you submitted ID {id}"
#     return HttpResponse(message)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Trsansaction.objects.all().order_by('date')
    serializer_class=TransactionSerializer