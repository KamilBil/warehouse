from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post, Group
from .serializers import GroupSerializer, PostSerializer
class GroupView(viewsets.ViewSet):
    serializer = GroupSerializer
    def list(self, request):
        queryset = Group.objects.all()
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data)
class PostView(viewsets.ViewSet):
    serializer = PostSerializer
    def list(self, request):
        queryset = Post.objects.all()
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data,
            status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'Bad Request',
            'errors': serializer.errors,
            'message': serializer.is_valid()},
            status=status.HTTP_400_BAD_REQUEST)
