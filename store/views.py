from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator

# Create your views here.
def store(request,category_slug=None):
    
    products = None
    category = None
    if category_slug :
        category = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(is_available = True,category = category)
        page = request.GET.get('page')
        paginator = Paginator(products,2)
        paged_product = paginator.get_page(page)
        
    else :
        products = Product.objects.filter(is_available = True)
        paginator = Paginator(products,7)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
     
    categories = Category.objects.all()
    return render(request,'store/store.html',{'products':paged_product,'categories':categories},)



def product_detail(request,caregory_slug,product_slug):
    single_product = Product.objects.get(slug = product_slug,category__slug = caregory_slug)
    return render(request,'store/product-detail.html',{'product':single_product})