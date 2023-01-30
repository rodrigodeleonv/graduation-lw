from django.utils import timezone

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.db.models import F

from .models import Invite


class IndexView(View):
    def get(self, request: HttpRequest):
        return HttpResponse('Invite')


class ConfirmInvitationView(View):
    def get(self, request: HttpRequest, uuid: str):
        invite = Invite.objects.get(id=uuid)
        invite.total_requests = F('total_requests') + 1
        invite.save(update_fields=['total_requests'])
        context = {'invite': invite, 'invite_id': uuid}
        return render(request, 'invites/confirm.html',
                      context)

    def post(self, request: HttpRequest, uuid: str):
        total_confirmed = int(
            request.POST.get('total_confirmed')
        )
        invite = Invite.objects.get(id=uuid)
        invite.total_confirmed = total_confirmed
        invite.confirmed = True
        invite.confirm_date = timezone.now()
        invite.save(force_update=True)
        return HttpResponse('Actualizado')


class DeclineInvitation(View):
    def get(self, request: HttpRequest, uuid: str):
        invite = Invite.objects.get(id=uuid)
        invite.confirmed = False
        invite.confirm_date = timezone.now()
        invite.save(force_update=True)
        return HttpResponse('No asistiré')


class ConfirmCompletedView(View):
    pass