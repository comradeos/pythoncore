from django.db import models

# Create your models here.
# После изменений
# python manage.py makemigrations
# python manage.py migrate


class MyFourthTable(models.Model):
    class Meta:
        verbose_name_plural = 'MyFourthTable'
    value = models.CharField(max_length=255)

    def __str__(self):  # отображение в таблице /admin
        return f'{self.value}'


class MyThirdTable(models.Model):
    class Meta:
        verbose_name_plural = 'MyThirdTable'
    value = models.CharField(max_length=255)

    def __str__(self):  # отображение в таблице /admin
        return f'{self.value}'


class MySecondTable(models.Model):
    class Meta:
        verbose_name_plural = 'MySecondTable'
    name = models.CharField(max_length=255)

    def __str__(self):  # отображение в таблице /admin
        return f'{self.name}'


class MyFirstTable(models.Model):
    class Meta:
        verbose_name_plural = 'MyFirstTable'
    intv = models.IntegerField()
    charv = models.CharField(max_length=255)
    many_to_one = models.ForeignKey(MySecondTable, on_delete=models.CASCADE, null=True)  # связь many to one
    many_to_many = models.ManyToManyField(MyThirdTable)  # связь many to many
    one_to_one = models.OneToOneField(MyFourthTable, on_delete=models.CASCADE, null=True)  # связь one to one

    def __str__(self):  # отображение в таблице /admin
        return f'{self.charv}'
