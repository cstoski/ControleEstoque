from multiprocessing.util import abstract_sockets_supported
from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em'
        auto_now_add = True, 
        auto_now=False
    )
    modfied = models.DateTimeField(
        'Modificado em',
        auto_now_add = False, 
        auto_now=True
    )
    class Meta:
        abstract = True
