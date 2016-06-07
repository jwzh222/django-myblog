from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.views import generic
from datetime import datetime
from django.http import Http404

# Create your views here.

def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'article/home.html', {'post_list' : post_list})

class HomeView(generic.ListView):
	template_name='article/home.html'
	context_object_name='post_list'
	
	def get_queryset(self):
		return Article.objects.order_by('date_time')[:5]



def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/post.html', {'post' : post})

class DetailView(generic.DetailView):
	template_name='article/post.html'
	model=Article

class ArchivesView(generic.ListView):
        template_name='article/archives.html'
        context_object_name='post_list'

        def get_queryset(self):
                return Article.objects.all()


def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'article/tag.html', {'post_list' : post_list})

