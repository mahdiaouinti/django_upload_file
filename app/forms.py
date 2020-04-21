from django.forms import ModelForm

from .models import *
# creating a form
class FormFormulaire(ModelForm):
    class Meta:

       model = candidat
       fields = ['nom', 'prenom', 'Email', 'Date_de_naissance',
                 'num_tel', 'Disponibilite', 'Nb_années_expérience','cv','message']