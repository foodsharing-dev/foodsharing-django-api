from django.contrib.auth import logout
from django.middleware.csrf import get_token as generate_csrf_token_for_frontend
from rest_framework import status, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from foodsharing_api.session.serializers import AuthLoginSerializer
from foodsharing_api.users.serializers import UserSerializer


class SessionViewSet(viewsets.GenericViewSet):
    serializer_class = AuthLoginSerializer

    def status(self, request):
        """ Get the login state (logged in user)
        ---
        response_serializer: UserSerializer
        """
        generate_csrf_token_for_frontend(request)
        if request.user.is_anonymous():
            return Response(data={"error": "not_authed"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)

    def login(self, request, **kwargs):
        """ Log in
        ---
        request_serializer: AuthLoginSerializer
        response_serializer: UserSerializer
        """
        serializer = AuthLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(data=UserSerializer(request.user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def logout(self, request, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)
