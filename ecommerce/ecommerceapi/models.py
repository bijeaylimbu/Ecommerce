from django.db import models

# Create your models here.
class Categories(models.Model):
    title=models.CharField(max_length=255)

    class meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return  self.title

WARRENTY=[('YES','YES'),('NO','NO')]
class MobileCharger(models.Model):
    title=models.CharField(max_length=255)
    category=models.ForeignKey(Categories,related_name='cell_phone',on_delete=models.CASCADE)
    brand=models.CharField(max_length=255)
    color=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    warrenty=models.CharField(max_length=255,choices=WARRENTY)
    date_created=models.DateField(auto_now_add=True)
    imageUrl=models.URLField()

    class Meta:
        ordering=['title']


class Headphone(models.Model):
    brand=models.CharField(max_length=255)
    color=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    warrenty=models.CharField(max_length=255,choices=WARRENTY)
    category=models.ForeignKey(Categories,related_name='headphone',on_delete=models.CASCADE)
    imageUrl=models.URLField()
    created_at=models.DateField(auto_now_add=True)
