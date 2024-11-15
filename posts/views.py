# posts/views.py
from rest_framework import generics,permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly # new


class PostList(generics.ListCreateAPIView):
   #permission_classes = (IsAuthorOrReadOnly,)  # Un permiso customizado
   permission_classes = (permissions.IsAuthenticated,) # para permiso ver solo cuando esta autentificado
   queryset = Post.objects.all()
   serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = (permissions.IsAuthenticated,)
   #permission_classes = (IsAuthorOrReadOnly,) # new
   queryset = Post.objects.all()
   serializer_class = PostSerializer   

   