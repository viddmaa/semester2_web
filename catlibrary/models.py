from django.db import models
from django.urls import reverse


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

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('catlibrary:breed_detail', kwargs={'pk': self.pk})
    

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
