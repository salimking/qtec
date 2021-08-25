from django.shortcuts import render
from .models import Story
from django.db.models import Q
# import re
# Create your views here.
def home(request):
                         
    return  render(request,'index.html')



def search(request):
    
    if request.method=='GET':
        
        query=None
        total=0
        if request.method=="GET":
            query=request.GET.get('search')
            
            results=Story.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(footer__icontains=query) )
            total+=results.count()
        return  render(request,'result.html',{'query': query,
                                            'total': total,
                                            'results':results})

def detail(request,id):
    obj=Story.objects.get(id=id) 
    con={
        'obj':obj
    }     
    return render(request,'detail.html',con)                                      

