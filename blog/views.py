from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from blog.models import *
from blog import serializers
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from django.views.generic import ListView
# Create your views here.

#首页
class Index_List(ListView):
    template_name = 'blog_index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.all().order_by('-created_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_three'] = Posts.objects.all().order_by('-views')[:5]
        context['cate_all'] = Category.objects.all()
        return context



# 文章详情页
def detail(request, article_id):
    post = get_object_or_404(Posts, pk=article_id)
    post.increase_views()
    return render_to_response('blog_detail.html', context={'detail': post})

#分类详情页
def category(request, cate_id):
    category_list = Category.objects.get(id=cate_id).Get_Posts.all()
    category_name = Category.objects.get(id=cate_id)
    return render(request, 'blog_category.html', locals())



class Search(ListView):
    model = Posts
    template_name = 'blog_search.html'

    def get_queryset(self):
        key =self.request.GET['key']
        if key:
            return Posts.objects.filter(Q(title__icontains=key))
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = self.request.GET['key']
        return context



#JSON
class ListPosts(APIView):

   def get(self, request, format=None):
       p_all = Posts.objects.all()
       s = serializers.PostSerializer(p_all, many=True)
       return Response(s.data)


class DetailPosts(generics.RetrieveAPIView):

    def get(self,request,format=None):
        pass


