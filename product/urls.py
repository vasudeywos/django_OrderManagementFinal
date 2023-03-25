from django.urls import path
from . import views
#from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView

urlpatterns = [
    path('product/', views.prdct, name='order-home')
                ]