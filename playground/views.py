from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, ExpressionWrapper, Func, Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.db import models
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem




# def say_hello(request):
#     query_set = Product.objects.all()
#     for product in query_set:
#         print(product)
#     # print(query_set)
#     return render(request, 'hello.html', {'name': 'Mosh'})

# def say_hello(request):
#     try:
#         product = Product.objects.get(pk=0)
#     except ObjectDoesNotExist:
#         pass
# return render(request, 'hello.html', {'name': 'Mosh'})

# def say_hello(request):
#     exist = Product.objects.filter(pk=0).exists()
#     print(exist)
#     # print(query_set)
#     return render(request, 'hello.html', {'name': 'Mosh'})

# def say_hello(request):
#     query_set = Product.objects.filter(unit_price__gt=20)
    
#     return render(request, 'hello.html', {'name': 'Mosh'})

# def say_hello(request):
#     query_set = Product.objects.filter(unit_price__range=(20, 30))
    
#     return render(request, 'hello.html', {'name': 'Olaifa Wilson', 'products': list(query_set)})
    
# def say_hello(request):
    # try:
    # query_set = Product.objects.filter(collection__id__range=(1, 3))
    # query_set = Product.objects.filter(title__contains='coffee')
    # query_set = Product.objects.filter(title__icontains='coffee')
    # query_set = Product.objects.filter(title__istartswith='coffee')
    # query_set = Product.objects.filter(last_update__year = 2021)
    # query_set = Product.objects.filter(description__isnull=True)
    # return render(request, 'hello.html', {'name': 'Olaifa Wilson', 'products': list(query_set)})

#Applying multiple_filters for complex look up

# def say_hello(request):
#     # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
#     # query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    
#     # using Q class for OR instead of AND
#     # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
#     # query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20)) 
#     return render(request, 'hello.html', {'name': 'Hemark Olaifa', 'products': list(query_set)})

# referencing using F object
# def say_hello(request):
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    # query_set = Product.objects.filter(inventory=F('collection__id'))
    # return render(request, 'hello.html', {'name': 'Sola Alisson', 'products': list(query_set)})


# sorting query
# def say_hello(request):
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()
    # query_set = Product.objects.filter(collection__id=1).order_by('unit_price')
    # return render(request, 'hello.html', {'name': 'Sola Alisson', 'products': list(query_set)})
    # query_set = Product.objects.order_by('-unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')
    # return render(request, 'hello.html', {'name': 'Sola Alisson', 'product': (query_set)})
    # return render(request, 'hello.html', {'name': 'Sola Alisson', 'product': product})



# limiting results
# def say_hello(request):
#     query_set = Product.objects.all()[5:20]
#     return render(request, 'hello.html', {'name': 'Sola Alisson', 'products': query_set})


#  selecting fields to query   
# def say_hello(request):
    # query_set = Product.objects.values('id', 'title')
    # query_set = Product.objects.values('id', 'title', 'collection__title')

    # return render(request, 'hello.html', {'name': 'Sola Alisson', 'products': query_set})


# def say_hello(request):
#     order = Product.objects.filter(title__in=OrderItem.objects.values('product__title').distinct()).order_by('title')

#     return render(request, 'hello.html', {'name': 'Adeyanju Samuel', 'ordered_items': list(order)})

# def say_hello(request):
#     query_set = Product.objects.only('id', 'title')

#     return render(request, 'hello.html', {'name': 'Adeyanju Samuel', 'products': list(query_set)})


# selecting related fields
# def say_hello(request):
    # select related
    # query_set = Product.objects.select_related('collection').all()
    
    # prefetch_related
    # query_set = Product.objects.prefetch_related('promotions').all()
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # return render(request, 'hello.html', {'name': 'Sammy Michelle', 'products': list(query_set)})

# def say_hello(request):
#     query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
#     return render(request, 'hello.html', {'name': 'Sammy Michelle', 'orders': list(query_set)})


# aggregate method
# def say_hello(request):
    # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    
#     # return render(request, 'hello.html', {'name': 'Sammy Michelle', 'result': result})

# # annotations
# def say_hello(request):

