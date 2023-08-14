from django.urls import path
from product.views import (
    CategoryApiView,
    CategorySingleApiView,
    ProductApiView,
    ProductCreateView
    )


urlpatterns = [
    path(
        'categories/',
        CategoryApiView.as_view(),
        name='categories'
        ),
    path(
        'category/<slug>/',
        CategorySingleApiView.as_view(),
        name='category'
        ),
    path(
        'products/',
        ProductApiView.as_view(),
        name='products'
        ),
    path(
        'products/create/',
        ProductCreateView.as_view(),
        name='product-create'
        ),
]
