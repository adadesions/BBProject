"""Be Balance /root view controller"""

from django.shortcuts import HttpResponse, render
import app.openada as ada
from itertools import chain

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
    context = {"img_list": finallist}
    return render(req, 'app/index.html', context)

def detail(req):
    """detail view as /view """
    return HttpResponse("Hey! Ada")
