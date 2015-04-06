from __future__ import print_function

from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from paypal.standard.forms import PayPalPaymentsForm

@csrf_exempt
def home (request):
  http_prefix = "{}://{}".format(request.scheme, request.get_host())
  
  paypal_dict = {
    "business": settings.PAYPAL_RECEIVER_EMAIL,
    "amount": "25.00",
    "item_name": "Phat Donation",
    "invoice": "phat-donation-unique-id",
    "custom": 'phat-donation',
    "notify_url": http_prefix + reverse('paypal-ipn'),
    "return_url": http_prefix + "/",
    "cancel_return": http_prefix + "/",
  }
  
  form = PayPalPaymentsForm(initial=paypal_dict)
  return TemplateResponse(request, 'index.html', {"form": form})
  
### Probably better to put this in models.py 
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def show_me_the_money (sender, **kwargs):
  ipn_obj = sender
  print(ipn_obj.payment_status)
  print(ipn_obj.custom)
  
  if ipn_obj.payment_status == ST_PP_COMPLETED:
    if ipn_obj.custom == "phat-donation":
      print("PHAT DONATION")
      
valid_ipn_received.connect(show_me_the_money)
