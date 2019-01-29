import hashlib
from django.contrib import messages
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

    # esboço copiado e colado
    if export_to_mailchimp(form.cleaned_data['email']) == 'Already':
        messages.error(request, "E-mail cadastrado anteriormente!")
        return HttpResponseRedirect('/')

    return HttpResponseRedirect(r('core:success'))


def export_to_mailchimp(email):
    u_login = ''
    k_api = ''
    m_l_id = ''

    databody_item = {
        'email_address': email,
        'status': 'subscribed',
    }

    client = MailChimp(mc_user=u_login, mc_api=k_api)
    try:
        client.lists.members.create(m_l_id, databody_item)
    except:  # MailChimpError: # esboço
        return "Already"



    # does update tags now
    # 'update_members', not just 'update'
    # client.lists.segments.update_members(m_l_id, segment_id=2097, data={'name': 'par', 'members_to_remove': [email]})


def success(request):
    return render(request, 'core/success.html', {})

# GET all members
# client = MailChimp(mc_user=u_login, mc_api=k_api)
# dict_members = client.lists.members.all(m_l_id, get_all=True, fields="members.id,members.email_address,members.timestamp_opt")
# del dict_members['total_items']
