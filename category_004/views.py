from django.shortcuts import render
from .models import Category_004

# Create your views here.
def all_images_004(request):
    images = Category_004.objects.all()
    return render(request, "app_001/catagory_004.html", {"category_004": images})