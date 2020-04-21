import smtplib

from django.contrib import messages
from django.core import mail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

connection = mail.get_connection()


from test_django import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from app.forms import FormFormulaire
from .models import candidat
from django.core.paginator import Paginator

def list_condidats(request):
    candidats = candidat.objects.get_queryset().order_by('id')

    paginator = Paginator(candidats, 5)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'liste_condidats.html',{'page_obj': page_obj})
def profile(request,candidat_id,etat):

    candidat_id = int(candidat_id)
    candidat_sel = candidat.objects.get(id=candidat_id)
    etat2 = candidat_sel.etat
    if etat == 1 :
        etat1= "En cour"
    elif etat == 2 :
        etat1 = "Confirmer"
    elif etat == 3:
        etat1="Rejeter"
    else:
        etat1=etat2
    candidat_sel.etat = etat1
    candidat_sel.save()
    return render(request,'profile.html', {'condidats': candidat_sel})



FILE_TYPES = ['pdf']
def update_candidat(request, candidat_id):
    candidat_id = int(candidat_id)
    try:
        candidat_sel = candidat.objects.get(id = candidat_id)
    except candidat.DoesNotExist:
        return redirect('listcondidats')
    candidat_form = FormFormulaire(request.POST or None, instance = candidat_sel)
    if candidat_form.is_valid():
       candidat_form.save()
       return redirect('listcondidats')
    context = {"form": candidat_form }
    return render(request, 'formulaire.html', context)



def create_candidat(request):
    form = FormFormulaire()
    if request.method == 'POST':
        form = FormFormulaire(request.POST, request.FILES)
        if form.is_valid():
            candidat_pr = form.save(commit=False)
            file = request.FILES['cv']
            file_type = candidat_pr.cv.url.split('.')[-1]
            file_type = file_type.lower()
            email1 = form.cleaned_data.get("Email")
            subject = "candidature a été sauvegardé avec succès"
            msg = "votre candidature a été sauvegardé avec succès Merci pour la validation de Votre candidature"
            if file_type not in FILE_TYPES:
                messages.success(request, 'File doit être de Format PDF')
            else:
                res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [email1], fail_silently=False)
                if (res == 1):
                    msg = "Valide"
                else:
                    msg = "Non valide"
                candidat_pr.status_email = msg

                candidat_pr.save()



    context = {"form": form,}

    return render(request, 'formulaire.html', context)
def update_etat(request, candidat_id,etat):
    candidat_id = int(candidat_id)

    candidat_sel = candidat.objects.get(id=candidat_id)
    if etat==1 :
        etat1= "En cour"


    elif etat ==2 :
        etat1 = "Confirmer"
    else:
        etat1="Rejeter"



    candidat_sel.etat = etat1
    candidat_sel.save()


    return render(request, 'profile.html', {'condidats': candidat_sel})


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('listcondidats'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)
def update_etat(request,candidat_id,etat):

    candidat_id = int(candidat_id)
    candidat_sel = candidat.objects.get(id=candidat_id)
    if etat == 1 :
        etat1= "En cour"
    elif etat == 2 :
        etat1 = "Confirmer"
    elif etat == 3:
        etat1="Rejeter"
    else:
        etat1="Nouvelle"
    candidat_sel.etat = etat1
    candidat_sel.save()
    return render(request,'profile.html', {'condidats': candidat_sel})

