from django.db import models

class Ads(models.Model):
    # Класс отображает таблицу с рекламными объявлениями
    ads_title = models.CharField(max_length=100, blank=True, default='Рекламное объявление', verbose_name='Название объявления')
    ads_showing = models.IntegerField(blank=True, default=5, verbose_name='Частота показов')
    ads_author = models.ForeignKey('auth.User', related_name="outputs", on_delete=models.CASCADE, verbose_name='Пользователь')
    ads_url = models.URLField(max_length=200, verbose_name='Ссылка')
    ads_email = models.EmailField(max_length=254, verbose_name='Email')
    ads_category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    ads_description = models.TextField(max_length=250, verbose_name='Описание')
    ads_image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    ads_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    ads_accept = models.BooleanField(blank=True, default=False,verbose_name='Принято')

    def __str__(self):
        return self.ads_title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-ads_created_at']


class Script(models.Model):
    # Класс отображает таблицу с данными для получения скриптов
    script_showing = models.IntegerField(blank=True, default=5, verbose_name='Частота показов')
    script_url = models.URLField(max_length=200, verbose_name='Ссылка')
    script_email = models.EmailField(max_length=254, verbose_name='Email')
    script_category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория сайта пользователя')
    script_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Скрипт'
        verbose_name_plural = 'Скрипты'
        ordering = ['-script_created_at']


class Category(models.Model):
    # Класс отображает категории для рекламных объявлений
    category_title = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_title']