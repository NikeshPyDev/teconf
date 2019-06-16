from django.db import models
from tinymce.models import HTMLField
# from conference import Conference

# Create your models here.

PROPOSAL_TYPES = [
    ('talk', 'Talk'),
    ('workshop', 'Workshop')
]


class Proposals(models.Model):

    title = models.CharField(max_length=250)
    description = HTMLField()
    audience = models.CharField(max_length=1500)
    status = models.CharField(max_length=50)
    proposal_type = models.CharField(choices=PROPOSAL_TYPES, max_length=25)
    proposal_section = models.CharField(max_length=1500)
    pre_requisites = HTMLField()
    current_urls = HTMLField()
    speaker_info = HTMLField()
    speaker_links = HTMLField()
