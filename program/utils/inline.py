""" inline section button """


from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="▢", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="II", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'set_resume | {user_id}'),
      InlineKeyboardButton(text="‣‣I", callback_data=f'set_skip | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="Grubumuz", url=f"https://t.me/sohbet_muhabbet_tanisma_ark"),
      InlineKeyboardButton(text="Kanalımız", url=f"https://t.me/httpsiir_Edebiyat_vefa"),
    ],
    [
      InlineKeyboardButton(text="•Kapat", callback_data="set_close"),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="▢", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="II", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'set_resume | {user_id}'),
      InlineKeyboardButton(text="‣‣I", callback_data=f'set_skip | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔙 Geri Dön", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Kapat", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Geri Dön", callback_data="stream_menu_panel"
      )
    ]
  ]
)
