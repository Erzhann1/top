
from cgitb import text
import re
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,

)

from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler,
    PicklePersistence,
    Filters,
    MessageHandler,
    updater,
    CallbackQueryHandler
)

from menu import main_menu_keyboard, course_menu_keyboard, eng_menu_keyboard, ger_menu_keyboard, chi_menu_keyboard, kor_menu_keyboard,risa_menu_keyboard, bio_menu_keyboard
from key_button import tele_button, course_menu, eng_menu, ger_menu, kor_menu, chi_menu, bio_menu, risa_menu
from bot import TOKEN


def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEEPwNiOwMm--NQH_mjD5GjbkgZPVAmDgACNhYAAlxA2EvbRm7S3ZV6DSME'
    )
    update.message.reply_text(
        "Добро пожаловать, {username}. Выберите опцию: ".format(
        username = update.effective_user.first_name\
            if update.effective_user.first_name is not None \
                else update.effective_user.username
    ),
    reply_markup=main_menu_keyboard()


    )

BACK1 = r"(?=("+(eng_menu[2]) + r"))"




COURSE_REGEX1 = r"(?=("+(tele_button[0]) + r"))"

ENGLISH = r"(?=("+(course_menu[0]) + r"))"

GERMAN = r"(?=("+(course_menu[1]) + r"))"

KOREAN = r"(?=("+(course_menu[2]) + r"))"

CHINESE = r"(?=("+(course_menu[3]) + r"))"

BACK_REGEX = r"(?=("+(course_menu[6]) + r"))"

HIMIA = r"(?=("+(course_menu[4]) + r"))"

RISOVANIE = r"(?=("+(course_menu[5]) + r"))"

AMERICAN = r"(?=("+(eng_menu[0]) + r"))"

LONDON = r"(?=("+(eng_menu[1]) + r"))"

IWEX = r"(?=("+(ger_menu[0]) + r"))"

BOTO = r"(?=("+(ger_menu[1]) + r"))"

CREATORIAK = r"(?=("+(kor_menu[0]) + r"))"

GEC = r"(?=("+(kor_menu[1]) + r"))"

CREATORIAA = r"(?=("+(chi_menu[0]) + r"))"

ALK = r"(?=("+(chi_menu[1]) + r"))"

KELECHEK = r"(?=("+(bio_menu[0]) + r"))"

OWL = r"(?=("+(bio_menu[1]) + r"))"

SCETCH = r"(?=("+(risa_menu[0]) + r"))"

ART = r"(?=("+(risa_menu[1]) + r"))"


def receive_course_menu(update: Update, context: CallbackContext):
    info = re.match(COURSE_REGEX1, update.message.text)
    update.message.reply_text(
        "Выберите курс",
        reply_markup=course_menu_keyboard()
    )

# def def_back_inline(update: Update, context: CallbackContext):
#     info = re.match(BACK_REGEX, update.message.text)
#     update.message.reply_text(
#         "вы вернулись назад",
#          reply_markup=main_menu_keyboard()
#     )

# def deff_back_inline(update: Update, context: CallbackContext):
#     info = re.match(BACK_REGEXS, update.message.text)
#     update.message.reply_text(
#         "вы вернулись назад",
#          reply_markup=main_menu_keyboard()
#     )

# def back_inline(update: Update, context: CallbackContext):
#     info = re.match(BACK1, update.message.text)
#     update.message.reply_text(
#         "вы вернулись назад",
#          reply_markup=course_menu_keyboard()
#     )


def english_menu(update: Update, context: CallbackContext):
    info = re.match(ENGLISH, update.message.text)
    update.message.reply_text(
        " Выберите курс: ",
        reply_markup=eng_menu_keyboard()
    )

def nemec_menu(update: Update, context: CallbackContext):
    info = re.match(GERMAN, update.message.text)
    update.message.reply_text(
        " Выберите курс: ",
        reply_markup=ger_menu_keyboard()
    )

def korea_menu(update: Update, context: CallbackContext):
    info = re.match(KOREAN, update.message.text)
    update.message.reply_text(
        " Выберите курс: ",
        reply_markup=kor_menu_keyboard()
    )
def chinese_menu(update: Update, context: CallbackContext):
    info = re.match(CHINESE, update.message.text)
    update.message.reply_text(
        " Выберите курс: ",
        reply_markup=chi_menu_keyboard()
    )

