from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
from django.contrib.auth.models import User
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
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    post = models.ForeignKey(Proposals, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = HTMLField()
    created_date = models.DateTimeField(default=datetime.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
