from django.db import models
from categories.models import Category
from brands.models import Brand

class Product(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products') # não pode deletar a categorie se tiver algum produto vinculado à ela.
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products') # não pode deletar a brand se tiver algum produto vinculado à ela.
    description = models.TextField(null=True, blank=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2) # decimal_places é quantos pontos tem no numero
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) # Ao criar o registro ele automaticamente adiciona o momento atual somente na primeira vez.
    update_at = models.DateTimeField(auto_now=True) # Similar ao auto_now_add mas pode ser atualizado.

    # Ordena por titulo
    class Meta:
        ordering = ['title']
    
    # Retorna o titulo
    def __str__(self):
        return self.title