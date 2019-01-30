import hashlib
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import resolve_url as r
from mailchimp3 import MailChimp

from decouple import config


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

    # esboço copiado e colado
    if not export_to_mailchimp(form.cleaned_data['email']):  # == 'Already':
        messages.error(request, "E-mail cadastrado anteriormente!")
        return render(request, 'core/index.html', {'form': form})

    return HttpResponseRedirect(r('core:success'))


def export_to_mailchimp(email):
    u_login = config('MAILCHIMP_USER_LOGIN')
    k_api = config('MAILCHIMP_API_KEY')
    m_l_id = config('MAILCHIMP_L_ID')

    databody_item = {
        'email_address': email,
        'status': 'subscribed',
    }

    client = MailChimp(mc_user=u_login, mc_api=k_api)
    try:
        client.lists.members.create(m_l_id, databody_item)
        return True
    except:  # MailChimpError: # esboço
        return False  # "Already"

def success(request):
    return render(request, 'core/success.html', {})


# GET all members
# client = MailChimp(mc_user=u_login, mc_api=k_api)
# dict_members = client.lists.members.all(m_l_id, get_all=True, fields="members.id,members.email_address,members.timestamp_opt")
# del dict_members['total_items']

# GET segments id and name
# client = MailChimp(mc_user=u_login, mc_api=k_api)
# dict_segments = client.lists.segments.all(m_l_id, get_all=False, fields="segments.id,segments.name")
# for i in dict_segments['segments']:
#    print(i)

# does update tags now
# 'update_members', not just 'update'
# client.lists.segments.update_members(m_l_id, segment_id=2097, data={'name': 'par', 'members_to_remove': [email]})
