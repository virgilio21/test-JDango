#Django
from django.shortcuts import render
from django.http import Http404
#Models
from.models import Provider, Products, Users, Employees
from django.contrib.auth.models import User
#Serializers
from.serializers import *
#rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#Authentication
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#Provider Views
class ProviderList(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     #Retorna todos los datos del modelo provider
     def get(self, request, format=None):
          listProvider = Provider.objects.all()
          serializer = ProviderSerializer(listProvider, many=True)
          return Response(serializer.data)

     #Crea un objeto provider
     def post(self,request, format=None):
          serializer = ProviderSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProviderDetail(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get_object(self, pk):
        try:
            return Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            raise Http404

     def get(self,request,pk,format=None):
          provider = self.get_object(pk)
          serializer =  ProviderSerializer(provider)
          return Response(serializer.data)

     def put(self,request,pk,format=None):
          provider = self.get_object(pk=pk)
          serializer = ProviderSerializer(provider, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self,request,pk,format=None):
          provider = self.get_object(pk=pk)
          provider.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

#Product Views
class ProductList(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get(self, request, format=None):
          user=User.objects.get(id=1)
          token = Token.objects.get_or_create(user=user)
          print(token[0])
          listProduct = Products.objects.all()
          serializer = ProductViewSerializer(listProduct, many=True)
          return Response(serializer.data)
     
     def post(self, request, format=None):
          serializer = ProductSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)     
     def get_object(self, pk):
        try:
             #.select_related('id_provider') no es necesario el nestede ralated de la serializacion lo hace
             product= Products.objects.get(pk=pk)
             print('''
             

             Proveedor: {}
             

             '''.format(product))
             return product
        except Products.DoesNotExist:
            raise Http404

     def get(self,request,pk,format=None):
          product = self.get_object(pk)
          serializer =  ProductSerializer(product)
          return Response(serializer.data)
     
     def put(self,request,pk,format=None):
          product = self.get_object(pk)
          serializer = ProductSerializer(product, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
     
     def delete(self,request,pk,format=None):
          product=self.get_object(pk)
          serializer = ProductSerializer(product, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_204_NO_CONTENT)

# Users Views

class UserList(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get(self, request, format=None):
          users = Users.objects.all()
          serializer = UsersSerializer(users, many=True)
          return Response(serializer.data)

     def post(self, request, format=None):
          serializer = UsersSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

     def get(self,request,pk,format=None):
          user = self.get_object(pk)
          serializer =  UsersSerializer(user)
          return Response(serializer.data)

     def put(self,request,pk,format=None):
          user = self.get_object(pk)
          serializer = UsersSerializer(user, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_400_BAD_REQUEST)

     def delete(self,request,pk,format=None):
          user = self.get_object(pk)
          user.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

#Employees view
class EmployeList(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get(self, request, format=None):
          employee = Employees.objects.all()
          serializer = EmployeesViewSerializer(employee, many=True)
          return Response(serializer.data)

     def post(self, request, format=None):
          serializer = EmployeesSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployesDetail(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get_object(self, pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404

     def get(self,request,pk,format=None):
          employee = self.get_object(pk)
          serializer =  EmployeesViewSerializer(employee)
          return Response(serializer.data)

     def put(self,request,pk,format=None):
          employee  = self.get_object(pk)
          serializer = EmployeesSerializer(employee, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_400_BAD_REQUEST)

     def delete(self,request,pk,format=None):
          employee  = self.get_object(pk)
          serializer = EmployeesSerializer(employee, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_204_NO_CONTENT)

class HistoricalList(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get(self, request, format=None):
          historical = Historical.objects.all()
          serializer = HistoricalViewSerializer(historical, many=True)
          return Response(serializer.data)

     def post(self, request, format=None):
          serializer = HistoricalSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(status=status.HTTP_400_BAD_REQUEST)

class HistoricalDetail(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get_object(self, pk):
          try:
               historical = Historical.objects.get(pk=pk)
               return historical
          except historical.DoesNotExist:
               return Http404

     def get(self,request,pk,format=None):
          historical = self.get_object(pk)
          serializer =  HistoricalViewSerializer(historical)
          return Response(serializer.data)

     def put(self,request,pk,format=None):
          historical = self.get_object(pk)
          serializer = HistoricalSerializer(historical, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_400_BAD_REQUEST)

     def delete(self,request,pk,format=None):
          historical = self.get_object(pk)
          historical.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerList(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get(self, request, format=None):
          custumer = Customers.objects.all()
          serializer = CustomersSerializer(custumer, many=True)
          return Response(serializer.data)

     def post(self, request, format=None):
          serializer = CustomersSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get_object(self, pk):
        try:
            return Customers.objects.get(pk=pk)
        except Customers.DoesNotExist:
            raise Http404

     def get(self,request,pk,format=None):
          employee = self.get_object(pk)
          serializer =  CustomersSerializer(employee)
          return Response(serializer.data)

     def put(self,request,pk,format=None):
          custumer  = self.get_object(pk)
          serializer = CustomersSerializer(custumer, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_400_BAD_REQUEST)

     def delete(self,request,pk,format=None):
          custumer  = self.get_object(pk)
          serializer = CustomersSerializer(custumer, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_204_NO_CONTENT)       

     
class SaleList(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get(self, request, format=None):
          sale = Sales.objects.all()
          serializer = SalesViewSerializer(sale, many=True)
          return Response(serializer.data)

     def post(self, request, format=None):
          serializer = SalesSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleDetail(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get_object(self, pk):
        try:
            return Sales.objects.get(pk=pk)
        except Sales.DoesNotExist:
            raise Http404

     def get(self,request,pk,format=None):
          sale = self.get_object(pk)
          serializer =  SalesViewSerializer(sale)
          return Response(serializer.data)

     def put(self,request,pk,format=None):
          sale  = self.get_object(pk)
          serializer = SalesSerializer(sale, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_400_BAD_REQUEST)

     def delete(self,request,pk,format=None):
          sale  = self.get_object(pk)
          serializer = SalesSerializer(sale, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_204_NO_CONTENT)

class Product_has_SaleList(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get(self, request, format=None):
          product_has_sale = Product_has_Sale.objects.all()
          serializer = Product_has_SaleViewSerializer(product_has_sale, many=True)
          return Response(serializer.data)

     def post(self, request, format=None):
          serializer = Product_has_SaleSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Product_has_SaleDetail(APIView):
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticated,)
     def get_object(self, pk):
        try:
            return Product_has_Sale.objects.get(pk=pk)
        except Product_has_Sale.DoesNotExist:
            raise Http404

     def get(self,request,pk,format=None):
          product_has_Sale = self.get_object(pk)
          serializer =  Product_has_SaleViewSerializer(product_has_Sale)
          return Response(serializer.data)

     def put(self,request,pk,format=None):
          product_has_Sale  = self.get_object(pk)
          serializer = Product_has_SaleViewSerializer(product_has_Sale, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_400_BAD_REQUEST)

     def delete(self,request,pk,format=None):
          product_has_Sale  = self.get_object(pk)
          serializer = Product_has_SaleViewSerializer(product_has_Sale, data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(status=status.HTTP_204_NO_CONTENT)