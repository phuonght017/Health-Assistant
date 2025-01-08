import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Command Handlers
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I am your Health Assistant. I can help you track your health, suggest workouts, and track nutrition. Type /help to see available commands.")

async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("""
    Here are the available commands:
    - /track_health: Track your health data (weight, steps, exercise)
    - /workout: Get personalized workout suggestions
    - /nutrition: Log your meals and track calories
    """)

async def track_health(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Please provide your health data in the format:\nweight:<your weight> steps:<your steps> exercise:<exercise duration (in minutes)>")

async def workout(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Based on your goals, I suggest the following workouts:\n- Cardio: 30 mins\n- Strength training: 20 mins\n- Flexibility: 10 mins")

async def nutrition(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Please provide the food you ate and the quantity (in grams), e.g., 'apple: 100g'.")


def main():
    application = ApplicationBuilder().token("7222779491:AAEd1jB3sbU29vShNM07lg1Z1PhZ0xwVrYg").build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("track_health", track_health))
    application.add_handler(CommandHandler("workout", workout))
    application.add_handler(CommandHandler("nutrition", nutrition))

    # Run bot
    application.run_polling()

if __name__ == "__main__":
    main()



