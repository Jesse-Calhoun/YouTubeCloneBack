from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Reply
from ..comments.models import Comment
from .serializers import ReplySerializer
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_replies(request, video_id, comment_id):
    # comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(video_id=video_id)
        replies = Reply.objects.filter(comment_id=comment_id)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)