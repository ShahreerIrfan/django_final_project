from django.shortcuts import render,redirect
from cart.models import Cart,CartItem

# Create your views here.

def order_complete(request):
    return render(request,'orders/order_complete.html')


def place_order(request):
    print(request.POST)
    cart_items = None
    tax = 0
    total = 0
    grand_total = 0
    # 1 --- 100
    # 5 --- 100*5
    cart_items = CartItem.objects.filter(user = request.user)
    
    if cart_items.count() < 1:
        return redirect('store')
    
    for item in cart_items:
        total += item.product.price * item.quantity
    print(cart_items)  
    tax = (2*total)/100 # 2 % vat
    grand_total = total + tax
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.order_total = grand_total
            form.instance.tax = tax
            form.instance.ip = request.META.get('REMOTE_ADDR')
            form.instance.payment = 2
            saved_instance = form.save()  # Save the form data to the database
            form.instance.order_number = saved_instance.id
            
            form.save()
            print('form print', form)
            return redirect(sslcommerz_payment_gateway(request,  saved_instance.id, str(request.user.id), grand_total))

    return render(request, 'orders/place-order.html',{'cart_items' : cart_items, 'tax' : tax,'total' : total, 'grand_total' : grand_total})