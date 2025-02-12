from django.contrib import admin
from accounts.models import User
from course_management.models import Course
from billing.models import SubscriptionPlan
from communication.models import LiveSession
from notifications.models import Notification

admin.site.register(User)
admin.site.register(Course)
admin.site.register(SubscriptionPlan)
admin.site.register(LiveSession)
admin.site.register(Notification)
