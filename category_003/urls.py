from django.conf.urls import url, include
from .views import all_images_003

urlpatterns = [
    url(r'^$', all_images_003, name='category_003'),
]