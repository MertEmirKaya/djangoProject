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





class CodeNightDetailAPIView(APIView):
    def get_object(self,pk):
        codenight_instance=get_object_or_404(CodeNight,pk=pk)
        return codenight_instance


    def get(self,request,pk):
        codenight=self.get_object(pk=pk)    
        serializer=CodeNightSerializer(codenight)
        return Response(serializer.data )
    
    def put(self,request,pk):
        codenight=self.get_object(pk=pk) 
        serializer=CodeNightSerializer(codenight,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        codenight=self.get_object(pk=pk) 
        codenight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)