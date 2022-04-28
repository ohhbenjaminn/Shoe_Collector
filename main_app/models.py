from django.db import models
from django.urls import reverse

class Accessory(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size =  models.DecimalField(max_digits = 3, decimal_places = 1)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return f"The shoe named {self.name} has id of {self.id}"
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})


CONDITIONS = (
    ('DS', 'Deadstock'),
    ('VNDS', 'Moderate'),
    ('U', 'Used'),
)

class Release(models.Model):
	date = models.DateField('release date')
	condition = models.CharField(
		max_length=4,
		choices=CONDITIONS,
		default=CONDITIONS[0][0]
	)

	shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.get_condition_display()} on {self.date}"

	class Meta:
		ordering = ['-date']