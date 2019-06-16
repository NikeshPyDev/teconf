from django.shortcuts import render
from .forms import *
from .models import PROPOSAL_TYPES, Proposals
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


def generate_prposal_type_url(p_type):
    return '{}'.format(p_type)


def list_proposal_types(request):
    proposal_types = []
    for p_type in PROPOSAL_TYPES:
        proposal_types.append({
            'p_type': p_type[0],
            'p_type_url': generate_prposal_type_url(p_type[0])
        })
    return render(request, 'proposal_type.html', {'proposal_types': proposal_types})


class ProposalListView(FormView):

    def get(self, request, proposal_type=None):
        data = {
            'proposal_type': proposal_type,
            'proposals': []
        }
        if proposal_type:
            data['proposals'] = Proposals.objects.filter(proposal_type=proposal_type)
        return render(request, 'proposal_list.html', {'data': data})


class ProposalView(TemplateView):
    form_class = ProposalForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'proposal_create.html', {'form': form})

