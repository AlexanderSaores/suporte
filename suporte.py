from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    message = 'Olá, ' + update.message.from_user.first_name + ' nos diga qual o seu problema!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '1125623544:AAEoT8ZS6LIeZzy4hJEc4iGC3FwtLI7F4vo'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == "__main__":
    main()
