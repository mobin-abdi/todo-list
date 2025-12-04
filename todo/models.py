from django.db import models

class TodoItem(models.Model):
    PERIORITY_CHOISE = [
        ('L', 'low'),
        ('M', 'medium'),
        ('H', 'high'),
    ]

    name = models.CharField(max_length=60)
    context = models.TextField()
    periority = models.CharField(max_length=1, choices=PERIORITY_CHOISE, default='M')
    
    def __str__(self):
        return self.name
    
