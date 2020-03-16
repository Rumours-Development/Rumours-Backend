from django.db import models

class Home(models.Model):
	title = models.CharField(max_length=120)

	def _str_(self):
		return self.title