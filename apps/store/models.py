from django.db import models
from django.utils.text import slugify
from apps.accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'uma categoria'
        verbose_name_plural = 'Categorias'

    
class ProductBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'uma marca'
        verbose_name_plural = 'Marca'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, editable=False)
    barcode = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='img/products')
    brand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    total_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    total_reviews = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.price <= 1000:
            self.price = self.price * 100
        super(Product, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = 'um produto'
        verbose_name_plural = 'Produtos'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0, validators=[MinValueValidator(0, "Avaliação não pode ser inferior a 0 estrelas"), MaxValueValidator(5, "Avaliação não pode ser superior a 5 estrelas")])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'uma avaliação'
        verbose_name_plural = 'Avaliações'
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    tax_price = models.DecimalField(max_digits=7, decimal_places=2)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField()
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'um pedido'
        verbose_name_plural = 'Pedidos'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.order
    
    class Meta:
        verbose_name = 'um item'
        verbose_name_plural = 'Item'
