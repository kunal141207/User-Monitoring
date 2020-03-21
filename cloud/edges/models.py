from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to ='uploads/')
    gray_scale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edge_id = models.ForeignKey('Edge', on_delete =models.CASCADE)


class Edge(models.Model):
    gray_scale_setting = models.BooleanField(default=False)
    time_setting = models.FloatField(default=60)
