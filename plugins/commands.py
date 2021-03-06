import os
from config import Config
from .fonts import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'Mo_Tech_YT'

    # start text
    text = f"""**πβππππ ! {m.from_user.mention(style='md')}**,

π**π ππ ππ₯πͺπππ€π π½π ππ₯ πΉπ π₯**

`π βππ βπππ‘ ππ π¦ ππ  πΎππ₯ ππ₯πͺπππ€π π½π ππ₯π€. ππ¦π€π₯ ππππ ππ ππ ππ πππ©π₯ πΈππ πππ πππππ.`

**π² πππππ₯πππππ πΉπͺ:** {owner.mention(style='md')}
"""

    buttons = [
        [
            InlineKeyboardButton('π¨βπΌππͺ π½ππ₯πππ£π¨βπΌ', url=f"https://t.me/{owner_username}")
        ],
        [
            InlineKeyboardButton('π€πΉπ π₯ ππ‘πππ₯π', url="t.me/mo_tech_yt"),
            InlineKeyboardButton('ππ ππ¦π‘π‘π π£π₯π', url="https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ")
        ],
        [
            InlineKeyboardButton('π€πΉπ π₯ ππ‘πππ₯π', url="t.me/mo_tech_yt"),
            InlineKeyboardButton('ππ ππ¦π‘π‘π π£π₯π', url="https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ")
        ],
        [
            InlineKeyboardButton('π₯οΈβπ π¨ ππ  ππ€ππ₯οΈ', url="https://youtu.be/9b9uWNyuk9M")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
   
    await bot.send_text(
        chat_id=update.chat.id,
        text=text.format(
                update.owner.username),
        reply_markup=reply_markup,
        parse_mode="html",
    )



@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m):
    buttons = [[
        InlineKeyboardButton('ππ’πππ πππππ', callback_data='style+typewriter'),
        InlineKeyboardButton('ππ¦π₯ππππ', callback_data='style+outline'),
        InlineKeyboardButton('πππ«π’π', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('πΊππππ', callback_data='style+bold_cool'),
        InlineKeyboardButton('πππππ', callback_data='style+cool'),
        InlineKeyboardButton('Sα΄α΄ΚΚ Cα΄α΄s', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('ππΈππΎππ', callback_data='style+script'),
        InlineKeyboardButton('πΌπ¬π»π²πΉπ½', callback_data='style+script_bolt'),
        InlineKeyboardButton('α΅β±βΏΚΈ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('αOα°Iα', callback_data='style+comic'),
        InlineKeyboardButton('π¦π?π»π', callback_data='style+sans'),
        InlineKeyboardButton('πππ£π¨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('ππ’π―π΄', callback_data='style+slant'),
        InlineKeyboardButton('π²πΊππ', callback_data='style+sim'),
        InlineKeyboardButton('βΈοΈβΎοΈβοΈβΈοΈβοΈβΊοΈβοΈ', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('ποΈποΈπ‘οΈποΈποΈποΈπ’οΈ', callback_data='style+circle_dark'),
        InlineKeyboardButton('ππ¬π±π₯π¦π ', callback_data='style+gothic'),
        InlineKeyboardButton('π²πππππ', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('CΝ‘ΝlΝ‘ΝoΝ‘ΝuΝ‘ΝdΝ‘ΝsΝ‘Ν', callback_data='style+cloud'),
        InlineKeyboardButton('HΜΜaΜΜpΜΜpΜΜyΜΜ', callback_data='style+happy'),
        InlineKeyboardButton('SΜΜaΜΜdΜΜ', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('βππ©π₯ β‘οΈ', callback_data="nxt")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_text(
        chat_id=update.chat.id,
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["nxt"]) & filters.private, group=1)
async def nxt(bot, update):
      buttons = [[
            InlineKeyboardButton('πΈβπ΅βπͺβπ¨βπ?βπ¦βπ±β', callback_data='style+special'),
            InlineKeyboardButton('ππππ°ππ΄π', callback_data='style+squares'),
            InlineKeyboardButton('ποΈποΈποΈπ°οΈποΈπ΄οΈποΈ', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('κͺκͺα¦κͺκͺΆκͺα₯΄π²κͺ', callback_data='style+andalucia'),
            InlineKeyboardButton('ηͺεε αε', callback_data='style+manga'),
            InlineKeyboardButton('SΜΎtΜΎiΜΎnΜΎkΜΎyΜΎ', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('BΝ¦Μ₯uΝ¦Μ₯bΝ¦Μ₯bΝ¦Μ₯lΝ¦Μ₯eΝ¦Μ₯sΝ¦Μ₯', callback_data='style+bubbles'),
            InlineKeyboardButton('UΝnΝdΝeΝrΝlΝiΝnΝeΝ', callback_data='style+underline'),
            InlineKeyboardButton('κκκ·κ©κκκ', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('R?a?y?s?', callback_data='style+rays'),
            InlineKeyboardButton('B?i?r?d?s?', callback_data='style+birds'),
            InlineKeyboardButton('SΜΈlΜΈaΜΈsΜΈhΜΈ', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('sβ tβ oβ pβ ', callback_data='style+stop'),
            InlineKeyboardButton('SΝΜΊkΝΜΊyΝΜΊlΝΜΊiΝΜΊnΝΜΊeΝΜΊ', callback_data='style+skyline'),
            InlineKeyboardButton('AΝrΝrΝoΝwΝsΝ', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('αͺαα­αΏα', callback_data='style+qvnes'),
            InlineKeyboardButton('SΜΆtΜΆrΜΆiΜΆkΜΆeΜΆ', callback_data='style+strike'),
            ],[
            InlineKeyboardButton('βοΈBack', callback_data="start"),
            InlineKeyboardButton('Nextβ‘οΈ', callback_data="nxt2")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_text(
        chat_id=update.chat.id,
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m):
    buttons = [[
            InlineKeyboardButton('απ΄ααπααπ»ααπααπααπα', callback_data='style+frozen')
            InlineKeyboardButton('κͺκͺα¦κͺκͺΆκͺα₯΄π²κͺ', callback_data='style+andalucia'),
            InlineKeyboardButton('ηͺεε αε', callback_data='style+manga'),
            ],[
            InlineKeyboardButton('β¬οΈ πΉπππ', callback_data='nxt')
        ]]

        reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_text(
        chat_id=update.chat.id,
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text)
    try:
        await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
    except:
        pass
