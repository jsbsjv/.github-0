# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="•Del•", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="ll", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
            ],
            [
            InlineKeyboardButton("⦓ Source VebThon ⦔", url=f"https://t.me/WWEEHHHH"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="•Add BoT tO Group•",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="•Operating Orders•", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="⦓ Source VebThon ⦔", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="⦓ Support Group ⦔", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="•Source Developer•", url="https://t.me/WWEEHHHH"
        ),
        InlineKeyboardButton(text="•BoT Owner•", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="•Add BoT tO Group•",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="⦓ Source VebThon ⦔", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="⦓ Support Group ⦔", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="•Source Developer•", url="https://t.me/WWEEHHHH"
        ),
        InlineKeyboardButton(text="•BoT Owner•", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="•Operating Orders•",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="•Developer Orders•", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="•Owner's Orders•", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="•Back•", callback_data="fallen_home"),
        InlineKeyboardButton(text="•Del•", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="⦓ Support Group ⦔", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="•Back•", callback_data="fallen_help"),
        InlineKeyboardButton(text="•Del•", callback_data="close"),
    ],
]
