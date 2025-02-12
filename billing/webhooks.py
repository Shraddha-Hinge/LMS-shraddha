from django.http import JsonResponse
import stripe
from .models import Payment

stripe.api_key = "your_stripe_secret_key"

def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(payload, stripe.api_key)
    except ValueError:
        return JsonResponse({"error": "Invalid payload"}, status=400)

    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        transaction_id = intent["id"]

        payment = Payment.objects.filter(transaction_id=transaction_id).first()
        if payment:
            payment.status = "completed"
            payment.save()

    return JsonResponse({"status": "success"}, status=200)
