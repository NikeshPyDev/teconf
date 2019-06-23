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
        data['proposals'] = Proposals.objects.filter(proposal_type=proposal_type)
        return render(request, 'proposal_list.html', {'data': data})


class ProposalView(TemplateView):
    form_class = ProposalForm

    def get(self, request, **kwargs):
        proposal_id = kwargs.get('proposal_id', None)
        proposal_type = kwargs.get('proposal_type', None)
        bread_crumbs = []
        if proposal_type:
            bread_crumbs.append({'url': '/' + proposal_type,'label': dict(PROPOSAL_TYPES)[proposal_type]})
        if proposal_id is not None:
            proposal = Proposals.objects.get(id=proposal_id)
            bread_crumbs.append({'url': proposal.id, 'label': proposal.title})
            proposal_form = self.form_class(prefix='proposal',instance=proposal)
        else:
            bread_crumbs.append({'url': 'new_proposal', 'label': 'New'})
            proposal_form = self.form_class(prefix='proposal')            
        return render(request, 'proposal_create.html', {'form': proposal_form, 'bread_crumbs': bread_crumbs})


    def post(self, request, *args, **kwargs):
        proposal_form = self.form_class(request.POST)
        proposal = proposal_form.save()
        proposal.save()
        bread_crumbs = [{'url': proposal.proposal_type, 'label': dict(PROPOSAL_TYPES)[proposal.proposal_type]},
                        {'url':proposal.id, 'label': proposal.title}]
        data = {
            'proposal_type': proposal.proposal_type,
            'proposals': Proposals.objects.all(),
        }
        return render(request, 'proposal_list.html', {'data': data, 'bread_crumbs': bread_crumbs})

