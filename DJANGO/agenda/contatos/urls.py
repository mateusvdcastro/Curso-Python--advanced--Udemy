from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
]
