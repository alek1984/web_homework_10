from djongo import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    class Meta:
        app_label = 'quotes'

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.JSONField()

    class Meta:
        app_label = 'quotes'

