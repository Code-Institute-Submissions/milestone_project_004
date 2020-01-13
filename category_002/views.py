from django.shortcuts import render
from .models import Category_002

# Create your views here.
def all_images_002(request):
    images = Category_002.objects.all()
    return render(request, "app_001/catagory_002.html", {"category_002": images})
