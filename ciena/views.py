import json

from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse
import random

from ciena.models import Tickets, History

@login_required(login_url='/login/')
def dashboard(request):
    context = {
        'next': "whats next"
    }
    context.update(request)
    template = get_template("home.html")
    html = template.render(context, request)
    return HttpResponse(html)


def query2engine(request):
    try:
        query_str = request.GET.get('query', 'testing shiv ABC')
        output = requests.get(
                            'http://172.20.10.2:8080/query2engine',
                            params=dict(query=query_str)
                        ).content
        output = json.loads(output)
    except:
        output = {"response": [{"confidence": 0.34, "query": "testing shiv ABC", "closest_query": "Solution Description: Pending response from Jade.", "response": "MN:OME6500: Release 11.2: ODU Signal Degrade Alarm on LARDTXEC-01o - OTM 4-12-6"}, {"confidence": 0.3, "query": "testing shiv ABC", "closest_query": "Solution Description: Customer resolves this issue in other case.", "response": "MN: OME6500 :Rel 12.0 :Warm Restart of 10G Cards via DEBUG"}, {"confidence": 0.28, "query": "testing shiv ABC", "closest_query": "MN: OME 6500: REL11.2: Issue Missing Optics alarm", "response": "Solution Description: 1. FIRSTLIGHT FIBER reported that Issue Missing Optics alarm 2. Checked and found that circuit pack that is raising the alarm are on slot 9 and Slot 11. Both are eMOTR\\u00a0circuit packs. 3. Vincent told that they are still waiting on approval from change management and there is no time-frame\\u00a0for that ,so close the case. 4. If any anomaly happens after the given action plan is performed in maintenance window, he will get back accordingly with new case. Action Plan: 1. Perform a cold restart on the circuit pack on slot 9 and slot 11.\\u00a0 2. If the alarm still persists after 10 minutes then replace the pluggable module with a tested pluggable\\u00a0XFP\'s.\\u00a0 3. If the alarm still persists after step-2, we need to perform Cold reboot on SP-2 card on slot 15."}]}
    try:
        if request.GET['query']:
            history = History()
            history.problem = request.GET['query']
            history.solution = ""
            history.confidence = random.randint(20, 100)
            history.save()
    except:
        pass
    return JsonResponse(output)


def update(request):
    """save new ticket and solution for re-training and modeling"""
    try:
        if request.method == 'POST':
            ticket = Tickets()
            ticket.problem = request.POST['query']
            ticket.solution = request.POST['solution']
            ticket.save()
            response = {"response": "Solution updated.", "status": "success"}
    except:
        response = {"response": "", "status": "error"}

    return JsonResponse(response)

@login_required(login_url='/login/')
def history(request):
    history_list = History.objects.all().order_by('-date')[:10]
    tickets_list = Tickets.objects.all().order_by('-date')[:10]
    context = {
        'next': "whats next",
        'searches': history_list,
        'tickets': tickets_list
    }
    context.update(request)
    template = get_template("history.html")
    html = template.render(context, request)
    return HttpResponse(html)
