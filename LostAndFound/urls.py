from django.conf.urls import url
from .views import item_list
urlpatterns = [
    url(r'^$',item_list.as_View()),
]