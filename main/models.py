from django.db import models


class Hello(models.Model):
    froms = models.CharField("От кого", max_length=50)
    hello = models.TextField('Ваш привет')

    def __str__(self):
        return self.froms

    class Meta:
        verbose_name = 'Привет'
        verbose_name_plural = 'Приветы'