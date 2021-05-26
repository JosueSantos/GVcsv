from ..models import VulnerabilityItem
from django.db.models import Avg

def getAllVulnerabilities():
    return VulnerabilityItem.objects.all()

def deleteFixedVulnerability(id):
    VulnerabilityItem.objects.get(id=id).delete()
    return VulnerabilityItem.objects.all()

def getOnlyHostname():
    return VulnerabilityItem.objects.values('asset_hostmane').annotate(avg_cvss=Avg('vulnerability_cvss')).order_by('-avg_cvss')