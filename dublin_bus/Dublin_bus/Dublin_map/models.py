from django.db import models

class BookInfo(models.Model):

    btitle = models.CharField(max_length=20,verbose_name='bookname')
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)

    hgender = models.BooleanField(default=False)

    hcomment = models.CharField(max_length=128)

    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):

        return self.hname



class Bus_Locations(models.Model):

    stop_id = models.IntegerField(primary_key=True,verbose_name='stop_id')

    stop_name = models.CharField(max_length=50, verbose_name='stop_name')

    # latitude = models.DecimalField(max_digits=15, decimal_places=9,verbose_name='latitude')
    latitude = models.FloatField(null=True, blank=True, default=None,verbose_name='latitude')

    # longitude =models.DecimalField(max_digits=15, decimal_places=9,verbose_name='longitude')
    longitude = models.FloatField(null=True, blank=True, default=None,verbose_name='longitude')


    def __str__(self):

        return self.stop_name