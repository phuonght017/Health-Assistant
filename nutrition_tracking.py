# Example database for food (you can replace this with a more complex database)
food_database = {
    "apple": 52,  # calories per 100g
    "banana": 96,
    "chicken": 239
}

user_nutrition_data = {}

def nutrition(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    food_log = update.message.text.split()

    total_calories = 0
    for item in food_log:
        food, quantity = item.split(":")
        if food in food_database:
            calories = food_database[food] * (int(quantity.replace("g", "")) / 100)
            total_calories += calories
        else:
            update.message.reply_text(f"Food item {food} not found in the database.")

    # Save data (again, can be replaced with a database)
    if user_id not in user_nutrition_data:
        user_nutrition_data[user_id] = []

    user_nutrition_data[user_id].append(total_calories)
    update.message.reply_text(f"Total calories consumed: {total_calories} kcal")
