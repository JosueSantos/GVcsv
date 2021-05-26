from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from backDjango.functions.model_access import deleteFixedVulnerability, getAllVulnerabilities, getOnlyHostname
from backDjango.functions.populate_vulnerabilities import populate_vulnerabilities_from_csv


@login_required()
def index(request):
    vulnerabilitiesHost = getOnlyHostname()
    vulnerabilities = getAllVulnerabilities()

    if request.method == 'POST' and "newVulnerabilities" in request.FILES:
        newVulnerabilities = request.FILES['newVulnerabilities']

        if (newVulnerabilities.name.endswith('.csv')):
            populate_vulnerabilities_from_csv(newVulnerabilities)
            message = "Lista de vulnerabilidades Criada"
        else:
            message = "Arquivo deve possuir a extensão .csv"
        
        return render(request, 'frontend/index.html', {
            'message': message,
            'vulnerabilities': vulnerabilities,
            'vulnerabilitiesHost': vulnerabilitiesHost,
        })

    if request.method == 'POST' and "id" in request.POST:
        vulnerabilities = deleteFixedVulnerability(request.POST['id'])
        
        return render(request, 'frontend/index.html', {
            'message': "Vulnerabilidade Corrigida",
            'vulnerabilities': vulnerabilities,
            'vulnerabilitiesHost': vulnerabilitiesHost,
        })

    return render(request, 'frontend/index.html', {
        'vulnerabilities': vulnerabilities,
        'vulnerabilitiesHost': vulnerabilitiesHost,
    })
