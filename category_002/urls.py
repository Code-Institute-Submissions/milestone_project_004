from django.conf.urls import url, include
from .views import all_images_002

urlpatterns = [
    url(r'^$', all_images_002, name='category_002'),
]