from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

til = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 O'zbekcha"),
            KeyboardButton("🇷🇺 Russcha")

        ],
    ],
    resize_keyboard=True
)

raqam = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Telefon raqamni yuborish", request_contact=True)
        ],
    ],
    resize_keyboard=True
)

joylashuv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📍 Joylashuvni yuborish", request_location=True)
        ],
    ],
    resize_keyboard=True
)

pastki_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Buyurtma berish")
        ],
        [
            KeyboardButton("Sozlamalar"),
            KeyboardButton("Biz bilan aloqa")
        ],
    ],
    resize_keyboard=True
)


# bosh menu
bosh_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Lavash", callback_data='lavash'),
            InlineKeyboardButton(text="Xod-Dog", callback_data='xot-dog')
        ],
        [
            InlineKeyboardButton(text="Lavash", callback_data='lavash'),
            InlineKeyboardButton(text="Xod-Dog", callback_data='xot-dog')
        ],
        [
            InlineKeyboardButton(text="Lavash", callback_data='lavash'),
            InlineKeyboardButton(text="Xod-Dog", callback_data='xot-dog')
        ],
    ]
)

# lavash menu
lavash_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mol gushli", callback_data='molgush'),
            InlineKeyboardButton(text="Tovuqli ", callback_data='tovuqgush')
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data='back1'),
            
        ],
       
    ]
)

# lavash_menu_mini_class
lavash_menu_mini_class = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini", callback_data='min'),
            InlineKeyboardButton(text="Classik ", callback_data='cls')
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data='back2'),
            
        ],
       
    ]
)



# lavash_menu_mini_class_raqamlar
lavash_menu_mini_class_raqamlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data='1'),
            InlineKeyboardButton(text="2 ", callback_data='1'),
            InlineKeyboardButton(text="3", callback_data='1'),
        ],
         [
            InlineKeyboardButton(text="4", callback_data='1'),
            InlineKeyboardButton(text="5 ", callback_data='1'),
            InlineKeyboardButton(text="6", callback_data='1'),
        ],
         [
            InlineKeyboardButton(text="7", callback_data='1'),
            InlineKeyboardButton(text="8", callback_data='1'),
            InlineKeyboardButton(text="9", callback_data='1'),
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data='back2'),
            
        ],
       
    ]
)

