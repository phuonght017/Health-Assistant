def workout(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    # Example: Personalized suggestion based on goal (weight loss, muscle gain, etc.)
    goal = "weight_loss"  # This should be captured from user input or preferences

    if goal == "weight_loss":
        update.message.reply_text("For weight loss, I suggest the following workout plan:\n- Cardio: 40 mins\n- Strength training: 20 mins\n- Stretching: 10 mins")
    elif goal == "muscle_gain":
        update.message.reply_text("For muscle gain, I suggest the following workout plan:\n- Strength training: 40 mins\n- Cardio: 20 mins")
    else:
        update.message.reply_text("Here’s a balanced workout for overall fitness:\n- Cardio: 30 mins\n- Strength training: 20 mins\n- Flexibility: 10 mins")
