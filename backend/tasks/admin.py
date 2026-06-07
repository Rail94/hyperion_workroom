from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ("title", "completed", "created_by")
	list_filter = ("completed",)
	search_fields = ("title",)
	ordering = ("created_at",)
	readonly_fields = ("created_by","created_at", "updated_at",)

	def save_model(self, request, obj, form, change):
		obj.created_by = request.user
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs if request.user.is_superuser else qs.filter(created_by=request.user)