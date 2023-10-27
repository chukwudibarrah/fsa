from django.db import models
from django.core.validators import FileExtensionValidator
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField()
    date = models.DateTimeField(editable=True)
    image = models.ImageField(default='default.png', upload_to='pimages', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f"Post: {self.title}"
    