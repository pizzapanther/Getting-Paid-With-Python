#!/usr/bin/env python

from __future__ import print_function

from flask import Flask, render_template, request

import stripe

app = Flask(__name__)

STRIPE_PUB_KEY = 'pk_X0XK07me4sK6TBufGmsCqpMvlMhvg'
STRIPE_SECRET = 'Aa8S9o85plzCEMnzk3oSahxqJpUwe9W0'

stripe.api_key = STRIPE_SECRET

@app.route("/", methods=['GET', 'POST'])
def main_view ():
  if request.method == 'POST':
    print("POST Data")
    for key, value in request.form.items():
      print("{}: {}".format(key, value))
      
    token = request.form['stripeToken']
    response = stripe.Charge.create(
      amount=2500,
      currency="usd",
      source=token,
      description="Phat Donation"
    )
    print("Stripe Response")
    print(response)
    
    return render_template('thanks.html')
    
  return render_template('index.html', public_key=STRIPE_PUB_KEY)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
  