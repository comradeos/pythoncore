from django.contrib import admin
from .models import MyFirstTable, MySecondTable, MyThirdTable, MyFourthTable

# Register your models here.
admin.site.register(MyFirstTable)  # зарегистрировать в админке
admin.site.register(MySecondTable)
admin.site.register(MyThirdTable)
admin.site.register(MyFourthTable)
