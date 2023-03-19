from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.id}_{self.name}"
    



class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)


