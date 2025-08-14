from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import wikipedia

# Set the language (optional)
wikipedia.set_lang("en")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your Wikipedia Bot. Just ask me anything!")

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    try:
        summary = wikipedia.summary(query, sentences=2)
        await update.message.reply_text(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        await update.message.reply_text(f"Too many results. Try being more specific.\nExamples: {e.options[:5]}")
    except wikipedia.exceptions.PageError:
        await update.message.reply_text("I couldn’t find anything. Try a different query.")
    except Exception as e:
        await update.message.reply_text("Something went wrong. Try again later.")

# Main function
def main():
    bot_token = "enter your token name"
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
