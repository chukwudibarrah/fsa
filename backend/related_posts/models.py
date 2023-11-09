from django.db import models
from django.core.validators import FileExtensionValidator

class RelatedPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='related_images', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.title
