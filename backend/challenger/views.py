# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Challenger
from .serializers import ChallengerSerializer

# Create your views here.

class ChallengerList(APIView):
    # Challenger list를 보여줄 때
    def get(self, request):
        challengers = Challenger.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = ChallengerSerializer(challengers, many=True)
        return Response(serializer.data)

    # 새로운 Challenger 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = ChallengerSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Challenger의 detail을 보여주는 역할
class ChallengerDetail(APIView):
    # Challenger 객체 가져오기
    def get_object(self, pk):
        try:
            return Challenger.objects.get(pk=pk)
        except Challenger.DoesNotExist:
            raise Http404
    
    # Challenger의 detail 보기
    def get(self, request, pk, format=None):
        challenger = self.get_object(pk)
        serializer = ChallengerSerializer(challenger)
        return Response(serializer.data)

    # Challenger 수정하기
    def patch(self, request, pk, format=None):
        challenger = self.get_object(pk)
        serializer = ChallengerSerializer(challenger, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Challenger 삭제하기
    def delete(self, request, pk, format=None):
        challenger = self.get_object(pk)
        challenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  