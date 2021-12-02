from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100, null=False)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    codproduto = models.IntegerField()
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=12, decimal_places=10)
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.nome
    
    
    
