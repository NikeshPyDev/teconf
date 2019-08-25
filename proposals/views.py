from django.shortcuts import render, redirect
from .forms import *
from .models import PROPOSAL_TYPES, Proposals, Comment
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


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

    def get(self, request, *args, **kwargs):
        proposal_id = kwargs.get('proposal_id', None)
        proposal_type = kwargs.get('proposal_type', None)
        bread_crumbs = []
        comments = []
        editable = False
        if proposal_type:
            bread_crumbs.append({'url': '/' + proposal_type, 'label': dict(PROPOSAL_TYPES)[proposal_type]})
        if proposal_id is not None:
            proposal = Proposals.objects.get(id=proposal_id)
            comments = Comment.objects.filter(proposal=proposal_id)
            bread_crumbs.append({'url': proposal.id, 'label': proposal.title})
            editable = True if (proposal.author_id == request.user) else False
            # proposal_form = self.form_class(instance=proposal)
        else:
            bread_crumbs.append({'url': 'new_proposal', 'label': 'New'})
        return render(request, 'proposal_view.html', {'proposal': proposal, 'bread_crumbs': bread_crumbs, 'editable': editable, 'comments': comments})


class ProposalEditView(TemplateView):
    form_class = ProposalForm
    redirect_field_name = "/proposals/"

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        proposal_id = kwargs.get('proposal_id', None)
        proposal_type = kwargs.get('proposal_type', None)
        bread_crumbs = []
        if proposal_type:
            bread_crumbs.append({'url': '/' + proposal_type,'label': dict(PROPOSAL_TYPES)[proposal_type]})
        if proposal_id is not None:
            proposal = Proposals.objects.get(id=proposal_id)
            bread_crumbs.append({'url': proposal.id, 'label': proposal.title})
            proposal_form = self.form_class(instance=proposal)
        else:
            bread_crumbs.append({'url': 'new_proposal', 'label': 'New'})
            proposal_form = self.form_class()
        return render(request, 'proposal_create.html', {'form': proposal_form, 'bread_crumbs': bread_crumbs})

    def post(self, request, *args, **kwargs):
        proposal_form = self.form_class(request.POST)

        data = {'proposal_type': 'talk',
                'proposals': Proposals.objects.all()}
        bread_crumbs = []
        if proposal_form.is_valid():
            if request.POST.get('proposal_id', None) and (request.POST.get('proposal_id') != 'None'):
                proposal = Proposals.objects.get(id=request.POST.get('proposal_id'))
                self.form_class(request.POST, instance=proposal).save(commit=False)
                proposal.updated_date = datetime.now()
            else:
                proposal = proposal_form.save(commit=False)
                proposal.author_id = request.user
            proposal.save()
            bread_crumbs = [{'url': proposal.proposal_type, 'label': dict(PROPOSAL_TYPES)[proposal.proposal_type]},
                            {'url': proposal.id, 'label': proposal.title}]
            data = {
                'proposal_type': proposal.proposal_type,
                'proposals': Proposals.objects.all(),
            }
        return render(request, 'proposal_list.html', {'data': data, 'bread_crumbs': bread_crumbs})


def post_comments(request, proposal_type, proposal_id):
    proposal = Proposals.objects.get(id=proposal_id)
    text = request.POST.get('text')
    comment = Comment(proposal=proposal, author=request.user, text=text)
    comment.save()
    proposal.comments_count += 1
    proposal.save()
    return redirect('/proposals/'+proposal_type + '/' + str(proposal_id))



