from django.urls import path
from .views import (
    ConferenceDetails,
    ConferenceCreate,
    ConferenceUpdate,
    ConferenceDelete,
    ConferenceList,
    SubmissionList,
    SubmissionDetailView,
    SubmissionCreate,
    SubmissionUpdate
)

urlpatterns = [
    # Conférences
    path("liste/", ConferenceList.as_view(), name="liste_conferences"),
    path("ajouter/", ConferenceCreate.as_view(), name="conference_create"),
    path("<int:pk>/", ConferenceDetails.as_view(), name="conference_details"),
    path("<int:pk>/modifier/", ConferenceUpdate.as_view(), name="conference_update"),
    path("<int:pk>/supprimer/", ConferenceDelete.as_view(), name="conference_delete"),

    # Soumissions
    path("submissions/liste/", SubmissionList.as_view(), name="submission_list"),
    path("submissions/ajouter/", SubmissionCreate.as_view(), name="submission_create"),
    path("submissions/<str:pk>/details/", SubmissionDetailView.as_view(), name="submission_details"),
    path("submissions/<str:pk>/modifier/", SubmissionUpdate.as_view(), name="submission_update"),
]
