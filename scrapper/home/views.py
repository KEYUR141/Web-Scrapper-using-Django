from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from scrapper_script import *
from django.db.models import Q
from home.models import *
from home.tasks import *
# Create your views here.

def imdb_run_scrapper(request):
    scrape_imdb_news()
    return JsonResponse({
        "status": True,
        "Message":"IMDB Scrapper Executed"
    })

def imdb_index(request):
    data = IMBD_News.objects.all()
    # Handle navbar search redirect
    navbar_search = request.GET.get('navbar_search')
    if navbar_search:
        return redirect(f"/imdb_scrap?imdb_search={navbar_search}")

    search = request.GET.get('imdb_search')
    if search:
        data = data.filter(
            Q(title__icontains = search) |
            Q(description__icontains = search)
        )
    return render(request,"IMDBindex.html",context={
        'data':data,
        'imdb_search':search or request.GET.get('navbar_search')
    })
    

def toi_run_scrapper(request):
    scrape_toi_news()

    return JsonResponse({
        "status": True,
        "Message":"Times of India Scrapper Executed"
    })

def toi_index(request):

    data = TOI_News.objects.all()
    # Handle navbar search redirect
    navbar_search = request.GET.get('navbar_search')
    if navbar_search:
        return redirect(f"/toi_scrap?toi_search={navbar_search}")

    search = request.GET.get('toi_search')
    if search:
        data = data.filter(
            Q(title__icontains = search) |
            Q(description__icontains = search)
        )
    return render(request,"TOIindex.html",context={
        'data':data,
        'toi_search':search or request.GET.get('navbar_search')
    })

def Main_Page(request):
    return render(request,'NavBar.html')

def main_index(request):
    print(add.delay(10,20))
    return JsonResponse( {
        "status":True
    })
    