from app.models import Public,Private
from rest_framework import viewsets
from app.serializers import PrivateSerializer,PublicSerializer
from rest_framework.permissions import IsAuthenticated





class PrivateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Private.objects.all()
    serializer_class = PrivateSerializer


class PublicViewSet(viewsets.ModelViewSet):

    queryset = Public.objects.all()
    serializer_class = PublicSerializer




