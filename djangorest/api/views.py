from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import MainInfoSerializer
from .serializers import ExperienceInfoSerializer
from .serializers import SkillsInfoSerializer
from .serializers import ProyectsInfoSerializer
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from .serializers import CommentsSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import MainInfo
from .models import ExperienceInfo 
from .models import SkillsInfo 
from .models import ProyectsInfo
from .models import Comments  
from rest_framework.response import Response
from rest_framework import status

class MainInfoList(APIView):
    def get(self, request, format=None):
        maininfo = MainInfo.objects.all()
        serializer = MainInfoSerializer(maininfo, many=True)
        return Response(serializer.data)


class ExperienceInfoList(APIView):
    def get(self, request, format=None):
        experienceinfo = ExperienceInfo.objects.all()
        serializer = ExperienceInfoSerializer(experienceinfo, many=True)
        return Response(serializer.data)


class SkillsInfoList(APIView):
    def get(self, request, format=None):
        skillsinfo = SkillsInfo.objects.all()
        serializer = SkillsInfoSerializer(skillsinfo, many=True)
        return Response(serializer.data)


class ProyectsInfoList(APIView):
    def get(self, request, format=None):
        proyectsinfo = ProyectsInfo.objects.all()
        serializer = ProyectsInfoSerializer(proyectsinfo, many=True)
        return Response(serializer.data)


class CommentsList(APIView):
    def get(self, request, format=None):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect("http://18.216.46.196:5000")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsDetail(APIView):
    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comments = self.get_object(pk)
        serializer = CommentsSerializer(comments)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comments = self.get_object(pk)
        serializer = CommentsSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comments = self.get_object(pk)
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

