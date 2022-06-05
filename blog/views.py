from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from .models import post, category
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from datetime import datetime


# Create your views here.

def one(request):
    pages = Paginator(post.objects.all(), 4)
    num = request.GET.get('page')
    try:
        page = pages.page(num)
    except PageNotAnInteger:
        page = pages.page(1)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    posts = post.published.all()
    x = datetime.now()
    x = x.year
    return render(request, 'index.html', {'post' : posts})



def display(request, year, month, day, slug):
    pst = get_object_or_404(post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'page.html', {'post' : pst})


class add_post(CreateView):
    model = post
    template_name = 'add_post.html'
    fields = ['title', 'slug', 'body', 'photo', 'status']
    success_url = reverse_lazy('one')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class edit(UpdateView):
    model = post
    template_name = 'update.html'
    fields = ['author', 'title', 'body', 'publish', 'status', 'photo']
    success_url = reverse_lazy('one')

class delete(DeleteView):
    model = post
    template_name = 'delete.html'
    success_url = reverse_lazy('one')



def registeruser(request):
    if request.user.is_authenticated:
        return redirect('one')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('one')
        return render(request, 'register.html', {'form' : form})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('one')
    else:
        if request.method == 'POST':
            usr = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(username=usr, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('one')
        return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('one')



def search(request):
    query = request.GET.get('query')
    if query == "":
        return redirect('one')
    posts = post.objects.filter(
        Q(title__icontains=query) | Q(body__icontains=query)
    )
    return render(request, 'search.html', {'posts' : posts})


    
def categories(request, slug):
    posts = post.objects.filter(cate__slug=slug)
    n = category.objects.get(slug=slug)
    return render(request, 'categoris.html', {'posts' : posts, 'catname' : n})



def year_filter(request, month, year):
    posts = post.objects.filter(publish__month=month, publish__year=year)
    return render(request, 'date.html', {'posts' : posts})
