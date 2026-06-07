from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	completed = models.BooleanField(default=False)

	created_by = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name="created_tasks",
	)

	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title