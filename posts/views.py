# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# from .models import Post, Comment
# from .forms import PostForm
# from django.views import generic
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import PostSerializer
#
#
# @api_view(['GET', 'POST'])
# def index(request):
#     # return HttpResponse('<h1>Welcome to Django</h1>')
#
#     # print(request.data)
#     # return Response(dict(request.data))
#     # return Response(dict(request.data))
#     # print(foo)
#     # return Response({'name': 'Ali'}, status=status.HTTP_400_BAD_REQUEST)
#
#     # pk = request.query_params.get('pk')
#     pk = request.data.get('pk')
#     print(request.data)
#     try:
#         p = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response({'details': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     serializer = PostSerializer(p)
#     # print(serializer)
#     # print('=' * 40)
#     # print(serializer.data)
#     return Response(serializer.data)
#
#
# def home(request):
#
#     return HttpResponse('<h3> Welcome to my site</h3>')
#
#
# # def post_list(request):
# #     posts = Post.objects.all()
# #     context = {'posts': posts}
# #     return render(request, 'posts/post_list.html', context=context)
# #
#
# class PostList(generic.ListView):
#     queryset = Post.objects.all()
#     template_name = 'posts/post_list.html'
#     context_object_name = 'posts'
#
#
# def post_detail(request, post_id):
#     # try:
#     #     post = Post.objects.get(pk=post_id)
#     # except Post.DoesNotExist:
#     #     return HttpResponseNotFound('Post in not exist!')
#     post = get_object_or_404(Post, pk=post_id)
#
#     # comments = Comment.objects.filter(post=post_id)
#     comments = Comment.objects.filter(post=post)
#     context = {'post': post, 'comments': comments}
#     return render(request, 'posts/post_detail.html', context=context)
#
#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html'
#     # context_object_name = 'posts'
#     #
#     # def get_queryset(self):
#     #     return get_object_or_404(Post, pk=self.request.POST['post_id'])
#
#     def get_context_data(self, **kwargs):
#         context = super(PostDetail, self).get_context_data()
#         print(kwargs)
#         context['comments'] = Comment.objects.filter(post=kwargs['object'].pk)
#         return context
#
#
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             print(type(form.cleaned_data))
#             print(form.cleaned_data)
#             Post.objects.create(**form.cleaned_data)
#             return HttpResponseRedirect('/posts/')
#     else:
#         form = PostForm()
#
#     return render(request, 'posts/post_create.html', {'form': form})


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404
# from .models import Post
# from .serializers import PostSerializer


# class PostListView(APIView):
#
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetailView(APIView):
#
#     def get_object(self, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
#         return post
#
#     def get(self, request, pk):
#         # try:
#         #     post = Post.objects.get(pk=pk)
#         # except Post.DoesNotExist:
#         #     return Response(status.HTTP_404_NOT_FOUND)
#
#         post = self.get_object(pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         # try:
#         #     post = Post.objects.get(pk=pk)
#         # except Post.DoesNotExist:
#         #     return Response(status.HTTP_404_NOT_FOUND)
#
#         post = self.get_object(pk=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk=pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from django.http import Http404
#
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework import generics
# from rest_framework import mixins
#
# from .serializers import PostSerializer
# from .models import Post
#
#
# class PostListView(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PostDetailView(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#
# from rest_framework import generics
#
# from .serializers import PostSerializer
# from .models import Post
#
#
# class PostListView(generics.ListCreateAPIView):
#
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


from rest_framework import viewsets

from .serializers import PostSerializer
from .models import Post


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



