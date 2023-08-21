# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from .models import Members
# from .serializers import MembersSerializer

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls={
#         'List': '/list/',
#         'Detail View' : '/detail/<int:year>/',
#         'Create' : '/create/',
#         'Update':'/update/<int:std_id>/',
#         'Delete':'/delete/<int:std_id>/'
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def memberList(request):
#     member=Members.objects.all()
#     serializer=MembersSerializer(member, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def memberDetail(request, year):
#     member=Members.objects.filter(year=year)
#     serializer=MembersSerializer(member, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def memberCreate(request):
#     serializer=MembersSerializer(data=request.data)
#     try:
#         if serializer.is_valid():
#             serializer.save()
#     except Exception as e:
#         print("저장 안됨")
#         return Response(str(e))
#     return Response(serializer.data)

# @api_view(['POST'])
# def memberUpdate(request, std_id):
#     member=Members.objects.get(std_id=std_id)
#     serializer=MembersSerializer(instance=member, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     else:
#         print("업데이트 안됨")
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def memberDelete(request, std_id):
#     try:
#         member = Members.objects.get(std_id=std_id)
#         print(member)
#         member.delete()
#         return Response("Member successfully deleted!")
#     except Exception as e:
#         return Response(str(e))


from .models import Members
from .serializers import MembersSerializer
from rest_framework import viewsets


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
