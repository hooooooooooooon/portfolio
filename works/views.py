from rest_framework.viewsets import ModelViewSet
from .models import Work
from .serializers import WorkSerializer


class WorkViewSet(ModelViewSet):

    serializer_class = WorkSerializer
    queryset = Work.objects.all()