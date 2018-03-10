"""Be Balance /root view controller"""

from django.shortcuts import HttpResponse, render, redirect
from django.utils import timezone
from app.models import Agenda, Applicant
import app.openada as ada


def index(request):
    """index view as / """
    list_files = [
        "placeslist.txt",
        "treatmentlist.txt",
        "foodslist.txt",
        "roomslist.txt",
        "facilitylist.txt"
        ]
    list_data = {}
    for txt in list_files:
        list_data.update(ada.readimgfromlist(txt))
    finallist = list_data.items()
    if 'registed' in request.session:
        pass
    else:
        request.session['registed'] = False
    agendas = Agenda.objects.all()
    context = {
        "img_list": finallist,
        "agenda_object": agendas,
        "registed": request.session['registed']
    }
    return render(request, 'app/index.html', context)


def register(request):
    """ registration function """
    keys = ['name', 'email', 'phone', 'recommender', 'reason']
    data = request.POST
    new_applicant = Applicant(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        recommender=data['recommender'],
        reason=data['reason'],
        date=timezone.now(),
        time=timezone.now()
        )
    new_applicant.save()

    request.session['registed'] = True
    return redirect('/#contact')
    # return HttpResponse(new_applicant)


def more_register(request):
    """ Reset registed session """
    request.session['registed'] = False
    return redirect('/#contact')


def marathon_ex(request):
    return render(request, 'app/marathon.html')
