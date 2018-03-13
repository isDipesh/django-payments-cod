document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('#payment-form button').innerHTML = 'Processing...';
  document.getElementById('payment-form').submit();
}, false);
