from django.urls import path
from .views import *

urlpatterns = [
    path('', list_proposal_types, name='proposal_types'),
    path('<str:proposal_type>/new', ProposalEditView.as_view(), name='new_proposal'),
    path('<str:proposal_type>/edit/<int:proposal_id>', ProposalEditView.as_view(), name='edit_proposal'),
    path('<str:proposal_type>/<int:proposal_id>', ProposalView.as_view(), name='view_proposal'),
    path('<str:proposal_type>/<int:proposal_id>/comment/new', post_comments, name='post_comment'),
    path('<str:proposal_type>', ProposalListView.as_view(), name='proposal_type'),
]
