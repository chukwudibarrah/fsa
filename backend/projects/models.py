from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    skills = models.TextField()
    link = models.URLField()
    github = models.URLField(null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='pimages', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return f"Project: {self.title}"
    