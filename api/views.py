from django.shortcuts import render
from api import safebrowsing
from django.conf import settings


def home(request):
    context = {}
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        vendor = request.POST.get('vendor', '')
        url = request.POST.get('url', '')
        if vendor == "google":
            api_key = settings.GOOGLE_API_KEY
            sb = safebrowsing.LookupAPI(api_key)
            resp = sb.threat_matches_find(url)

            if resp:
                if resp.get('matches', ''):
                    context['result'] = 'unsafe'
                if resp.get('error', ''):
                    context['result'] = 'error'

                context['details'] = resp
            else:
                context['result'] = 'safe'
                context['details'] = 'Try a different URL'
        if vendor == "norton":
            context['result'] = 'Work in Progress'

    return render(request, 'home.html', context)
