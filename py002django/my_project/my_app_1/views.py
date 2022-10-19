from django.shortcuts import render
from my_app_1.models import MyFirstTable, MySecondTable, MyThirdTable, MyFourthTable
from rest_framework.viewsets import ModelViewSet
from .serializers import MyFirstSerializer


# Create your views here.


def my_view(request):
    items = MyFirstTable.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'my_app_1/my_template_1.html', context=context)


class MyFirstModelViewSet(ModelViewSet):
    queryset = MyFirstTable.objects.all()
    serializer_class = MyFirstSerializer


def vue_app_view(request):
    return render(request, 'my_app_1/vue_app.html')
