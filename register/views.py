from register.serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class Register(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        context = {'request': request}
        serialized = self.serializer_class(data=request.data, context=context)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        data = {'success': True}
        data.update(serialized.data)
        return Response(data=data
                        , status=status.HTTP_201_CREATED)
