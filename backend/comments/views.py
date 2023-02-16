from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_video_comments(request, video_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(video_id=video_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, video_id):
    print(
        'User', f"{request.user.id,}{request.user.email} {request.user.username}"
        )
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_comment(request, comment_id, video_id):
    print(
        'User', f"{request.user.id,}{request.user.email} {request.user.username}"
    )
    comment = get_object_or_404(Comment, pk=comment_id)
    video_id = comment.video_id
    if request.method == 'PUT':
        # comments = Comment.objects.filter(user_id=request.user.id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)