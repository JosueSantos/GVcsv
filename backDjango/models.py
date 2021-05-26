from django.db import models

class VulnerabilityItem(models.Model):

    class Meta:
        db_table = 'vulnerability_item'
        verbose_name = 'vulnerability_item'
        verbose_name_plural = 'vulnerability_itens'
    
    asset_hostmane = models.CharField(max_length=200)
    asset_ip_address = models.CharField(max_length=200)
    vulnerability_title = models.CharField(max_length=300)
    vulnerability_severity = models.CharField(max_length=50)
    vulnerability_cvss = models.CharField(max_length=200)
    vulnerability_publication_date = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asset_hostmane