def bios_menu(update: Update, context: CallbackContext):
    info = re.match(HIMIA, update.message.text)
    update.message.reply_text(
        " Выберите курс: ",
        reply_markup=bio_menu_keyboard()
    )

def risav_menu(update: Update, context: CallbackContext):
    info = re.match(RISOVANIE, update.message.text)
    update.message.reply_text(
        " Выберите курс: ",
        reply_markup=risa_menu_keyboard()
    )



# def english_inline_menu(update: Update, context: CallbackContext):
#     info = re.match(AMERICAN, update.message.text)
#     keyboard = [
#         [InlineKeyboardButton("Контакты", callback_data='kontakts_fot')],
#         [InlineKeyboardButton("Тарифы", callback_data='price_fot')],
#         [InlineKeyboardButton("Локация", callback_data='lokation_fot')],
#     ]
#     reply_markup1 = InlineKeyboardMarkup(keyboard)
    

def american1_menu(update: Update, context: CallbackContext):
    info = re.match(AMERICAN, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_ame')],
        [InlineKeyboardButton("Тарифы", callback_data='price_ame')],
        [InlineKeyboardButton("Локация", callback_data='lokation_ame')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )

def london_menu(update: Update, context: CallbackContext):
    info = re.match(LONDON, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_lon')],
        [InlineKeyboardButton("Тарифы", callback_data='price_lon')],
        [InlineKeyboardButton("Локация", callback_data='lokation_lon')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )

def iwex_menu(update: Update, context: CallbackContext):
    info = re.match(IWEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_iwe')],
        [InlineKeyboardButton("Тарифы", callback_data='price_iwe')],
        [InlineKeyboardButton("Локация", callback_data='lokation_iwe')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )

def boto_menu(update: Update, context: CallbackContext):
    info = re.match(BOTO, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_bot')],
        [InlineKeyboardButton("Тарифы", callback_data='price_bot')],
        [InlineKeyboardButton("Локация", callback_data='lokation_bot')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )

def craetoriak_menu(update: Update, context: CallbackContext):
    info = re.match(CREATORIAK, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_crek')],
        [InlineKeyboardButton("Тарифы", callback_data='price_crek')],
        [InlineKeyboardButton("Локация", callback_data='lokation_crek')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )

def gec_menu(update: Update, context: CallbackContext):
    info = re.match(GEC, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_gec')],
        [InlineKeyboardButton("Тарифы", callback_data='price_gec')],
        [InlineKeyboardButton("Локация", callback_data='lokation_gec')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )

def creatoriaa_menu(update: Update, context: CallbackContext):
    info = re.match(CREATORIAA, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_cre')],
        [InlineKeyboardButton("Тарифы", callback_data='price_cre')],
        [InlineKeyboardButton("Локация", callback_data='lokation_cre')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )
    
def alk_menu(update: Update, context: CallbackContext):
    info = re.match(ALK, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_alk')],
        [InlineKeyboardButton("Тарифы", callback_data='price_alk')],
        [InlineKeyboardButton("Локация", callback_data='lokation_alk')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )


def kelechek_menu(update: Update, context: CallbackContext):
    info = re.match(KELECHEK, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_kel')],
        [InlineKeyboardButton("Тарифы", callback_data='price_kel')],
        [InlineKeyboardButton("Локация", callback_data='lokation_kel')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )

def scetch_menu(update: Update, context: CallbackContext):
    info = re.match(SCETCH, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_sce')],
        [InlineKeyboardButton("Тарифы", callback_data='price_sce')],
        [InlineKeyboardButton("Локация", callback_data='lokation_sce')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )

def art_menu(update: Update, context: CallbackContext):
    info = re.match(ART, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_art')],
        [InlineKeyboardButton("Тарифы", callback_data='price_art')],
        [InlineKeyboardButton("Локация", callback_data='lokation_art')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        " Выберите интересуещее вам место: ",
        reply_markup=reply_markup1
    )



def inline_buttons(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts')],
        [InlineKeyboardButton("Тарифы", callback_data='price')],
        [InlineKeyboardButton("Локация", callback_data='lokation')],
    ]
    reply_markup=InlineKeyboardMarkup(keyboard)

    keyboard1 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_ame')],
        [InlineKeyboardButton("Тарифы", callback_data='price_ame')],
        [InlineKeyboardButton("Локация", callback_data='lokation_ame')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard1)


    keyboard2 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_lon')],
        [InlineKeyboardButton("Тарифы", callback_data='price_lon')],
        [InlineKeyboardButton("Локация", callback_data='lokation_lon')],
    ]
    reply_markup2 = InlineKeyboardMarkup(keyboard2)

    keyboard3 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_iwe')],
        [InlineKeyboardButton("Тарифы", callback_data='price_iwe')],
        [InlineKeyboardButton("Локация", callback_data='lokation_iwe')],
    ]
    reply_markup3 = InlineKeyboardMarkup(keyboard3)

    keyboard4 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_bot')],
        [InlineKeyboardButton("Тарифы", callback_data='price_bot')],
        [InlineKeyboardButton("Локация", callback_data='lokation_bot')],
    ]
    reply_markup4 = InlineKeyboardMarkup(keyboard4)

    keyboard5 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_crek')],
        [InlineKeyboardButton("Тарифы", callback_data='price_crek')],
        [InlineKeyboardButton("Локация", callback_data='lokation_crek')],
    ]
    reply_markup5 = InlineKeyboardMarkup(keyboard5)

    keyboard6 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_gec')],
        [InlineKeyboardButton("Тарифы", callback_data='price_gec')],
        [InlineKeyboardButton("Локация", callback_data='lokation_gec')],
    ]
    reply_markup6 = InlineKeyboardMarkup(keyboard6)

    keyboard7 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_cre')],
        [InlineKeyboardButton("Тарифы", callback_data='price_cre')],
        [InlineKeyboardButton("Локация", callback_data='lokation_cre')],
    ]
    reply_markup7 = InlineKeyboardMarkup(keyboard7)

    keyboard8 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_alk')],
        [InlineKeyboardButton("Тарифы", callback_data='price_alk')],
        [InlineKeyboardButton("Локация", callback_data='lokation_alk')],
    ]
    reply_markup8 = InlineKeyboardMarkup(keyboard8)

    keyboard9 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_kel')],
        [InlineKeyboardButton("Тарифы", callback_data='price_kel')],
        [InlineKeyboardButton("Локация", callback_data='lokation_kel')],
    ]
    reply_markup9 = InlineKeyboardMarkup(keyboard9)

    keyboard10 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_sce')],
        [InlineKeyboardButton("Тарифы", callback_data='price_sce')],
        [InlineKeyboardButton("Локация", callback_data='lokation_sce')],
    ]
    reply_markup10 = InlineKeyboardMarkup(keyboard10)

    keyboard11 = [
        [InlineKeyboardButton("Контакты", callback_data='kontakts_art')],
        [InlineKeyboardButton("Тарифы", callback_data='price_art')],
        [InlineKeyboardButton("Локация", callback_data='lokation_art')],
    ]
    reply_markup11 = InlineKeyboardMarkup(keyboard11)



    query = update.callback_query
    query.answer()

 

    if query.data =='kontakts_ame':
         query.edit_message_text(
             text="""
📞 0706 54 56 57
☎️ 0312 54 56 57
            """,
            reply_markup = reply_markup1   
        )
    
    if query.data =='price_ame':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 2500 сом.
Стоимость индивидуальных курсов составляет 5500 сом в месяц.
            """,
        reply_markup=reply_markup1
        )
    if query.data =='lokation_ame':
        query.message.reply_location(
           longitude=74.58836182184768,
           latitude=42.843167512873734
        )
###############################################################################
    if query.data =='kontakts_lon':
        query.edit_message_text(
            text="""
📞 0706 38 39 09
☎️ 0312 54 44 74
            """,
            reply_markup = reply_markup2   
        )
    
    if query.data =='price_lon':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 2500,
для начинающих 1600 сом в месяц
            """,
        reply_markup=reply_markup2
        )
    if query.data =='lokation_lon':
        query.message.reply_location(
           longitude=74.58836182184768,
           latitude=42.847336890061314
        )

    if query.data =='kontakts_iwe':
        query.edit_message_text(
            text="""
📞 0771 33 70 00
☎️ 0556 33 70 00
            """,
            reply_markup = reply_markup3  
        )
    
    if query.data =='price_iwe':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 2500 сом,
Стоимость индивидуальных занятий 5500 сом.
            """,
        reply_markup=reply_markup3
        )
    if query.data =='location_iwe':
        query.message.reply_location(
           longitude=74.56634779596874,
           latitude=42.83606815916657
        )

    if query.data =='kontakts_bot':
        query.edit_message_text(
            text="""
📞 0706 01 10 66
☎️ 0702 18 00 80
            """,
            reply_markup = reply_markup4
        )
    
    if query.data =='price_bot':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 3000 сом,
Стоимость Talcking club в месяц составляет 2500 сом.
            """,
        reply_markup=reply_markup4
        )
    if query.data =='lokation_bot':
        query.message.reply_location(
           longitude=74.60793794252645, 
           latitude=42.83502047633171
        )

    if query.data =='kontakts_crek':
        query.edit_message_text(
            text="""
📞  0509 50 95 10
            """,
            reply_markup = reply_markup5
        )
    
    if query.data =='price_crek':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 3000 сом
            """,
        reply_markup=reply_markup5
        )
    if query.data =='lokation_crek':
        query.message.reply_location(
           longitude=74.58408294056773,
           latitude=42.8753435379175
        )

    if query.data =='kontakts_gec':
        query.edit_message_text(
            text="""
