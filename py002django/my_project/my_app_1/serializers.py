from rest_framework.serializers import ModelSerializer
from my_app_1.models import MyFirstTable


class MyFirstSerializer(ModelSerializer):
    class Meta:
        model = MyFirstTable
        fields = [
            'id',
            'charv',
        ]
