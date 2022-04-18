import telegram
from key_button import tele_button, course_menu, eng_menu, ger_menu, kor_menu, chi_menu,bio_menu,risa_menu

def main_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(tele_button[0])
    ],
    
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def course_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(course_menu[0]),
        telegram.KeyboardButton(course_menu[1])
    
    ],
    [    
        telegram.KeyboardButton(course_menu[2]),
        telegram.KeyboardButton(course_menu[3])

    ],       
    [
        telegram.KeyboardButton(course_menu[4]),
        telegram.KeyboardButton(course_menu[5])
    
    ],
    [    
        telegram.KeyboardButton(course_menu[6]),

    ],       
         
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def eng_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(eng_menu[0]),
    
    ],
    [    
        telegram.KeyboardButton(eng_menu[1]),
    ],
    [    
        telegram.KeyboardButton(eng_menu[2]),

    ],       
         
         
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def ger_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(ger_menu[0]),
    
    ],
    [    
        telegram.KeyboardButton(ger_menu[1]),
    ],
    [    
        telegram.KeyboardButton(ger_menu[2]),

    ],       
         
         
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def kor_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(kor_menu[0]),
    
    ],
    [    
        telegram.KeyboardButton(kor_menu[1]),
    ],
    [    
        telegram.KeyboardButton(kor_menu[2]),

    ],       
         
         
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def chi_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(chi_menu[0]),
    
    ],
    [    
        telegram.KeyboardButton(chi_menu[1]),
    ],
    [    
        telegram.KeyboardButton(chi_menu[2]),

    ],

    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def bio_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(bio_menu[0]),
    
    ],
    [    
        telegram.KeyboardButton(bio_menu[1]),

    ]])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def risa_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(risa_menu[0]),
    
    ],
    [    
        telegram.KeyboardButton(risa_menu[1]),
    ],
    [    
        telegram.KeyboardButton(risa_menu[2]),

    ]])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )







