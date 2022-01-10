from django.http.response import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework import status
from backend.models import Item, ItemSerializer
from django.http import JsonResponse
import csv

def index(request):
    return render(request,"index.html")

class ItemAPIView(APIView):
    def get(self,request):
        items=Item.objects.all()
        serializer=ItemSerializer(items,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        item_serializer=ItemSerializer(data=json.loads(request.body))
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Item saved successfully")
        return Response(item_serializer.errors)

    def put(self,request,item_id):
        try:
            item=Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            raise Http404
        serializer=ItemSerializer(item,data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response("Updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,item_id):
        try:
            item=Item.objects.get(pk=item_id)
            name=str(item)
        except Item.DoesNotExist:
            raise Http404
        item.delete()
        return Response(f"Deleted item = {item}")

def exportData(request):
    header=['id','Item name','Price(per item)','Quantity']
    items=[[item.id,item.name,item.price,item.quantity] for item in Item.objects.all()]
    with open("data.csv","w") as file:
        writer=csv.writer(file)
        writer.writerow(header)
        writer.writerows(items)
    return JsonResponse("Items data exported to data.csv file",safe=False)