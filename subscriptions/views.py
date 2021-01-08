from django.shortcuts import render
from .models import SubscriptionItem

def subscriptionView(request):
    current_user = request.user
    subscriptions = SubscriptionItem.objects.filter(user = current_user, item__is_active = True).order_by('item__name')
    context ={
        'current_user': current_user,
        'subscriptions': subscriptions
    }

    return render(request, 'subscriptions/subform.html', context)
