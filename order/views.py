from django.shortcuts import render,get_object_or_404, HttpResponseRedirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Orders
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from .form import PostForm

Orderss=[
        {'Name':'Phone Adapter',
         'Order_Number':10,
         'Quantity':5,
         },{'Name':'Television',
            'Order_Number':15,
            'Quantity':2,
         },{'Name':'Refrigerator',
            'Order_Number':16,
            'Quantity':5,
         },{'Name':'Microwave',
            'Order_Number':12,
            'Quantity':7,
         },{'Name':'Speaker',
            'Order_Number':11,
            'Quantity':6,
         }
    ]
def order(request):
    context={'orde':Orders.objects.all()}
    return render(request, 'order/odr.html',context)

class PostListView(ListView):
    model=Orders
    template_name = 'order/odr.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'orde'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
        model = Orders


class PostCreateView(LoginRequiredMixin, CreateView):
    model =Orders
    fields=['Name', 'Order_Number','Quantity','tags']

    def form_valid(self, form):
         form.instance.author=self.request.user
         return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Orders
    fields = ['Name', 'Order_Number','Quantity','tags']

    def form_valid(self, form):
         form.instance.author=self.request.user
         return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Orders
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def searchbar(request):
    if request.method=='GET':
        query=request.GET.get('query')
        if query:
            obj=Orders.objects.filter(Order_Number__icontains=query)
            return render(request,'order/search.html',{'orde':obj})
        else:
            print('No Info')
            return(request,'order/search.html',{})

def search_tag(request):
    if request.method=='GET':
        query=request.GET.get('tag_query')
        if query:
            obj=Orders.objects.filter(tags__name__icontains=query)
            return render(request,'order/tagsearch.html',{'orde':obj})
        else:
            print('No Info')
            return(request,'order/tagsearch.html',{})

def index(request):
    ord = Orders.objects.prefetch_related('tags').all()
    tags = Tag.objects.all()
    context = {'ord': ord, 'tags': tags}
    return render(request, 'order/tagger.html', context)

#TAGSSS!!!!!
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class TagIndexView(TagMixin,ListView):
    model = Orders
    template_name = 'order/tagger.html'
    context_object_name = 'ord'

    def get_queryset(self):
        return Orders.objects.filter(tags__slug=self.kwargs.get('tag_slug'))

@login_required
def favourite_add(request,id):
    post=get_object_or_404(Orders,id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favourite_list(request):
    new=Orders.objects.filter(favourites=request.user)
    return render(request,'order/favourites.html',{'new':new})



