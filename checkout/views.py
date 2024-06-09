from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PPjD4LuLUxWdLnagq6xIbmiZuwZv1L54dqNNFoUBXqLiTn01uR6StXkTF85OiaMXvVb6LyOAAPGM91roJHS05lI00zz4pp44w'
    }

    return render(request, template, context)