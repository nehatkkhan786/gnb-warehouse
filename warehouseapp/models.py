from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=250)
	price = models.IntegerField()
	quantity = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.name

class Transaction(models.Model):
	object_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	operation_choice = [
		(1, 'Addition'),
		(2, 'Deletion'),
	]
	operation = models.IntegerField(choices=operation_choice)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	remarks = models.CharField(max_length=1000, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now=True)

	