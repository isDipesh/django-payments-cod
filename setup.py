from setuptools import setup

setup(name='django-payments-cod',
      version='0.1.3',
      description='Cash on Delivery Provider for django-payments',
      url='http://github.com/xtranophilist/django-payments-cod',
      author='Dipesh Acharya',
      author_email='dipesh@awecode.com',
      maintainer='Awecode',
      license='BSD License',
      packages=['django_payments_cod'],
      long_description=open('README.md').read(),
      include_package_data=True,
      zip_safe=False,
      keywords='django,payments,ecommerce,saleor,delivery',
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      )
