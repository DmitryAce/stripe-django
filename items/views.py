import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item, Order
from django.views.decorators.http import require_GET

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def get_stripe_keys(currency):
    if currency == 'eur':
        return settings.STRIPE_PUBLISHABLE_KEY_EUR, settings.STRIPE_SECRET_KEY_EUR
    else:
        return settings.STRIPE_PUBLISHABLE_KEY, settings.STRIPE_SECRET_KEY
    
@require_GET
def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    publishable_key, _ = get_stripe_keys(item.currency)
    
    context = {
        'item': item,
        'STRIPE_PUBLISHABLE_KEY': publishable_key
    }
    return render(request, 'item_detail.html', context)

@require_GET
@csrf_exempt
def create_checkout_session(request, id):
    item = get_object_or_404(Item, id=id)
    publishable_key, secret_key = get_stripe_keys(item.currency)
    stripe.api_key = secret_key
    
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(f'/item/{id}/'),
        )
        return JsonResponse({'id': session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def create_payment_intent(request, id):
    item = get_object_or_404(Item, id=id)
    
    if item.currency == 'eur':
        stripe.api_key = settings.STRIPE_SECRET_KEY_EUR
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY_USD
    
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(item.price * 100),
            currency=item.currency,
            payment_method_types=['card'],
        )
        return JsonResponse({'client_secret': intent.client_secret})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def payment_success(request):
    return render(request, 'payment_success.html')