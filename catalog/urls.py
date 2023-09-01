from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductCreateView, ProductUpdateView, home, ProductsDeleteView, \
    ProductsDetailView

app_name = CatalogConfig.name
urlpatterns = [
    path('', cache_page(60)(home), name='home'),
    path('product/', ProductListView.as_view(), name='product_list'),
    # path('product/', never_cache(ProductListView.as_view()), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductsDeleteView.as_view(), name='delete_product'),
    path('detail/<int:pk>/', cache_page(60)(ProductsDetailView.as_view()), name='detail_product'),
    ]
