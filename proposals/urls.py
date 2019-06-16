from django.urls import path
from .views import *

urlpatterns = [
    path('', list_proposal_types, name='proposal_types'),
    path('new', ProposalView.as_view(), name='new_proposal'),
    path('<str:proposal_type>', ProposalListView.as_view(), name='proposal_type'),
]
