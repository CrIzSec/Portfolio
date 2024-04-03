from django.db import models

# Create your models here.
class Project(models.Model):
    thumbnail = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images',)

    def __str__(self):
        return self.post.title