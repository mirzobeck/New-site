from inspect import Traceback
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from telegram import CallbackQuery
from handlers.users.stat import lst
import re
from handlers.users.button import asos, tel, menu, asosiy_menu, not_ariza, kitob_sinf, sinf_1, ortga_kitob1, sinf_5, ortga_kitob5, sinf_6, ortga_kitob6, sinf_7, ortga_kitob7, sinf_8, ortga_kitob8, sinf_9, ortga_kitob9, tenglama, wikiped,  tuturia, r, t, nwb, soroq, soroqq, nwb2
import wikipedia
import asyncio
from loader import dp, db ,bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .stat import post



wikipedia.set_lang('uz')

@dp.message_handler(commands='start')
async def start(massage: types.Message):
    frst = massage.from_user.first_name
    user = massage.from_user.username
    idd = massage.from_user.id
    await massage.answer(f"Salom {frst}. Bot'ga xush kelibsiz!\nKerakli bo'limni tanlang: ", reply_markup=menu)


    
    # await massage.answer(f"Salom {frst}, bo'tdan foydalanish uchun ro'yxatdan o'ting! ", reply_markup=asos)



@dp.message_handler(state=lst.telefon)
async def get_num(message: types.Message, state: FSMContext):
    await message.reply("'Raqamni yuborish' tugmasini bosing 👇🏻", reply_markup=tel)


@dp.callback_query_handler(text='report')
async def sorov(call: types.CallbackQuery):
    await call.message.edit_text("Aniq shikoyat qilmoqchimisiz?\nAgar ha tugmasini bossangiz shikoyat qilmaguncha ortga qayta olmaysiz!"), await call.message.edit_reply_markup(reply_markup=not_ariza)
    await call.answer(cache_time=3)


