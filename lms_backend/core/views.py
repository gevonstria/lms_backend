from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class AuthenticationTest(APIView):

    def get(self, request):

        permission_classes = [IsAuthenticated] 

        content = {'message': 'Hello, World!'}
        return Response(content)
