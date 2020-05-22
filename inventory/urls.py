from django.urls import path
from . import views

urlpatterns = [
    path('', views.type_list, name='type_list'),
    path('types/<type_id>/', views.type_detail, name='type_detail'),
    path('industry/', views.industry_indices, name='industry'),
]
