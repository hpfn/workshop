# import hashlib

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import resolve_url as r
from mailchimp3 import MailChimp

from workshop.core.forms import SubscriptionForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'core/index.html', context)


def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'core/index.html', {'form': form})

    export_to_mailchimp(form.cleaned_data['email'])

    return HttpResponseRedirect(r('core:success'))


def export_to_mailchimp(email):
    u_login =
    k_api =
    m_l_id =

    databody_item = {
        'email_address': email,
        'status': 'subscribed',
    }

    client = MailChimp(mc_user=u_login, mc_api=k_api)
    client.lists.members.create(m_l_id, databody_item)
    # does not update tags
    # email = email.lower().encode(encoding='utf-8')
    # hash = hashlib.md5(email).hexdigest()
    # client.lists.members.update(m_l_id, subscriber_hash=hash, data=databody_item)
    # client.lists.segments.update(m_l_id, segment_id=2097, data=databody_item)


def success(request):
    return render(request, 'core/success.html', {})

# GET all members
# client = MailChimp(mc_user=u_login, mc_api=k_api)
# dict_members = client.lists.members.all(m_l_id, get_all=True, fields="members.id,members.email_address,members.timestamp_opt")
# del dict_members['total_items']
