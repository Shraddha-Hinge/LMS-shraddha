from django.urls import path
from .views import SubscriptionPlanListView, ProcessPaymentView
from .webhooks import stripe_webhook

urlpatterns = [
    path("plans/", SubscriptionPlanListView.as_view(), name="list-plans"),
    path("pay/", ProcessPaymentView.as_view(), name="process-payment"),
    path("webhooks/stripe/", stripe_webhook, name="stripe-webhook"),
]
