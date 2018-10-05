from django.db import models


class Site(models.Model):
    title = models.CharField('Title', max_length=50)

    def __str__(self):
        return '{} Site'.format(self.title)


class Value(models.Model):
    site = models.ForeignKey(Site, verbose_name='value_site', related_name='values', on_delete=models.CASCADE)
    a_value = models.FloatField(verbose_name='A Value')
    b_value = models.FloatField(verbose_name='B Value')
    date = models.DateField(verbose_name='Date', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Value'
        verbose_name_plural = 'Values'
