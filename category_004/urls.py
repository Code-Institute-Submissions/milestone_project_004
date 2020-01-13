from django.conf.urls import url, include
from .views import all_images_004

urlpatterns = [
    url(r'^$', all_images_004, name='category_004'),
]