# django-payments-cod

Cash on Delivery (COD) Provider for [django_payments](https://django-payments.readthedocs.org/)


Installation
========================

```
pip install django-payments-cod
```

OR

```
pip install https://github.com/xtranophilist/django-payments-cod/archive/master.zip
```


Usage
==============

In your Django project settings:

```
INSTALLED_APPS = [
    ...
    'django_payments_cod',
    ]
```


```
PAYMENT_VARIANTS = {
    'default': ('django_payments_cod.CODProvider', {})}
```


```
CHECKOUT_PAYMENT_CHOICES = [
    ('default', 'Cash On Delivery')
]
```
