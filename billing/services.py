import stripe
from .models import Payment

stripe.api_key = "your_stripe_secret_key"

def process_payment(user, plan, payment_method):
    if payment_method == "stripe":
        intent = stripe.PaymentIntent.create(
            amount=int(plan.price * 100),
            currency="usd",
            metadata={"user_id": user.id, "plan_id": plan.id}
        )
        transaction_id = intent.id
    else:
        transaction_id = "offline_manual"

    payment = Payment.objects.create(
        user=user,
        amount=plan.price,
        payment_method=payment_method,
        transaction_id=transaction_id,
        status="pending" if payment_method == "stripe" else "completed"
    )

    return payment
