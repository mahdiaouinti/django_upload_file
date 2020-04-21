from django.conf.urls.static import static
from django.urls import path

from test_django import settings
from . import views

urlpatterns = [
path('formulaire', views.create_candidat, name='formulaire'),
path(r'profile/<int:candidat_id>/<int:etat>', views.profile),
path('login', views.user_login, name='login'),
path('listcondidats', views.list_condidats, name='listcondidats'),
path('update/<int:candidat_id>', views.update_candidat),
path('profile/<int:candidat_id>/profile/<int:etat>', views.update_etat),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)