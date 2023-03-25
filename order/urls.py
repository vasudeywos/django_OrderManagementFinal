from django.urls import path,re_path
from . import views
#from .views import searchposts
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', views.order, name='order_pg'),
    path('', PostListView.as_view(), name='order_pg'),
    path('search/', views.searchbar, name='search'),
    path('tag-search/', views.search_tag, name='tag-search'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tag/', views.index, name='tag'),
    path('tags/<slug:tag_slug>/', views.TagIndexView.as_view(), name='posts_by_tag'),
    path('fav/<int:id>/',views.favourite_add, name='favourite_add'),
    path('favourites/',views.favourite_list, name='favourite_list'),
    ]
