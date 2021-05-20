from django.shortcuts import render
from rest_framework import viewsets, status, parsers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExecutableSerializer
from .models import ExecutableModel
from .utils.docker_utils import run_alpine


class ExecutableViewSet(viewsets.ModelViewSet):
    queryset = ExecutableModel.objects.all().order_by('id')
    serializer_class = ExecutableSerializer
    parser_classes = [parsers.MultiPartParser,
                      parsers.FormParser]


def container_view(request):
    if request.method == 'GET':
        run_alpine()
        return Response()


# # V2
# @api_view(['GET', 'POST'])
# def file(request):
#     # User requesting file download
#     if request.method == 'GET':
#         snippets = FileTest.objects.all()
#         serializer = FileSerializer(snippets, many=True)
#         return Response(serializer.data)
#     # User uploading a file
#     elif request.method == 'POST':
#         serializer = FileSerializer(data=request.data)
#         if serializer.is_valid():
#             # Upload to database
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
