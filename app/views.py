"""Be Balance /root view controller"""

from django.shortcuts import HttpResponse, render
from app.models import Agenda
import app.openada as ada


def index(req):
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

    agendas = Agenda.objects.all()
    context = {
        "img_list": finallist,
        "agenda_object": agendas
    }
    return render(req, 'app/index.html', context)


def register(req):
    """ registration function """
    keys = ['name', 'email', 'phone', 'address', 'recommender', 'reason']
    result = ""
    for key in keys:
        if key in req.POST:
            result += req.POST[key]+" "
            print(result)
        else:
            continue
    return HttpResponse(result)