@dp.callback_query_handler(text="yes")
async def new(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Shikoyat qilish uchun bizga aniq ma'lumot bering! ", reply_markup=asos)


@dp.message_handler(text="📝 Ma'lumot berish")
async def start(massage: types.Message):
    await massage.answer("Iltimos ismingizni kiriting:")
    await lst.ism.set()


@dp.message_handler(state=lst.ism)
async def get_ism(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data(
        {'ism': ism}
    )
    await message.answer("Familiyangizni kiriting:")
    await lst.next()


@dp.message_handler(state=lst.familiya)
async def get_fam(message: types.Message, state: FSMContext):
    familiya = message.text
    await  state.update_data(
        {'familiya': familiya}
    )
    await message.answer("Telefon raqamingizni yuboring:", reply_markup=tel)
    await lst.next()


num = "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"
@dp.message_handler(content_types=['contact'],state=lst.telefon)
async def get_num(message: types.Message, state: FSMContext):
    number = message.contact['phone_number']
    try:
        if re.match(num, number) or re.match(num, f"+{number}"):
            await state.update_data(
                {'Telefon raqam' : number}
            )
            await message.answer("Ma'lumotlaringiz olindi ✅")
            await message.answer("Shikoyatingizni yozing:")
            await lst.next()
        else:
            await message.answer(f"Bu bot faqat O'zbekiston raqamlarida ishlaydi.")
    except:
        await message.answer("Uzr bizda xatolik yuz berdi, qayta uruning!")



@dp.message_handler(content_types=['photo'],state=lst.telefon)
async def get_num(message: types.Message, state: FSMContext):
    await message.answer("Rasm emas telefon raqmingizni yuboring!")


@dp.message_handler(state=lst.shikoyat)
async def shik(message: types.Message, state: FSMContext):
    shikoyat = message.text
    await state.update_data(
        {'shikoyat':shikoyat}
    )
    data = await state.get_data()
    fname = data.get("ism")
    lname = data.get('familiya')
    tel = data.get('Telefon raqam')
    report = data.get('shikoyat')
    frst = message.from_user.first_name
    usr = message.from_user.username
    idd = message.from_user.id
    if usr == None:
        await bot.send_message(chat_id='1361526026',text=f"Malumotlar:\n    Firstname: {frst}\n    Id: {idd}\n    Ism: {fname}\n    Familiya: {lname}\n    Telefon: {tel}\nShikoyati:\n    {report}")
    elif usr != None:
        await bot.send_message(chat_id='1361526026',text=f"Malumotlar:\n    Username: @{usr}\n    Id: {idd}\n    Ism: {fname}\n    Familiya: {lname}\n    Telefon: {tel}\nShikoyati:\n    {report}")
    await state.finish()
    await message.answer("Shikoyatingiz qabul qilindi. Biz uni albatta ko'rib chiqamiz!", reply_markup=asosiy_menu)



@dp.callback_query_handler(text=['no','home'])
async def bosh_menu(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli bo'limni tanlang: "), await call.message.edit_reply_markup(reply_markup=menu)
    await call.answer(cache_time=3)


@dp.callback_query_handler(text='books')
async def books_class(call: types.CallbackQuery):
    await call.message.edit_text("Sinfingizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=kitob_sinf)


# 1-sinf
@dp.callback_query_handler(text='1-sinf')
async def books_class(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli faningizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=sinf_1)

@dp.callback_query_handler(text='fan orqa1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.edit_text("Sinfingizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=kitob_sinf)

@dp.callback_query_handler(text='kitob orqa1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli faningizni tanlang 👇🏻 ", reply_markup=sinf_1)


@dp.callback_query_handler(text='kitob home1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli bo'limni tanlang: ", reply_markup=menu)


@dp.callback_query_handler(text="tasviriy san'at1")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/14", caption="1-sinf tasviriy san'at elektron kitobi 📖", reply_markup=ortga_kitob1)


@dp.callback_query_handler(text="tarbiya1")
async def books_class(call: types.CallbackQuery):
    await call.answer("❌ Hozircha bu kitob botimizda yo'q.",show_alert=True)
    # await call.message.answer_document(document="https://t.me/DarsliklarElektron/15", caption="1-sinf tarbiya elektron kitobi 📖", reply_markup=ortga_kitob1)


@dp.callback_query_handler(text="ingliz tili1")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/xabarhabar/46", caption="1-sinf ingliz tili elektron kitobi 📖", reply_markup=ortga_kitob1)


@dp.callback_query_handler(text="jismoniy tarbiya1")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/16", caption="1-sinf jismoniy tarbiya elektron kitobi 📖", reply_markup=ortga_kitob1)


@dp.callback_query_handler(text="matematika1")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/edurtm_uz/8239", caption="1-sinf matematika elektron kitobi 📖", reply_markup=ortga_kitob1)


@dp.callback_query_handler(text="otos1")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/edurtm_uz/8238", caption="1-sinf ona tili va o'qish savodxonligi elektron kitobi 📖", reply_markup=ortga_kitob1)


@dp.callback_query_handler(text="musiqa1")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/edurtm_uz/8241", caption="1-sinf musiqa elektron kitobi 📖", reply_markup=ortga_kitob1)


@dp.callback_query_handler(text="tabiiy fanlar1")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/edurtm_uz/8240", caption="1-sinf musiqa elektron kitobi 📖", reply_markup=ortga_kitob1)


#2-sinf
@dp.callback_query_handler(text='2-sinf')
async def books_class(call: types.CallbackQuery):
    await call.answer("❌ Hozircha 2-sinf elektron darsliklari yo'q", show_alert=True)


#3-sinf
@dp.callback_query_handler(text='3-sinf')
async def books_class(call: types.CallbackQuery):
    await call.answer("❌ Hozircha 3-sinf elektron darsliklari yo'q", show_alert=True)


#4-sinf
@dp.callback_query_handler(text='4-sinf')
async def books_class(call: types.CallbackQuery):
    await call.answer("❌ Hozircha 4-sinf elektron darsliklari yo'q", show_alert=True)


#5-sinf
@dp.callback_query_handler(text='5-sinf')
async def books_class(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli faningizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=sinf_5)


@dp.callback_query_handler(text='fan orqa1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.edit_text("Sinfingizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=kitob_sinf)


@dp.callback_query_handler(text='kitob orqa5')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli faningizni tanlang 👇🏻 ", reply_markup=sinf_5)

@dp.callback_query_handler(text='kitob home1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli bo'limni tanlang: ", reply_markup=menu)


@dp.callback_query_handler(text="tasviriy san'at5")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/114", caption="5-sinf tasviriy san'at elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text="jismoniy tarbiya5")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    # await call.answer("❌ Hozircha bu kitob botimizda yo'q.",show_alert=True)
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/108", caption="5-sinf jismoniy tarbiya elektron kitobi 📖", reply_markup=ortga_kitob5)

@dp.callback_query_handler(text="ingliz tili5")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/106", caption="5-sinf ingliz tili elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text="vatan tuyg'usi5")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/115", caption="5-sinf vatan tuyg'usi elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text="matematika5")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/109", caption="5-sinf matematika elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text="adabiyot5")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/100", caption="5-sinf adabiyot 1 elektron kitobi 📖")
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/99", caption="5-sinf adabiyot 2 elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text="musiqa5")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/111", caption="5-sinf musiqa elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text="botonika5")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/102", caption="5-sinf botonika elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text='informatika5')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/105", caption="5-sinf informatika elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text='geografiya5')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/104", caption="5-sinf geografiya elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text='tarixdan hikoyalar5')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/117", caption="5-sinf tarixdan hikoyalar elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text='texnologiya5')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/119", caption="5-sinf texnologiya elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text='ona tili5')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/113", caption="5-sinf ona tili elektron kitobi 📖", reply_markup=ortga_kitob5)


@dp.callback_query_handler(text='rus tili5')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/118", caption="5-sinf rus tili elektron kitobi 📖", reply_markup=ortga_kitob5)


#6-sinf
@dp.callback_query_handler(text='6-sinf')
async def books_class(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli faningizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=sinf_6)


@dp.callback_query_handler(text='fan orqa1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.edit_text("Sinfingizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=kitob_sinf)

@dp.callback_query_handler(text='kitob orqa6')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli faningizni tanlang 👇🏻 ", reply_markup=sinf_6)

@dp.callback_query_handler(text='kitob home1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli bo'limni tanlang: ", reply_markup=menu)


@dp.callback_query_handler(text="adabiyot6")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/121", caption="6-sinf adabiyot 1 elektron kitobi 📖")
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/122", caption="6-sinf adabiyot 2 elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text='fizika6')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/123", caption="6-sinf fizika elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text="botonika6")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/126", caption="6-sinf botonika elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text='informatika6')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/127", caption="6-sinf informatika elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text='geografiya6')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/128", caption="6-sinf geografiya elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text="ingliz tili6")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/129", caption="6-sinf ingliz tili elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text="matematika6")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/131", caption="6-sinf matematika elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text="musiqa6")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/133", caption="6-sinf musiqa elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text='ona tili6')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/134", caption="6-sinf ona tili elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text='tarix6')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/136", caption="6-sinf tarix elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text='rus tili6')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/137", caption="6-sinf rus tili elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text='texnologiya6')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/138", caption="6-sinf texnologiya elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text="vatan tuyg'u6")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/139", caption="6-sinf vatan tuyg'usi elektron kitobi 📖", reply_markup=ortga_kitob6)


