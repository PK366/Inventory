from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views import View
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
@login_required

def index(request):
    orders = Order.objects.all()
    products= Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('dashboard-index')
       
    else:
        form = OrderForm()

    context={
        'orders': orders,
        'form': form,
        'products': products,
    }
    return render(request, 'dashboard/index.html', context)

@login_required

def user(request):
    workers = User.objects.all()
    user_count = User.objects.all().count()
    order_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    context = {
        'workers': workers,
        'user_count': user_count,
        'order_count': order_count,
        'product_count': product_count,
    }
    
    return render(request, 'dashboard/user.html', context)
@login_required
def user_detail(request, pk):
    workers = User.objects.get(id=pk)
    
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/user_detail.html', context)



@login_required
def product(request):
    items = Product.objects.all()
   # items = Product.objects.raw('SELECT * FROM dashboard_product')
    product_count = Product.objects.all().count()
    user_count = User.objects.all().count()
    order_count = Order.objects.all().count()


    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{ product_name } has been added successfully')
            return redirect('dashboard-product')
            
    else:
        form = ProductForm()
    context = {
        'product_count': product_count,
        'items': items,
        'form': form,
        'user_count': user_count,
        'order_count': order_count,
        
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    form = ProductForm(instance=item)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    context = {
        'form': form
        
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required
def order(request):
    orders = Order.objects.all()
    order_count = Order.objects.all().count()
    user_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    context = {
        'orders': orders,
        'order_count': order_count,
        'user_count': user_count,
        'product_count': product_count,
    }
   

    return render(request, 'dashboard/order.html', context)


 