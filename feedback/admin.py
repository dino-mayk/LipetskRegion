from django.contrib import admin

from feedback.models import Feedback


class Feedback_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Feedback, Feedback_admin)
