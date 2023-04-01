from django.contrib import admin
from.models import *

# Подключение таблиц к сайту администратора
class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ads_accept', 'ads_author','ads_url', 'ads_email', 'ads_category', 'ads_created_at', 'ads_image')
    list_display_links = ('id', 'ads_accept', 'ads_author','ads_url', 'ads_email', 'ads_category', 'ads_created_at', 'ads_image')
    list_filter = ('ads_accept', 'ads_category')


class ScriptAdmin(admin.ModelAdmin):
    list_display = ('id', 'script_url', 'script_email', 'script_category', 'script_created_at')
    list_display_links = ('id', 'script_url', 'script_email', 'script_category', 'script_created_at')
    list_filter = ('script_category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_title')
    list_display_links = ('id', 'category_title')
    search_fields = ('category_title',)


admin.site.register(Ads, AdsAdmin)
admin.site.register(Script, ScriptAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.site_title = 'Сайт администратора LisovenkovaAds'
admin.site.site_header = 'LisovenkovaAds'