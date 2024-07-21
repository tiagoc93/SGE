from django.db import models
from products.models import Product

class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ao criar o registro ele automaticamente adiciona o momento atual somente na primeira vez.
    update_at = models.DateTimeField(auto_now=True) # Similar ao auto_now_add mas pode ser atualizado.

    class Meta:
        ordering = ['-created_at'] # O menos na frente o django considera descendente (do mais novo pro mais antigo)

    def __str__(self):
        return str(self.product)
