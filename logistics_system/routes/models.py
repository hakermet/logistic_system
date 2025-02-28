from django.db import models
from django.conf import settings  # Змінено імпорт

class Route(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Замість User використовуємо settings.AUTH_USER_MODEL
        on_delete=models.CASCADE,
        related_name='routes'
    )
    start_place = models.CharField(max_length=255, verbose_name="Початкова точка")
    end_place = models.CharField(max_length=255, verbose_name="Кінцева точка")
    start_lat = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="Початкова широта")
    start_lng = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="Початкова довгота")
    end_lat = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="Кінцева широта")
    end_lng = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="Кінцева довгота")
    distance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Відстань (км)")
    duration = models.IntegerField(verbose_name="Тривалість (хв)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.start_place} → {self.end_place}"