from payments.forms import PaymentForm


class CODForm(PaymentForm):
    cod = True

    class Media:
        js = ('js/cod.js',)
