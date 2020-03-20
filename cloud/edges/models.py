from django.db import models

class Edge(models.Model):
    image = models.ImageField(upload_to ='uploads/')
    gray_scale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