@dp.callback_query_handler(text="tasviriy san'at6")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/140", caption="6-sinf tasviriy san'at elektron kitobi 📖", reply_markup=ortga_kitob6)


#7-sinf
@dp.callback_query_handler(text='7-sinf')
async def books_class(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli faningizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=sinf_7)


@dp.callback_query_handler(text='fan orqa1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.edit_text("Sinfingizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=kitob_sinf)

@dp.callback_query_handler(text='kitob orqa7')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli faningizni tanlang 👇🏻 ", reply_markup=sinf_7)

@dp.callback_query_handler(text='kitob home1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli bo'limni tanlang: ", reply_markup=menu)


@dp.callback_query_handler(text="adabiyot7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/146", caption="7-sinf adabiyot elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text='fizika7')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/149", caption="7-sinf fizika elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="zoologiya7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/164", caption="7-sinf zoologiya elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text='informatika7')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/156", caption="7-sinf informatika elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text='geografiya7')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/148", caption="7-sinf geografiya elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="ingliz tili7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/153", caption="7-sinf ingliz tili elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="algebra7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/147", caption="7-sinf algebra elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="musiqa7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/163", caption="7-sinf musiqa elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text='ona tili7')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/157", caption="7-sinf ona tili elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text='uzb tarix7')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/160", caption="7-sinf O'zbekiston tarixi elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text='jahon tarix7')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/151", caption="7-sinf jahon tarixi elektron kitobi 📖", reply_markup=ortga_kitob7)



@dp.callback_query_handler(text='rus tili7')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/161", caption="7-sinf rus tili elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text='texnologiya7')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/162", caption="7-sinf texnologiya elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="mig'7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/154", caption="7-sinf milliy istiqlol g'oyasi elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="tasviriy san'at7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/165", caption="7-sinf tasviriy san'at elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="geometriya7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/152", caption="7-sinf geometriya elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="kimyo7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/155", caption="7-sinf kimyo elektron kitobi 📖", reply_markup=ortga_kitob7)


@dp.callback_query_handler(text="jismoniy tarbiya7")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/159", caption="7-sinf jismoniy tarbiya elektron kitobi 📖", reply_markup=ortga_kitob7)


#8-sinf
@dp.callback_query_handler(text='8-sinf')
async def books_class(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli faningizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=sinf_8)


