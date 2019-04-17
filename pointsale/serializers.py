from rest_framework import serializers
from.models import *
from django.db import models

#Authentication
from rest_framework.authtoken.models import Token

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id','name','number')

        def create(self, validated_data):
            return Provider.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.number = validated_data.get('number', instance.email)
            instance.save()
            return instance

class ProductViewSerializer(serializers.ModelSerializer):
    id_provider = ProviderSerializer(many = False, read_only=True)

    class Meta:
        model= Products
        fields=('id',"product_name",'price','amount', 'description', 'status', 'image','id_provider')
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields=('id',"product_name",'price','amount', 'description', 'status', 'image','id_provider')
        
        def create(self, validated_data):
            print(validated_data,""" 
            
                <- validated
            
            """)
            """providers_data = validated_data.get('id_provider')
            provider = Provider.objects.get(pk=providers_data)
            validated_data['id_provider'] = provider
            token = Token.objects.create(user=ProductSerializer)
            print(token.key)
            return Provider.objects.create(**validated_data)"""
            products = Products(
                product_name=validated_data['product_name'],
                price=validated_data['price'],
                amount=validated_data['amount'],
                description=validated_data['description'],
                status=validated_data['status'],
                image=validated_data['image'],
                id_provider=validated_data['id_provider']
            )
            products.save()
            return products


        def update(self, instance, validated_data):
            instance.product_name = validated_data.get('product_name', instance.product_name)
            instance.price = validated_data.get('price', instance.price)
            instance.amount = validated_data.get('amount', instance.amount)
            instance.description = validated_data.get('description', instance.description)
            instance.status = validated_data.get('status', instance.status)
            instance.image = validated_data.get('image', instance.image)
            instance.id_provider = validated_data.get('id_provider', instance.id_provider)
            instance.save()
            return instance

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','user_type','description')

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id','name','las_name','rfc','direction','birthdate','passwd','telephone','status','user')

        def create(self, validated_data):
            employees = Employees(name=validated_data['name'],las_name=validated_data['las_name'],rfc=validated_data['rfc'], direction=validated_data['direction'],birthdate=validated_data['birthdate'], passwd=validated_data['passwd'],telephone=validated_data['telephone'], status=validated_data['status'], user=validated_data['user'])
            employees.save()
            return employees

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.las_name = validated_data.get('las_name', instance.las_name)
            instance.rfc = validated_data.get('rfc', instance.rfc)
            instance.direction = validated_data.get('direction', instance.direction)
            instance.birthdate = validated_data.get('birthdate', instance.birthdate)
            instance.passwd = validated_data.get('passwd', instance.passwd)
            instance.telephone = validated_data.get('telephone', instance.telephone)
            instance.status = validated_data.get('status', instance.status)
            instance.user = validated_data.get('user', instance.user)
            instance.save()
            return instance

class EmployeesViewSerializer(serializers.ModelSerializer):
     user = UsersSerializer(many=False, read_only=True)

     class Meta:
         model=Employees
         fields = ('id','name','las_name','rfc','direction','birthdate','telephone','status','user')

class HistoricalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ('id','description','date','employee')

        def create(self, validated_data):
            historical=Historical(description=validated_data['description'], date=validated_data['date'], employee=validated_data['employee'])
            historical.save()
            return historical
        
        def update(self,instance, validated_data):
            instance.description = validated_data.get('description', instance.description)
            instance.date = validated_data.get('date', instance.date)
            instance.employee = validated_data.get('employee', instance.employee)
            return instance

class HistoricalViewSerializer(serializers.ModelSerializer):
    employee = EmployeesViewSerializer(many=False, read_only=True)

    class Meta:
        model = Historical
        fields = ('id','description','date','employee')

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('id','customer_name','customer_phone','status')

        def create(self, validated_data):
            customer=Customers(customer_name=validated_data['customer_name'], customer_phone=validated_data['customer_phone'], status=validated_data['status'])
            customer.save()
            return customer
        
        def update(self,instance, validated_data):
            instance.customer_name = validated_data.get('customer_name', instance.customer_name)
            instance.customer_phone = validated_data.get('customer_phone', instance.customer_phone)
            instance.status = validated_data.get('status', instance.status)
            return instance

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('id','total_price','sale_date','id_employee','id_customers','status')

        def create(self, validated_data):
            sale=Sales(total_price=validated_data['total_price'], sale_date=validated_data['sale_date'], id_employee=validated_data['id_employee'],id_customers=validated_data['id_customers'],status=validated_data['status'])
            sale.save()
            return sale
        
        def update(self,instance, validated_data):
            instance.total_price = validated_data.get('total_price', instance.total_price)
            instance.sale_date = validated_data.get('sale_date', instance.sale_date)
            instance.id_employee = validated_data.get('id_employee', instance.id_employee)
            instance.id_customers = validated_data.get('id_customers', instance.id_customers)
            instance.status = validated_data.get('status', instance.status)
            return instance

class SalesViewSerializer(serializers.ModelSerializer):
    id_employee = EmployeesViewSerializer(many=False, read_only=True)
    id_customers= CustomersSerializer(many=False, read_only=True)

    class Meta:
        model = Sales
        fields = ('id','total_price','sale_date','id_employee','id_customers','status')

class Product_has_SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_has_Sale
        fields = ('id','id_product','id_sale','quantity','status')

        def create(self, validated_data):
            product_has_sale=Product_has_Sale(id_product=validated_data['id_product'], id_sale=validated_data['id_sale'], quantity=validated_data['quantity'],status=validated_data['status'])
            product_has_sale.save()
            return product_has_sale
        
        def update(self,instance, validated_data):
            instance.id_product = validated_data.get('id_product', instance.id_product)
            instance.id_sale = validated_data.get('id_sale', instance.id_sale)
            instance.quantity = validated_data.get('quantity', instance.quantity)
            instance.status = validated_data.get('status', instance.status)
            return instance

class Product_has_SaleViewSerializer(serializers.ModelSerializer):
    id_product = ProductViewSerializer(many=False, read_only=True)
    id_sale= SalesViewSerializer(many=False, read_only=True)

    class Meta:
        model = Product_has_Sale
        fields = ('id','id_product','id_sale','quantity','status')

