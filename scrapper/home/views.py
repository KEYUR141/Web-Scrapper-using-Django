from django.shortcuts import render
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

    search = request.GET.get('imdb_search')
    
    if search:
        
        
        data = data.filter(
            Q(title__icontains = search) |
            Q(description__icontains = search)
        )
        
 
    
    return render(request,"IMDBindex.html",context={
       
        'data':data,
        'imdb_search':search
    })
    

def toi_run_scrapper(request):
    scrape_toi_news()

    return JsonResponse({
        "status": True,
        "Message":"Times of India Scrapper Executed"
    })

def toi_index(request):

    data = TOI_News.objects.all()

    search = request.GET.get('toi_search')
    
    if search:
        
        
        data = data.filter(
            Q(title__icontains = search) |
            Q(description__icontains = search)
        )
        
 
    
    return render(request,"TOIindex.html",context={
        'data':data,
        'toi_search':search
    })

def Main_Page(request):
    return render(request,'NavBar.html')

def main_index(request):
    print(add.delay(10,20))
    return JsonResponse( {
        "status":True
    })
    