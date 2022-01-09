from django.urls import path
from backend import views

urlpatterns = [
    path('',views.index,name="index"),
    path('itemApi',views.ItemAPIView.as_view(),name="itemApi"),
    path('itemApi/<item_id>',views.ItemAPIView.as_view())
]