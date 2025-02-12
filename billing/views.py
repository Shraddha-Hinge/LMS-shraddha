from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment, SubscriptionPlan, UserSubscription
from .serializers import PaymentSerializer, SubscriptionPlanSerializer, UserSubscriptionSerializer
from .services import process_payment
from accounts.permissions import IsStudent, IsAdmin

# List Subscription Plans
class SubscriptionPlanListView(generics.ListAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAuthenticated]

# Process Payment (Stripe/Razorpay)
class ProcessPaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def create(self, request, *args, **kwargs):
        user = request.user
        plan_id = request.data.get("plan_id")
        payment_method = request.data.get("payment_method")

        try:
            plan = SubscriptionPlan.objects.get(id=plan_id)
            payment = process_payment(user, plan, payment_method)
            return Response({"message": "Payment initiated", "transaction_id": payment.transaction_id}, status=status.HTTP_201_CREATED)
        except SubscriptionPlan.DoesNotExist:
            return Response({"error": "Plan not found"}, status=status.HTTP_404_NOT_FOUND)
