from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Category


def product_to_dict(product):
    return {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category': product.category.id,
    }


def category_to_dict(category):
    return {
        'id': category.id,
        'name': category.name,
    }


def product_list(request):
    """GET /api/products/ — List of all Products"""
    products = Product.objects.select_related('category').all()
    data = [product_to_dict(p) for p in products]
    return JsonResponse(data, safe=False)


def product_detail(request, pk):
    """GET /api/products/<id>/ — Get one Product by ID"""
    product = get_object_or_404(Product, pk=pk)
    return JsonResponse(product_to_dict(product))


def category_list(request):
    """GET /api/categories/ — List of all Categories"""
    categories = Category.objects.all()
    data = [category_to_dict(c) for c in categories]
    return JsonResponse(data, safe=False)


def category_detail(request, pk):
    """GET /api/categories/<id>/ — Get one Category by ID"""
    category = get_object_or_404(Category, pk=pk)
    return JsonResponse(category_to_dict(category))


def category_products(request, pk):
    """GET /api/categories/<id>/products/ — List of Products by Category"""
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()
    data = [product_to_dict(p) for p in products]
    return JsonResponse(data, safe=False)