📞  0706 16 01 62
            """,
            reply_markup = reply_markup6
        )
    
    if query.data =='price_gec':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 2800 сом
            """,
        reply_markup=reply_markup6
        )
    if query.data =='lokation_gec':
        query.message.reply_location(
           longitude=74.58408294056773,
           latitude=42.8753435379175
        )

    if query.data =='kontakts_cre':
        query.edit_message_text(
            text="""
📞  0509 50 95 10
            """,
            reply_markup = reply_markup7   
        )
    
    if query.data =='price_cre':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 3000 сом
            """,
        reply_markup=reply_markup7
        )
    if query.data =='lokation_cre':
        query.message.reply_location(
           longitude=74.58408294056773,
           latitude=42.8753435379175
        )

    if query.data =='kontakts_alk':
        query.edit_message_text(
            text="""
📞  0509 50 95 10
            """,
            reply_markup = reply_markup8  
        )
    
    if query.data =='price_alk':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 3000 сом
            """,
        reply_markup=reply_markup8
        )
    if query.data =='lokation_alk':
        query.message.reply_location(
           longitude=74.58408294056773,
           latitude=42.8753435379175
        )

    if query.data =='kontakts_kel':
        query.edit_message_text(
            text="""
📞  0508 81 92 61
            """,
            reply_markup = reply_markup9
        )
    
    if query.data =='price_kel':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 1500 сом
            """,
        reply_markup=reply_markup9
        )
    if query.data =='lokation_kel':
        query.message.reply_location(
           longitude=74.61183655601936,
           latitude=42.87098201612602
        )

    if query.data =='kontakts_sce':
        query.edit_message_text(
            text="""
