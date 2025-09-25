import base64
import contextlib
from asyncio import sleep

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from . import zedub

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper import broadcast_sql as sql
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البوت"
LOGS = logging.getLogger(__name__)

ZED_BLACKLIST = [
    -1002220862939,
    -1002220862939,
    ]

DEVZ = [
    5571722913,
    6669024587,
]
#

ZelzalPRO_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامـر الاذا؏ـــة](t.me/YamenThon) 𓆪\n\n"
    "**⎞𝟏⎝** `.للجروبات`  / `.للمجموعات`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــه او وسـائــط تحتهــا نــص**\n"
    "**- لـ اذاعـة رسـالة او ميديـا لكـل المجموعـات اللي انت موجود فيهـا . .**\n\n\n"
    "**⎞𝟐⎝** `.للخاص`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــه او وسـائــط تحتهــا نــص**\n"
    "**- لـ اذاعـة رسـالة او ميديـا لكـل الاشخـاص اللي موجـودين عنـدك خـاص . .**\n\n\n"
    "**⎞𝟑⎝** `.خاص`\n"
    "**الامـر + معرف الشخص + الرسـاله . .**\n"
    " **- ارسـال رسـاله الى الشخص المحدد بدون الدخول للخاص وقراءة الرسـائل . .**\n\n\n"
    "**⎞4⎝** `.للكل`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــه او وسـائــط تحتهــا نــص**\n"
    " **- ارسـال رسـاله اذاعـة الى جميـع اعضـاء مجموعـة محددة .. قم باستخـدام الامـر داخـل المجموعـة . .**\n\n"
    "**⎞5⎝** `.زاجل`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــه او وسـائــط تحتهــا نــص**\n"
    " **- ارسـال رسـاله اذاعـة الى اشخاص محددة 🕊. .**\n\n"
    "\n 𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉](t.me/YamenThon) 𓆪"
)


# Copyright (C)2023 refz . All Rights Reserved
@zedub.zed_cmd(pattern="الاذاعه")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalPRO_cmd)


@zedub.zed_cmd(pattern=f"للجروبات(?: |$)(.*)")
async def gcast(event):
    yamen = event.pattern_match.group(1)
    if yamen:  
        await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        zelzal = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎جـاري الاذاعـه في المجموعـات ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if zelzal.text:  
                    try:
                        await borg.send_message(chat, zelzal, link_preview=False)
                        done += 1
                    except BaseException:
                        er += 1
                else:
                    try:  
                        await borg.send_file(
                            chat,
                            zelzal,
                            caption=zelzal.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                er += 1
    await zzz.edit(
        f"**    ⃟⁞⃟⟢ ╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من المجموعـات** \n**    ⃟⁞⃟⟢ ╎خطـأ في الارسـال الـى ** `{er}` **من المجموعـات**"
    )

@zedub.zed_cmd(pattern=f"للمجموعات(?: |$)(.*)")
async def gcast(event):
    yamen = event.pattern_match.group(1)
    if yamen: 
        await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        zelzal = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎جـاري الاذاعـه في المجموعـات ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if zelzal.text:  
                    try:
                        await borg.send_message(chat, zelzal, link_preview=False)
                        done += 1
                    except BaseException:
                        er += 1
                else:
                    try:  
                        await borg.send_file(
                            chat,
                            zelzal,
                            caption=zelzal.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                return
    await zzz.edit(
        f"**    ⃟⁞⃟⟢ ╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من المجموعـات ، خطـأ في الارسـال الـى ** `{er}` **من المجموعـات**"
    )
    
@zedub.zed_cmd(pattern=f"للخاص(?: |$)(.*)")
async def gucast(event):
    yamen = event.pattern_match.group(1)
    if yamen: 
        await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        zelzal = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**    ⃟⁞⃟⟢ ╎جـاري الاذاعـه في الخـاص ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if zelzal.text:  
                    try:
                        await borg.send_message(chat, zelzal, link_preview=False)
                        done += 1
                    except BaseException:
                        return
                else:
                    try:  
                        await borg.send_file(
                            chat,
                            zelzal,
                            caption=zelzal.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                return
    await zzz.edit(
        f"**    ⃟⁞⃟⟢ ╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من الخـاص**\n**    ⃟⁞⃟⟢ ╎خطـأ في الارسـال الـى ** `{er}` **من الخـاص**"
    )
    

@zedub.zed_cmd(pattern="خاص ?(.*)")
async def pmto(event):
    r = event.pattern_match.group(1)
    p = r.split(" ")
    chat_id = p[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    zelzal = ""
    for i in p[1:]:
        zelzal += i + " "
    if zelzal == "":
        return
    try:
        await zedub.send_message(chat_id, zelzal)
        await event.edit("**    ⃟⁞⃟⟢ ╎تـم ارسال الرسـالة بنجـاح ✓**\n**    ⃟⁞⃟⟢ ╎بـدون الدخـول للخـاص**")
    except BaseException:
        await event.edit("**    ⃟⁞⃟⟢ ╎اووبس .. لقـد حدث خطـأ مـا .. اعـد المحـاوله**")

