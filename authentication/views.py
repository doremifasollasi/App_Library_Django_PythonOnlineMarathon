from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import CustomUser
from order.models import Order


def users_listing_view(request):
    users = CustomUser.get_all()
    paginator = Paginator(users, 20)
    page = request.GET.get('page', 1)
    try:
        context_users = paginator.page(page)
    except PageNotAnInteger:
        context_users = paginator.page(1)
    except EmptyPage:
        context_users = paginator.page(paginator.num_pages)

    return render(request, "users_listing.html", {"users":context_users, "page_title": "Users", 'page':page})

def user_detail_view(request, pk):
    template_name = "user_detail.html"
    context = {}
    user = CustomUser.get_by_id(pk)
    context["user"] = user
    context["orders"] = Order.get_orders_by_user_id(pk)
    context["page_title"] = "{0} {1} profile".format(user.first_name, user.last_name)
    return render(request, template_name, context)

def sign_in(request):
    return render(request, 'sign_in.html')


def sign_up(request):
    return render(request, 'sign_up.html')


