from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers import CodeNightSerializer
from codenight.models import CodeNight

class CreateListCodenightAPIView(APIView):
    def get(self,request):
        codenights= CodeNight.objects.filter(aktif=True)
        serializer=CodeNightSerializer(codenights,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=CodeNightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)