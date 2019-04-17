from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    amount = models.SmallIntegerField()
    description = JSONField()
    status = models.BooleanField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    id_provider = models.ForeignKey('Provider', on_delete=models.CASCADE)

    def __str__(self):
        return "Nombre {} - precio{} - descripcion {} - status {}".format(self.product_name, self.price, self.description, self.status)

class Provider(models.Model):
    name = models.CharField(max_length=45)
    number = models.IntegerField()

    def __str__(self):
        return "Nombre: {} ------ Numero: {}".format(self.name,self.number)

class Employees(models.Model):
    name = models.CharField(max_length=45)
    las_name = models.CharField(max_length=50)
    rfc = models.CharField(max_length=45)
    direction = models.CharField(max_length=100, null=True)
    birthdate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    passwd = models.CharField(max_length=45)
    telephone = models.CharField(max_length=15, null=True)
    status = models.BooleanField()
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return "Nombre : {} --------- status: {}".format(self.name, self.status)

class Users(models.Model):
    user_type = models.CharField(max_length=45)
    description = models.CharField(max_length=450)

class Historical(models.Model):
    description = models.CharField(max_length=45)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE)

class Product_has_Sale(models.Model):
    id_product = models.ForeignKey('Products', on_delete=models.CASCADE)
    id_sale = models.ForeignKey('Sales', on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    status = models.BooleanField()

class Sales(models.Model):
    total_price = models.DecimalField(max_digits=19,decimal_places=10)
    sale_date = models.DateField()
    id_employee = models.ForeignKey('Employees', on_delete=models.CASCADE)
    id_customers = models.ForeignKey('Customers', on_delete=models.CASCADE)
    status = models.BooleanField()

class Customers(models.Model):
    customer_name = models.CharField(max_length=45)
    customer_phone = models.CharField(max_length=15)
    status = models.BooleanField()