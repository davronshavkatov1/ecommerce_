
from django.urls import path
from .views import *
urlpatterns = [

    path('', index, name='index'),
    path('store/', store, name='store'),
    path('store/<slug:category_slug>/', store, name='store_by_category'),   
    path('store/<slug:category_slug>/<slug:product_slug>/', product_detail, name="product_detail"), 
  


] 