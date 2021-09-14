
from ModelViewSet_App.models import Employee
from ModelViewSet_App.api.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    authentication_classes = (BasicAuthentication,)

    permission_classes = (IsAuthenticated,)







