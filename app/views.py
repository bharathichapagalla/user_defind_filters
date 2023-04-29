from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'HaI how ARE yoU'}
    return render(request,'filters.html',d)