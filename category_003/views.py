from django.shortcuts import render
from .models import Category_003

# Create your views here.
def all_images_003(request):
    images = Category_003.objects.all()
    return render(request, "app_001/catagory_003.html", {"category_003": images})