📞  0508 73 23 32 
            """,
            reply_markup = reply_markup10  
        )
    
    if query.data =='price_sce':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 2200 сом
            """,
        reply_markup=reply_markup10
        )
    if query.data =='lokation_sce':
        query.message.reply_location(
           longitude=74.61183655601936,
           latitude=42.87098201612602
        )

    if query.data =='kontakts_art':
        query.edit_message_text(
            text="""
☎️  0779 900 907
📞  0755 312 311
            """,
            reply_markup = reply_markup11
        )
    
    if query.data =='price_art':
        query.edit_message_text(
            text="""
Стоимость курсов в месяц составляет 2700 сом
            """,
        reply_markup=reply_markup11
        )
    if query.data =='lokation_art':
        query.message.reply_location(
           longitude=74.59177255601935,
           latitude=42.874284254831586
        )



   

    

    
   
    





updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_REGEX1),
    receive_course_menu

))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ENGLISH),
    english_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(GERMAN),
    nemec_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KOREAN),
    korea_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CHINESE),
    chinese_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HIMIA),
    bios_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RISOVANIE),
    risav_menu

)) 
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(AMERICAN),
    american1_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LONDON),
    london_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(IWEX),
    iwex_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BOTO),
    boto_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CREATORIAK),
    craetoriak_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(GEC),
    gec_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CREATORIAA),
    creatoriaa_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ALK),
    alk_menu

))   
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KELECHEK),
    kelechek_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(SCETCH),
    scetch_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ART),
    art_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_REGEX),
    receive_course_menu

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK1),
    receive_course_menu

))    


updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))

updater.start_polling()
updater.idle()
