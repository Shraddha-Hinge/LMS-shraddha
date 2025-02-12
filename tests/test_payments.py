from rest_framework.test import APITestCase
from rest_framework import status
from billing.models import Payment, SubscriptionPlan, UserSubscription
from accounts.models import User

class PaymentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="TestPass123")
        self.plan = SubscriptionPlan.objects.create(name="Monthly Plan", price=50, duration="monthly")
        self.client.force_authenticate(user=self.user)
        self.plan = SubscriptionPlan.objects.create(name="Monthly Plan", price=50, duration="monthly")

    def test_process_payment(self):
        response = self.client.post("/api/billing/pay/", {"plan_id": self.plan.id, "payment_method": "stripe"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_activation(self):
        end_date = timezone.now() + timedelta(days=30)
        subscription = UserSubscription.objects.create(user=self.user, plan=self.plan, is_active=True, end_date=end_date)
        self.assertTrue(subscription.is_active)
