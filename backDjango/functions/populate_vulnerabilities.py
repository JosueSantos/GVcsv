from ..models import VulnerabilityItem
import pandas as pd

def populate_vulnerabilities_from_csv(fileCsv):
    """Populate vulnerabilities"""

    data = pd.read_csv(fileCsv, error_bad_lines=False)

    vulnerabilities = []
    batch_number = 0
    batch_size = 100

    for _, row in data.iterrows():
        batch_number = 1 + batch_number

        vulnerability = VulnerabilityItem(
            asset_hostname = row['ASSET - HOSTNAME'],
            asset_ip_address = row['ASSET - IP_ADDRESS'],
            vulnerability_title = row['VULNERABILITY - TITLE'],
            vulnerability_severity = row['VULNERABILITY - SEVERITY'],
            vulnerability_cvss = row['VULNERABILITY - CVSS'],
            vulnerability_publication_date = row['VULNERABILITY - PUBLICATION_DATE']
        )
        vulnerabilities.append(vulnerability)

        if (batch_number > batch_size):
            VulnerabilityItem.objects.bulk_create(vulnerabilities)
            batch_number = 0
            vulnerabilities = []

    VulnerabilityItem.objects.bulk_create(vulnerabilities)