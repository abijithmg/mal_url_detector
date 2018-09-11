from django.shortcuts import render
from api import safebrowsing
from django.conf import settings


def home(request):
    context = {}
    api_key = settings.GOOGLE_API_KEY
    sb = safebrowsing.LookupAPI(api_key)
    resp = sb.threat_matches_find('')
    if resp:
        matches = resp.get('matches', '')
        if matches:
            context['result'] = 'Threat Found'
        error = resp.get('error', '')
        if error:
            context['result'] = 'ERROR'

        context['details'] = resp
    else:
        context['result'] = 'Threat Not Found'
        context['details'] = 'Try a different URL'

    return render(request, 'home.html', context)
