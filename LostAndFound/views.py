from django.shortcuts import render


def item_list(request):
    return render(request, 'LostAndFound.html',{'item':range(5)})