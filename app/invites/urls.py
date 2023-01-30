from django.urls import path

from . import views

app_name = 'invites'

urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='index'
    ),
    path(
        'confirm/<uuid>/',
        views.ConfirmInvitationView.as_view(),
        name='confirm'
    ),
    path(
        'decline/<uuid>/',
        views.DeclineInvitation.as_view(),
        name='decline'
    ),
]
