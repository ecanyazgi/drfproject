from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser,AllowAny,DjangoModelPermissionsOrAnonReadOnly,BasePermission,SAFE_METHODS

class PostWritePermission(BasePermission):
    message = 'Yoo stop nigger'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostWritePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
