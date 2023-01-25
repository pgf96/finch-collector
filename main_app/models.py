from django.db import models
from django.urls import reverse

# Create your models here.
NAP = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)


class Seed(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('seeds_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    behavior = models.TextField(max_length=150)
    seeds = models.ManyToManyField(Seed)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})


class Napping(models.Model):
    date = models.DateField('nap date')
    nap = models.CharField(
        max_length=1,
        choices=NAP,
        default=NAP[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # get_<field>_display grabs the choice
        return f"{self.get_nap_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
