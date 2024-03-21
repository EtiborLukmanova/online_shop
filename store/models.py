from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    catalog_number = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)


class Order(models.Model):
    STATUS_CHOICES = (
        ('received', 'Received'),
        ('processed', 'Processed'),
        ('shipped', 'Shipped'),
        ('cancelled', 'Cancelled'),
    )

    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def discount_price(self):
        return self.total_price - (self.total_price * self.product.discount / 100)