#     # query_set = Customer.objects.annotate(is_new=Value(True))

#     # using the F class to reference class that already exist in our field to create a new field
#     # query_set = Customer.objects.annotate(new_id=F('id'))
#     query_set = Customer.objects.annotate(new_id=F('id') + 1)

#     return render(request, 'hello.html', {'name': 'Sammy Michelle', 'query': list(query_set)})



# CALLING DATABASE FUNCTION(CONCAT)
# def say_hello(request):
    # query_set = Customer.objects.annotate(
    #         # CONCAT 
    #         full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )

    # query_set = Customer.objects.annotate(
    #         # CONCAT 
    #         full_name=Concat('first_name', Value(' '), 'last_name'))
    # return render(request, 'hello.html', {'name': 'Sammy Michelle', 'query': list(query_set)})

# def say_hello(request):
#      query_set = Customer.objects.annotate(
#             orders_count=Count('order')
#     )
#      return render(request, 'hello.html', {'name': 'Sammy Michelle', 'query': list(query_set)})


# # EXPRESSIONWRAPPER
# def say_hello(request):
#     discounted_price=ExpressionWrapper(
#         F('unit_price') * 0.8, output_field=models.DecimalField(max_digits=6, decimal_places=2))
#     query_set = Product.objects.annotate(
#             discounted_price=discounted_price
#     )
#     return render(request, 'hello.html', {'name': 'Sammy Michelle', 'query': list(query_set)})


# def say_hello(request):
#     content_type = ContentType.objects.get_for_model(Product)

#     query_set = TaggedItem.objects \
#     .select_related('tag') \
#     .filter(
#         content_type=content_type,
#         object_id=1
#     )
#     return render(request, 'hello.html', {'name': 'Sammy Michelle', 'tags': list(query_set)})


# def say_hello(request):
#     query_set = TaggedItem.objects.get_tags_for(Product, 1)
#     return render(request, 'hello.html', {'name': 'Sammy Michelle', 'tags': list(query_set)})

# def say_hello(request):
#     query_set = Product.objects.all()
#     # list(query_set)
#     # list(query_set)
#     query_set[0]
#     list(query_set)
#     return render(request, 'hello.html', {'name': 'Killer Bean'})


# # creating objects into the database
# def say_hello(request):
#     collection = Collection()
#     collection.title = 'Video Games'
#     collection.featured_product = Product(pk=1)
#     collection.save()

#     # collection = Collection.objects.create(name='a', featured_product_id=1)
    
#     return render(request, 'hello.html', {'name': 'Killer Bean'})


# updating objects in the database
# def say_hello(request):
    # collection = Collection(pk=12)
    # collection.title = 'Fabrics'
    # collection.featured_product = Product(pk=3)
    # collection.save()

    # without updating the title field 
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    # collection = Collection.objects.filter(pk=11).update(featured_product=None)
    
    # return render(request, 'hello.html', {'name': 'Killer Bean'})

# deleting objects from the database
# def say_hello(request):
#     # deleting single object 
#     # collection = Collection(pk=11)
#     # collection.delete()

#     # deleting multiple objects 
#     Collection.objects.filter(id__gt=10).delete()
    
#     return render(request, 'hello.html', {'name': 'Killer Bean'})


# from django.db import transaction
# def say_hello(request):
#     with transaction.atomic():

#         order = Order()
#         order.customer_id = 1
#         order.save()

#         item = OrderItem()
#         item.order = order
#         item.product_id = 1
#         item.quantity = 1
#         item.unit_price = 10
#         item.save()
    
#     return render(request, 'hello.html', {'name': 'Killer Bean'})


# executing raw sequel language
from django.db import connection
def say_hello(request):
    # query_set = Product.objects.raw('SELECT * FROM store_product')
    query_set = Product.objects.raw('SELECT id, title FROM store_product')

    with connection.cursor() as cursor:
        # cursor.execute()
        cursor.callproc('get_customers', [1, 2, 3, 'hi'])

    # cursor = connection.cursor


    return render(request, 'hello.html', {'name': 'Killer Bean', 'result': list(query_set)})


