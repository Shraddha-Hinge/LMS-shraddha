from django.db import models
from accounts.models import User
from course_management.models import Course

# Subscription Plan Model
class SubscriptionPlan(models.Model):
    PLAN_CHOICES = (
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=10, choices=PLAN_CHOICES)
    stripe_plan_id = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.duration} (${self.price})"

# User Subscription Model
class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    stripe_subscription_id = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.plan.name} ({'Active' if self.is_active else 'Expired'})"

# Payment Model
class Payment(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="payments", null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[("stripe", "Stripe"), ("razorpay", "Razorpay"), ("offline", "Offline")])
    transaction_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.amount} ({self.status})"
