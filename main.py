from telegram import Update, Message, User, CallbackQuery,InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler 
import os

TOKEN = os.getenv('TOKENN')
app = ApplicationBuilder().token(TOKEN).build()




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyord = [[InlineKeyboardButton("Assalomu alaykum", url="https://t.me/Dilmurod_Kitob_haqida_blog"), InlineKeyboardButton("Assalomu alaykum2", url="https://t.me/Dilmurod_Kitob_haqida_blog")],
              [InlineKeyboardButton("Assalomu alaykum3", url="https://t.me/Dilmurod_Kitob_haqida_blog")],
              [InlineKeyboardButton("Assalomu alaykum4", url="https://t.me/Dilmurod_Kitob_haqida_blog")]
    ]

    reply_markup = InlineKeyboardMarkup(keyord)
    await update.message.reply_text("Assalomu alaykum!\nBotimizga hush kelibsiz!", reply_markup=reply_markup)

    keyboard = [[KeyboardButton("Assalomu alaykum")],
        [KeyboardButton("Assalomu alaykum2")],
        [KeyboardButton("Assalomu alaykum3")],
        [KeyboardButton("Assalomu alaykum4")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Quyidagi tugmalardan birini tanlang:", reply_markup=reply_markup)

    

app.add_handler(CommandHandler("start", start))
app.run_polling()
