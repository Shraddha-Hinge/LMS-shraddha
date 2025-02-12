from django.contrib import admin
from .models import SubscriptionPlan, UserSubscription, Payment

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "duration", "price", "stripe_plan_id")
    search_fields = ("name", "stripe_plan_id")
    list_filter = ("duration",)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "plan", "start_date", "end_date", "is_active")
    search_fields = ("user__email", "plan__name")
    list_filter = ("is_active", "start_date", "end_date")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "amount", "payment_method", "status", "created_at")
    search_fields = ("user__email", "course__title", "transaction_id")
    list_filter = ("status", "payment_method", "created_at")
