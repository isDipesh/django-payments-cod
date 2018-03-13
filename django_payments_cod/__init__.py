from django.http import HttpResponseRedirect
from payments.core import BasicProvider
from payments.forms import PaymentForm


class CODProvider(BasicProvider):
    """
    Cash on Delivery Provider for django_payments
    """

    def get_form(self, payment, data=None):
        return PaymentForm({}, self.get_return_url(payment), self._method, autosubmit=True)

    def process_data(self, payment, request):
        return HttpResponseRedirect(payment.get_success_url())
