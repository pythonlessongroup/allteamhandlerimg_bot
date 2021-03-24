from telebot import types

menu = types.ReplyKeyboardMarkup()
btn_1 = types.KeyboardButton(text='/start')
btn_2 = types.KeyboardButton(text='/help')

menu.add(btn_1, btn_2)

inline_menu = types.InlineKeyboardMarkup(row_width=2)
w = types.InlineKeyboardButton(text='Stop', callback_data='stop')
s = types.InlineKeyboardButton(text='Next', callback_data='next')
d = types.InlineKeyboardButton(text='Random', callback_data='next')
inline_menu.add(w, s, d)