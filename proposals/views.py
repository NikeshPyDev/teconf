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
        data['proposals'] = Proposals.objects.all()
        return render(request, 'proposal_list.html', {'data': data})


class ProposalView(TemplateView):
    form_class = ProposalForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'proposal_create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        proposal_form = self.form_class(request.POST)
        proposal = proposal_form.save()
        proposal.save()
        data = {
            'proposal_type': proposal.proposal_type,
            'proposals': Proposals.objects.all()
        }
        return render(request, 'proposal_list.html', {'data': data})

