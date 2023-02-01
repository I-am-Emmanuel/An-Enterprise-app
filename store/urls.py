from django.urls import path
from django.urls.conf import include
# from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers 
from . import views
from pprint import pprint

router = routers.DefaultRouter()
# router = SimpleRouter()
# router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')
# router.urls
# the child routers
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_router =  routers.NestedDefaultRouter(router, 'carts', lookup= 'cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items-detail')
# URLConf
# urlpatterrns = router.urls + product_router.urls
urlpatterns = [    
    path('', include(router.urls + products_router.urls + carts_router.urls)),
    # path('', include(products_router.urls)),
#      # path('products/', views.ProductViewSet.as_view({'get': 'list'})),
#     # path('products/', views.ProductList.as_view()),
#     # path('products/', views.product_list),
#     # path('products/<int:pk>/', views.ProductViewSet()),
#     # path('products/<int:pk>/', views.ProductDetail.as_view()),
#     # path('products/<int:id>/', views.product_detail),
#     # path('collections/', views.CollectionViewSet.as_view({'get': 'list'})),
#     # path('collections/', views.CollectionList.as_view()),
#     # path('collections/', views.collection_list),
#     # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
#     # path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
]
