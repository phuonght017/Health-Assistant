# Store user health data (you can replace this with a database for persistence)
user_health_data = {}

def track_health(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    # Parse user input
    try:
        data = update.message.text.split()
        weight = data[0].split(":")[1]
        steps = data[1].split(":")[1]
        exercise = data[2].split(":")[1]

        # Save data to dictionary (you can replace this with a file or database)
        user_health_data[user_id] = {
            "weight": weight,
            "steps": steps,
            "exercise": exercise
        }

        update.message.reply_text(f"Your health data has been tracked!\nWeight: {weight}kg\nSteps: {steps} steps\nExercise: {exercise} minutes")

    except IndexError:
        update.message.reply_text("Invalid format. Please use the format: weight:<your weight> steps:<your steps> exercise:<exercise duration (in minutes)>")
