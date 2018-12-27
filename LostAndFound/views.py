from django.shortcuts import render
from django.views.generic.base import View
from .models import Item

class ItemList(View):

    def get(self,request):
        all = Item.objects.all()
        return render(request, 'LostAndFound.html',{'item':range(5)})