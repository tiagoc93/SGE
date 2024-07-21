from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ao criar o registro ele automaticamente adiciona o momento atual somente na primeira vez.
    update_at = models.DateTimeField(auto_now=True) # Similar ao auto_now_add mas pode ser atualizado.

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