@dp.callback_query_handler(text='fan orqa1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.edit_text("Sinfingizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=kitob_sinf)

@dp.callback_query_handler(text='kitob orqa8')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli faningizni tanlang 👇🏻 ", reply_markup=sinf_8)

@dp.callback_query_handler(text='kitob home1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli bo'limni tanlang: ", reply_markup=menu)


@dp.callback_query_handler(text="adabiyot8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/167", caption="8-sinf adabiyot elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text='fizika8')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/xabarhabar/57", caption="8-sinf fizika elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="biologiya8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/181", caption="8-sinf biologiya elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text='informatika8')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/173", caption="8-sinf informatika elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text='geografiya8')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/172", caption="8-sinf geografiya elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="ingliz tili8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/174", caption="8-sinf ingliz tili elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="algebra8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/168", caption="8-sinf algebra elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="huquq8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/183", caption="8-sinf o'zbekiston davlati va huquqi asoslari elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text='ona tili8')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/182", caption="8-sinf ona tili elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text='uzb tarix8')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/186", caption="8-sinf O'zbekiston tarixi elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text='jahon tarix8')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/177", caption="8-sinf jahon tarixi elektron kitobi 📖", reply_markup=ortga_kitob8)



@dp.callback_query_handler(text='rus tili8')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/189", caption="8-sinf rus tili elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text='texnologiya8')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/187", caption="8-sinf texnologiya elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="mig'8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/179", caption="8-sinf milliy istiqlol g'oyasi elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="iqtisodiy bilim asoslari8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/176", caption="8-sinf iqtisodiy bilim asoslari elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="geometriya8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/171", caption="8-sinf geometriya elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="kimyo8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/184", caption="8-sinf kimyo elektron kitobi 📖", reply_markup=ortga_kitob8)


@dp.callback_query_handler(text="jismoniy tarbiya8")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/178", caption="8-sinf jismoniy tarbiya elektron kitobi 📖", reply_markup=ortga_kitob8)


#9-sinf
@dp.callback_query_handler(text='9-sinf')
async def books_class(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli faningizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=sinf_9)


@dp.callback_query_handler(text='fan orqa1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.edit_text("Sinfingizni tanlang 👇🏻 "), await call.message.edit_reply_markup(reply_markup=kitob_sinf)

@dp.callback_query_handler(text='kitob orqa9')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli faningizni tanlang 👇🏻 ", reply_markup=sinf_9)

@dp.callback_query_handler(text='kitob home1')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer("Kerakli bo'limni tanlang: ", reply_markup=menu)


@dp.callback_query_handler(text="adabiyot9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/194", caption="9-sinf adabiyot elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text='fizika9')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/198", caption="9-sinf fizika elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="biologiya9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/196", caption="9-sinf biologiya elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text='informatika9')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/201", caption="9-sinf informatika elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text='geografiya9')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/204", caption="9-sinf geografiya elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="ingliz tili9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/202", caption="9-sinf ingliz tili elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="algebra9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/195", caption="9-sinf algebra elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="huquq9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/207", caption="9-sinf o'zbekiston davlati va huquqi asoslari elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text='ona tili9')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/210", caption="9-sinf ona tili elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text='uzb tarix9')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/211", caption="9-sinf O'zbekiston tarixi elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text='jahon tarix9')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/205", caption="9-sinf jahon tarixi elektron kitobi 📖", reply_markup=ortga_kitob9)



