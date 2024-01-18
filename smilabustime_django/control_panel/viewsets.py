from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class Route3ViewSet(ModelViewSet):
    queryset = route_3.objects.all()
    serializer_class = Route3Serializer
    permission_classes = [IsAuthenticated]


class Route4ViewSet(ModelViewSet):
    queryset = route_4.objects.all()
    serializer_class = Route4Serializer


class Route5ViewSet(ModelViewSet):
    queryset = route_5.objects.all()
    serializer_class = Route5Serializer


class Route17ViewSet(ModelViewSet):
    queryset = route_17.objects.all()
    serializer_class = Route17Serializer


class Route30ViewSet(ModelViewSet):
    queryset = route_30.objects.all()
    serializer_class = Route30Serializer


class Route32ViewSet(ModelViewSet):
    queryset = route_32.objects.all()
    serializer_class = Route32Serializer


class Route34ViewSet(ModelViewSet):
    queryset = route_34.objects.all()
    serializer_class = Route34Serializer


class Route39ViewSet(ModelViewSet):
    queryset = route_39.objects.all()
    serializer_class = Route39Serializer


class Route40ViewSet(ModelViewSet):
    queryset = route_40.objects.all()
    serializer_class = Route40Serializer


class Route41ViewSet(ModelViewSet):
    queryset = route_41.objects.all()
    serializer_class = Route41Serializer


class Route48ViewSet(ModelViewSet):
    queryset = route_48.objects.all()
    serializer_class = Route48Serializer


class Route49ViewSet(ModelViewSet):
    queryset = route_49.objects.all()
    serializer_class = Route49Serializer


class Route126ViewSet(ModelViewSet):
    queryset = route_126.objects.all()
    serializer_class = Route126Serializer


class Route129ViewSet(ModelViewSet):
    queryset = route_129.objects.all()
    serializer_class = Route129Serializer


class Route135ViewSet(ModelViewSet):
    queryset = route_135.objects.all()
    serializer_class = Route135Serializer


class Route139ViewSet(ModelViewSet):
    queryset = route_139.objects.all()
    serializer_class = Route139Serializer


class Route140ViewSet(ModelViewSet):
    queryset = route_140.objects.all()
    serializer_class = Route140Serializer


class Route141ViewSet(ModelViewSet):
    queryset = route_141.objects.all()
    serializer_class = Route141Serializer


class Route150ViewSet(ModelViewSet):
    queryset = route_150.objects.all()
    serializer_class = Route150Serializer


class Route151ViewSet(ModelViewSet):
    queryset = route_151.objects.all()
    serializer_class = Route151Serializer


class Route152ViewSet(ModelViewSet):
    queryset = route_152.objects.all()
    serializer_class = Route152Serializer


class Route153ViewSet(ModelViewSet):
    queryset = route_153.objects.all()
    serializer_class = Route153Serializer


class Route154ViewSet(ModelViewSet):
    queryset = route_154.objects.all()
    serializer_class = Route154Serializer


class Route155ViewSet(ModelViewSet):
    queryset = route_155.objects.all()
    serializer_class = Route155Serializer


class Route302ViewSet(ModelViewSet):
    queryset = route_302.objects.all()
    serializer_class = Route302Serializer


class Route309ViewSet(ModelViewSet):
    queryset = route_309.objects.all()
    serializer_class = Route309Serializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ClickCounterViewSet(ModelViewSet):
    queryset = ClickCounter.objects.all()
    serializer_class = ClickCounterSerializer
    


all_viewsets = {
    'route_3': Route3ViewSet,
    'route_4': Route4ViewSet,
    'route_5': Route5ViewSet,
    'route_17': Route17ViewSet,
    'route_30': Route30ViewSet,
    'route_32': Route32ViewSet,
    'route_34': Route34ViewSet,
    'route_39': Route39ViewSet,
    'route_40': Route40ViewSet,
    'route_41': Route41ViewSet,
    'route_48': Route48ViewSet,
    'route_49': Route49ViewSet,
    'route_126': Route126ViewSet,
    'route_129': Route129ViewSet,
    'route_135': Route135ViewSet,
    'route_139': Route139ViewSet,
    'route_140': Route140ViewSet,
    'route_141': Route141ViewSet,
    'route_150': Route150ViewSet,
    'route_151': Route151ViewSet,
    'route_152': Route152ViewSet,
    'route_153': Route153ViewSet,
    'route_154': Route154ViewSet,
    'route_155': Route155ViewSet,
    'route_302': Route302ViewSet,
    'route_309': Route309ViewSet,
    'users': UsersViewSet,
    'click_counter': ClickCounterViewSet,
}