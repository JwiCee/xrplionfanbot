import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Buy Fan Card", callback_data='buy')],
        [InlineKeyboardButton("Learn More", url="https://t.me/XRPLionFanBot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🦁 Welcome to the *XRP Lion Fan Club*!\n\nChoose an option below to begin your journey.",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'buy':
        await query.edit_message_text("💳 Fan Cards:\n1. Guardian Card – $375\n2. Revelation Card – $699\n3. Anointed Lion Card – $988\n\nDM @YourUsername to purchase or use Telegram Payments!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

if __name__ == '__main__':
    app.run_polling()
