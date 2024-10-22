from django.shortcuts import render, redirect

from tastyRecipesApp.recipes.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from tastyRecipesApp.recipes.models import Recipe
from tastyRecipesApp.utils import get_profile


def show_catalogue(request):
    all_recipes = Recipe.objects.all()
    profile = get_profile()

    context = {
        'all_recipes': all_recipes,
        'profile': profile,
    }
    return render(request, 'recipes/catalogue.html', context)


def create_recipe(request):
    form = RecipeCreateForm(request.POST or None)
    profile = get_profile()

    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author_id = profile.pk
        recipe.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'recipes/create-recipe.html', context)


def show_details_recipe(request, recipe_id):
    profile = get_profile()
    recipe = Recipe.objects.get(pk=recipe_id)
    all_ingredients = recipe.ingredients.split(', ')

    context = {
        'profile': profile,
        'recipe': recipe,
        'all_ingredients': all_ingredients,
    }

    return render(request, 'recipes/details-recipe.html', context)


def edit_recipe(request, recipe_id):
    profile = get_profile()
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeEditForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'recipe': recipe,
        'form': form
    }

    return render(request, 'recipes/edit-recipe.html', context)


def delete_recipe(request, recipe_id):
    profile = get_profile()
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeDeleteForm(instance=recipe)

    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogue')

    context = {
        'profile': profile,
        'recipe': recipe,
        'form': form
    }

    return render(request, 'recipes/delete-recipe.html', context)
