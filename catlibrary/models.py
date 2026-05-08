from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название породы'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    average_weight = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name='Средний вес'
    )
    life_expectancy = models.IntegerField(
        verbose_name='Средняя продолжительность жизни'
    )

    image = models.ImageField(
        upload_to='breeds/',
        verbose_name='Фото породы',
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('catlibrary:breed_detail', kwargs={'pk': self.pk})
    

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
