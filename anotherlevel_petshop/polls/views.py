from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate

def index(request):
    candidates = Candidate.objects.all()
    output = ''
    for candidate in candidates:
        output += "<p>{} 기호{}번({})<br>".format(candidate.name,
            candidate.party_number, candidate.area)
        output += candidate.introduction+"</p>"

    return HttpResponse(output)
