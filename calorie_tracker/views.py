from django.shortcuts import render, redirect
from .models import FoodItem
from django.shortcuts import get_object_or_404

def delete_food(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
    food.delete()
    return redirect("home")

def home(request):

    if request.method == "POST":
        day = request.POST.get("day")
        meal = request.POST.get("meal")
        food = request.POST.get("food")
        calories = request.POST.get("calories")

        FoodItem.objects.create(
            day=day,
            meal=meal,
            food=food,
            calories=calories
        )

        return redirect("home")

    foods = FoodItem.objects.all().order_by("-id")

    total_calories = sum(
        food.calories for food in foods
    )

    context = {
        "foods": foods,
        "total_calories": total_calories,
    }

    return render(
        request,
        "calorie_tracker/index.html",
        context
    )