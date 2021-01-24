from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Order
from .forms import OrderForm


def orders_listing_view(request):
    template_name = "orders_listing.html"
    orders = Order.get_all()
    paginator = Paginator(orders, 10)
    page = request.GET.get('page', 1)
    try:
        context_orders = paginator.page(page)
    except PageNotAnIntegers:
        context_orders = paginator.page(1)
    except EmptyPage:
        context_orders = paginator.page(paginator.num_pages)

    return render(request, template_name, {"orders":context_orders, "page_title": "Orders history"})

def order_detail_view(request, pk):
    template_name = "order_detail.html"
    order = Order.get_by_id(pk)
    return render(request, template_name, {"order":order, "page_title": f"Order #{order.id}"})

def lended_books_views(request):
    template_name = "open-orders.html"
    context = {}
    orders = Order.get_not_returned_books()
    if len(orders) == 0:
            return render(request, template_name, {"orders":0, "page_title": "Lended books"})

    paginator = Paginator(orders, 10)
    page = request.GET.get('page', 1)
    try:
        context["orders"] = paginator.page(page)
    except PageNotAnInteger:
        context["orders"] = paginator.page(1)
    except EmptyPage:
        context["orders"] = paginator.page(paginator.num_pages)

    context["page_title"] = "Lended books"
    context["page"] = page

    print("\n"*10 + str(len(orders)) + "\n"*10)


    
    return render(request, template_name, context)




def create_order(request):
    error = ''
    form = OrderForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orders')
        else:
            error = '"Returning Date" field should have format: yyyy-mm-dd'

    template_name = "order_form.html"
    context = {'form': form,
               'error': error}
    return render(request, template_name, context)


def update_order(request, pk):
    error = ''
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect(f'/orders/{pk}')
        else:
            error = '"Returning Date" field should have format: yyyy-mm-dd'

    context = {'form': form,
               'id': pk,
               'error': error}
    template_name = "order_update.html"
    return render(request, template_name, context)



def delete_order(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()

        #return redirect('/order_listing')
        return redirect('/orders')


    template_name = "order_delete.html"
    context = {'item': order}
    return render(request, template_name, context)


