from django.http import HttpResponseRedirect
from payments.core import BasicProvider

from django_payments_cod.forms import CODForm


class CODProvider(BasicProvider):
    """
    Cash on Delivery Provider for django_payments
    """

    def get_form(self, payment, data=None):
        return CODForm({}, self.get_return_url(payment), self._method, autosubmit=True)

    def process_data(self, payment, request):
        # FIXME Change payment status?
        return HttpResponseRedirect(payment.get_success_url())
