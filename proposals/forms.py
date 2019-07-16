from django import forms
from .models import Proposals
# from markedit.widgets import MarkEdit


class ProposalForm(forms.ModelForm):

    class Meta:
        model = Proposals

        fields = [
            "id",
            "title",
            "description",
            "audience",
            "status",
            "proposal_type",
            "proposal_section",
            "pre_requisites",
            "current_urls",
            "speaker_info",
            "speaker_links",
        ]

        # widgets = {
        #     "description": MarkEdit()
        # }

