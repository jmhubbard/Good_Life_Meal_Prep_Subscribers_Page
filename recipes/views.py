from django.shortcuts import render

from .models import Recipe

def menu(request):
    current_user = request.user
    recipes = Recipe.objects.all()
    context ={
        'current_user': current_user,
        'recipes': recipes
    }

    return render(request, 'recipes/menu.html', context)
