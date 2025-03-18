from django.db import models

class Plant(models.Model):
   genus = models.CharField("genus", max_length= 256, null=True, blank=True)
   species = models.CharField("species", max_length= 256, null=True, blank=True)
   image = models.ImageField(upload_to='images/', null=True, blank=True)
   common_name = models.CharField("common_name", max_length= 256, null=True, blank=True)
   year = models.CharField("year", max_length= 256, null=True, blank=True)
   collector = models.CharField("collector", max_length= 256, null=True, blank=True)

   # location of where the plant was collected from
   location = models.CharField("location", max_length= 256, null=True, blank=True)
   cabinet = models.CharField("cabinet", max_length= 256)
   drawer = models.CharField("drawer", max_length= 256)
   extra_info = models.CharField("extra_info", max_length= 256, null=True, blank=True)

   def __str__(self):
      return f"{self.genus} {self.species}"
   
