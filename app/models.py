from django.db import models

# Create your models here.
class Story(models.Model):
    
    title=models.CharField(max_length=200)
    body=models.TextField(db_index=True)
    footer=models.TextField(blank=True)
    publish=models.DateTimeField(auto_now_add=True)
    date=models.DateField(auto_now_add=True)
    class Meta:
        ordering=('-title',)
        verbose_name='Search Menu'
    def __str__(self):
        return self.title



    
