from django.db import models

class Mineral(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=300, null=True, blank=True)
    formula = models.CharField(max_length=300, null=True, blank=True)
    crystal_system = models.CharField(max_length=300, null=True, blank=True)
    unit_cell = models.CharField(max_length=300, null=True, blank=True)
    color = models.CharField(max_length=300, null=True, blank=True)
    cleavage = models.CharField(max_length=300, null=True, blank=True)
    crystal_symmetry = models.CharField(max_length=300, null=True, blank=True)
    mohs_scale = models.CharField(max_length=300, null=True, blank=True)
    image_caption = models.CharField(max_length=300, null=True, blank=True)
    image_filename = models.CharField(max_length=300, null=True, blank=True)
    strunz_classification = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name
