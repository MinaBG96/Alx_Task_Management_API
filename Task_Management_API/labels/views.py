from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Label , Task
from .serializers import LabelSerializer


class LabelListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        labels = Label.objects.filter(owner=request.user)
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Label, pk=pk, owner=user)

    def get(self, request, pk):
        label = self.get_object(pk, request.user)
        serializer = LabelSerializer(label)
        return Response(serializer.data)

    def put(self, request, pk):
        label = self.get_object(pk, request.user)
        serializer = LabelSerializer(
            label,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        label = self.get_object(pk, request.user)
        label.delete()
        return Response(
            {"message": "Label deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
        
        
class TaskLabelAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id, label_id):
        task = get_object_or_404(Task, id=task_id, owner=request.user)
        label = get_object_or_404(Label, id=label_id, owner=request.user)

        task.labels.add(label)
        return Response(
            {"message": "Label attached to task successfully"},
            status=status.HTTP_200_OK
        )

    def delete(self, request, task_id, label_id):
        task = get_object_or_404(Task, id=task_id, owner=request.user)
        label = get_object_or_404(Label, id=label_id, owner=request.user)

        task.labels.remove(label)
        return Response(
            {"message": "Label removed from task successfully"},
            status=status.HTTP_204_NO_CONTENT
        )