@dp.callback_query_handler(text='rus tili9')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/193", caption="9-sinf rus tili elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text='texnologiya9')
async def info5(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/212", caption="9-sinf texnologiya elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="mig'9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/208", caption="9-sinf milliy istiqlol g'oyasi elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="iqtisodiy bilim asoslari9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/203", caption="9-sinf iqtisodiy bilim asoslari elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="geometriya9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/200", caption="9-sinf geometriya elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="kimyo9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/206", caption="9-sinf kimyo elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="chizmachilik9")
async def books_class(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_document(document="https://t.me/DarsliklarElektron/197", caption="9-sinf chizmachilik elektron kitobi 📖", reply_markup=ortga_kitob9)


@dp.callback_query_handler(text="wiki")
async def send_text(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("So'z yuboring")
    await lst.wikii.set()

@dp.message_handler(state=lst.wikii)
async def send_text(massage: types.Message, state: FSMContext):
    s1 = await massage.answer("Kuting.")
    await asyncio.sleep(1)
    await s1.delete()
    s2 = await massage.answer("Kuting..")
    await asyncio.sleep(1)
    await s2.delete()
    s3 = await massage.answer("Kuting...")
    await asyncio.sleep(1)
    await s3.delete()
    try:
        await state.finish()
        ny = wikipedia.summary(massage.text)
        await massage.answer(ny, reply_markup=wikiped)
    except:
        await massage.answer(f"<b>{massage.text}</b>ga oid matn topilmadi. qayta uruning!", reply_markup=wikiped,parse_mode='html')
        await state.finish()

@dp.callback_query_handler(text='wikipedia_m')
async def fan_orqaa(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli bo'limni tanlang:")
    await call.message.edit_reply_markup(reply_markup=menu)


@dp.callback_query_handler(text='tuti')
async def tut(call: types.CallbackQuery):
    tt = await call.message.edit_text("Keraki bo'limni tanlang: ")
    await call.message.edit_reply_markup(reply_markup=tuturia)


@dp.callback_query_handler(text='teacher')
async def teach(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer_video(video="https://t.me/xabarhabar/60", caption="Marhamat\n\nUstozlar uchun video qo'llanma", reply_markup=r)


@dp.callback_query_handler(text='reader')
async def teach(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer_video(video="https://t.me/xabarhabar/59", caption="Marhamat\n\nO'quvchi va ota-onalar uchun video qo'llanma", reply_markup=t)


@dp.callback_query_handler(text='teacherv')
async def teach(call: types.CallbackQuery):
    await call.message.edit_media(media=types.InputMediaVideo(media="https://t.me/xabarhabar/60",caption="Marhamat\n\nO'qituvchilar uchun video qo'llanma"))
    await call.message.edit_reply_markup(reply_markup=r)

@dp.callback_query_handler(text='readerv')
async def teach(call: types.CallbackQuery):
    await call.message.edit_media(media=types.InputMediaVideo(media="https://t.me/xabarhabar/59",caption="Marhamat\n\nO'quvchi va ota-onalar uchun video qo'llanma"))
    await call.message.edit_reply_markup(reply_markup=t)


@dp.callback_query_handler(text='tut back')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.edit_caption("Video o'chib ketmaydi!\n\nMarhamat davom etavering 👇🏻")
    await call.message.answer("Kerakli bo'limni tanlang:", reply_markup=menu)


@dp.callback_query_handler(text='t back')
async def fan_orqa(call: types.CallbackQuery):
    await call.message.edit_text("Kerakli bo'limni tanlang:")
    await call.message.edit_reply_markup(reply_markup=menu)


@dp.callback_query_handler(text='new button', user_id=1361526026)
async def news(call: types.CallbackQuery):
    await call.answer(cache_time=1.5)
    await call.message.edit_text("Kerakli bo'limni tanlang:")
    await call.message.edit_reply_markup(reply_markup=nwb)


@dp.callback_query_handler(text='new button')
async def news(call: types.CallbackQuery):
    await call.answer(cache_time=1.5)
    await call.message.edit_text("Kerakli bo'limni tanlang:")
    await call.message.edit_reply_markup(reply_markup=nwb)


@dp.callback_query_handler(text='official', user_id=1361526026)
async def news(call: types.CallbackQuery):
    news_btn = InlineKeyboardMarkup()
    news = db.select_news()
    for i in news:
       news_btn.add(InlineKeyboardButton(i[0], callback_data=i[1]))
    news_btn.add(InlineKeyboardButton(text='Ortga', callback_data='new button2'))
    await call.message.edit_reply_markup(news_btn)
    await post.category.set()

@dp.callback_query_handler(text='new button2', state=post.category)
async def news(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1.5)
    await call.message.edit_text("Kerakli bo'limni tanlang:")
    await call.message.edit_reply_markup(reply_markup=nwb)
    await state.finish()


@dp.callback_query_handler(state=post.category)
async def get_news(call: types.CallbackQuery):
    await call.message.delete()
    slug = call.get_current()['data']
    id = db.get_news_id(slug=slug)
    posts = db.get_news(id[0])
    for post in posts:
        try:
            try:
                await call.message.answer_photo(photo=open(f"E:/NG/Mirzobek_py/django/news_blog/media/{post[2]}", 'rb'), caption=f"{post[0]}\n\n{post[1][3:-4]}")
            except PermissionError:
                await call.message.answer(f"{post[0]}\n\n{post[1][3:-4]}")
        except:
            pass
    news_btn = InlineKeyboardMarkup()
    news = db.select_news()
    for i in news:
       news_btn.add(InlineKeyboardButton(i[0], callback_data=i[1]))
    news_btn.add(InlineKeyboardButton(text='Ortga', callback_data='new button2'))
    await call.message.answer("kerakli kategoriyani tanlang:", reply_markup=news_btn)


@dp.message_handler()
async def send_text(message: types.Message):
    await message.delete()


# @dp.message_handler(content_types=['photo'])
# async def images(message: types.Message):
#     i = message.photo[-1].file_id


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


# SELECT id FROM table where slug="futbol";