» /play +「اسم الأغنية / رابط」لتشغيل اغنيه في المحادثه الصوتيه
» /vplay +「اسم الفيديو / رابط 」 لتشغيل الفيديو داخل المكالمة
» /vstream 「رابط」 تشغيل فيديو مباشر من اليوتيوب
» /playlist 「تظهر لك قائمة التشغيل」
» /end「لإنهاء الموسيقى / الفيديو في الكول」
» /song + 「الاسم تنزيل صوت من youtube」
»/vsong + 「الاسم  تنزيل فيديو من youtube」
» /skip「للتخطي إلى التالي」
» /ping 「إظهار حالة البوت بينغ」
» /uptime 「لعرض مده التشغيل للبوت」
» /alive「اظهار معلومات البوت(في المجموعه)」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("اوامر الادمنيه")
    await query.edit_message_text(
        f"""🏮 هنا أوامر الادمنيه:

» /pause 「ايقاف التشغيل موقتآ」
» /resume 「استئناف التشغيل」
» /stop「لإيقاف التشغيل」
» /vmute 「لكتم البوت」
» /vunmute 「لرفع الكتم عن البوت」
» /volume 「ضبط مستوئ الصوت」
» /reload「لتحديث البوت و قائمة المشرفين」
» /userbotjoin「لاستدعاء الحساب المساعد」
» /userbotleave「لطرد الحساب المساعد」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("اوامر المطور")
    await query.edit_message_text(
        f"""🏮 هنا اوامر المطور:

» /rmw「لحذف جميع الملفات 」
» /rmd「حذف جميع الملفات المحمله」
» /sysinfo「لمعرفه معلومات السيرفر」
» /update「لتحديث بوتك لاخر نسخه」
» /restart「اعاده تشغيل البوت」
» /leaveall「خروج الحساب المساعد من جميع المجموعات」

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ الإعدادات {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
