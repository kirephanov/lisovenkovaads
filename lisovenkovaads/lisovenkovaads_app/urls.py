from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('form/', ads_form_page, name='form'),
    path('ads/<int:pk>/', GetAds.as_view(), name='ads'),
    path('get_script/', ScriptFormPage.as_view(), name='script_form'),
    path('get_script/script/', script_page, name='script'),
]