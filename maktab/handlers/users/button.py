from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup

asos = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton("📝 Ma'lumot berish")]
    ], resize_keyboard=True,
    one_time_keyboard=True
)

tel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Raqamni yuborish", request_contact=True)]
    ], resize_keyboard=True,
    one_time_keyboard=True
)

manzil = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Manzilni yuborish", request_location=True)]
    ], resize_keyboard=True,
    one_time_keyboard=True
)


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("📈 Maktab yangiliklar", callback_data='new button'), InlineKeyboardButton("⚠️ Shikoyat qilish", callback_data="report")],
        [InlineKeyboardButton("📚 Darsliklar", callback_data="books"), InlineKeyboardButton("Kundalik.com bo'yicha video qo'llanma", callback_data="tuti")],
        [InlineKeyboardButton('Wikipedia', callback_data='wiki'),InlineKeyboardButton("😎 created by", url='http://t.me/Mirzobek_Sobirov')]
    ]
)

asosiy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("🏠 Asosiy menyuga qaytish", callback_data='home')]
    ]
)

not_ariza = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Ha, albatta", callback_data='yes'), InlineKeyboardButton("Yo'q", callback_data="no")]
    ]
)



kitob_sinf = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("1-sinf", callback_data="1-sinf"), InlineKeyboardButton("2-sinf", callback_data="2-sinf")],
        [InlineKeyboardButton("3-sinf", callback_data="3-sinf"), InlineKeyboardButton("4-sinf", callback_data="4-sinf")],
        [InlineKeyboardButton("5-sinf", callback_data="5-sinf"), InlineKeyboardButton("6-sinf", callback_data="6-sinf")],
        [InlineKeyboardButton("7-sinf", callback_data="7-sinf"), InlineKeyboardButton("8-sinf", callback_data="8-sinf")],
        [InlineKeyboardButton("9-sinf", callback_data="9-sinf"), InlineKeyboardButton("⬅️ Ortga", callback_data='home')]
    ]
)

#1-sinf
sinf_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Tasviriy san'at", callback_data="tasviriy san'at1"), InlineKeyboardButton("Tarbiya", callback_data='tarbiya1')],
        [InlineKeyboardButton("Ingliz tili", callback_data='ingliz tili1'), InlineKeyboardButton("Jismoniy tarbiya", callback_data='jismoniy tarbiya1')],
        [InlineKeyboardButton("Matematika", callback_data='matematika1'), InlineKeyboardButton("Ona tili va o'qish savodxonligi", callback_data='otos1')],
        [InlineKeyboardButton("Musiqa", callback_data='musiqa1'), InlineKeyboardButton("Tabiiy fanlar", callback_data='tabiiy fanlar1')],
        [InlineKeyboardButton("⬅️ Ortga", callback_data="fan orqa1"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='home')],
    ]
)


ortga_kitob1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("⬅️ Ortga", callback_data="kitob orqa1"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='kitob home1')]
    ]
)








#5-sinf
sinf_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Adabiyot", callback_data='adabiyot5'), InlineKeyboardButton("Vatan tuyg'usi", callback_data="vatan tuyg'usi5")],
        [InlineKeyboardButton("Rus tili", callback_data='rus tili5'), InlineKeyboardButton("Botanika", callback_data='botanika5')],
        [InlineKeyboardButton("Geografiya", callback_data='geografiya5'), InlineKeyboardButton("Informatika", callback_data='informatika5')],
        [InlineKeyboardButton("Ingliz tili", callback_data='ingliz tili5'), InlineKeyboardButton("Jismoniy tarbiya", callback_data='jismoniy tarbiya5')],
        [InlineKeyboardButton("Matematika", callback_data='matematika5'), InlineKeyboardButton("Musiqa", callback_data="musiqa5")],
        [InlineKeyboardButton("Ona tili", callback_data="ona tili5"), InlineKeyboardButton("Tasviriy san'at", callback_data="tasviriy san'at5")],
        [InlineKeyboardButton("Tarixdan hikoyalar", callback_data="tarixdan hikoyalar5"), InlineKeyboardButton("Texnologiya", callback_data='texnologiya5')],
        [InlineKeyboardButton("⬅️ Ortga", callback_data="fan orqa1"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='home')],
    ]
)


ortga_kitob5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("⬅️ Ortga", callback_data="kitob orqa5"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='kitob home1')]
    ]
)



#6-sinf
sinf_6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Adabiyot", callback_data='adabiyot6'), InlineKeyboardButton("Tasviriy san'at", callback_data="tasviriy san'at6")],
        [InlineKeyboardButton("Fizika", callback_data='fizika6'), InlineKeyboardButton("Botanika", callback_data='botanika6')],
        [InlineKeyboardButton("Informatika", callback_data='informatika6'), InlineKeyboardButton("Geografiya", callback_data='geografiya6')],
        [InlineKeyboardButton("Ingliz tili", callback_data='ingliz tili6'), InlineKeyboardButton("Matematika", callback_data='matematika6')],
        [InlineKeyboardButton("Musiqa", callback_data='musiqa6'), InlineKeyboardButton("Ona tili", callback_data="ona tili6")],
        [InlineKeyboardButton("Tarix (Qadimgi dunyo)", callback_data="tarix6"), InlineKeyboardButton("Rus tili", callback_data='rus tili6')],
        [InlineKeyboardButton("Texnologiya", callback_data="texnologiya6"), InlineKeyboardButton("Vatan tuyg'u", callback_data="vatan tuyg'u6")],
        [InlineKeyboardButton("⬅️ Ortga", callback_data="fan orqa1"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='home')],
    ]
)


ortga_kitob6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("⬅️ Ortga", callback_data="kitob orqa6"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='kitob home1')]
    ]
)



#7-sinf
sinf_7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Adabiyot", callback_data='adabiyot7'), InlineKeyboardButton("Tasviriy san'at", callback_data="tasviriy san'at7")],
        [InlineKeyboardButton("Fizika", callback_data='fizika7'), InlineKeyboardButton("Zoologiya", callback_data='zoologiya7')],
        [InlineKeyboardButton("Informatika", callback_data='informatika7'), InlineKeyboardButton("Geografiya", callback_data='geografiya7')],
        [InlineKeyboardButton("Ingliz tili", callback_data='ingliz tili7'), InlineKeyboardButton("Algebra", callback_data='algebra7')],
        [InlineKeyboardButton("Musiqa", callback_data='musiqa7'), InlineKeyboardButton("Ona tili", callback_data="ona tili7")],
        [InlineKeyboardButton("Kimyo", callback_data="kimyo7"), InlineKeyboardButton("Rus tili", callback_data="rus tili7'")],
        [InlineKeyboardButton("O'zbekiston tarix", callback_data="uzb tarix7"), InlineKeyboardButton("Jahon tarixi", callback_data='jahon tarix7')],
        [InlineKeyboardButton("Texnologiya", callback_data="texnologiya7"), InlineKeyboardButton("Milliy istiqlol g'oyasi", callback_data="mig'7")],
        [InlineKeyboardButton("Geometriya", callback_data="geometriya7"), InlineKeyboardButton("Jismoniy tarbiya", callback_data="jismoniy tarbiya7")],
        [InlineKeyboardButton("⬅️ Ortga", callback_data="fan orqa1"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='home')],
    ]
)


ortga_kitob7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("⬅️ Ortga", callback_data="kitob orqa7"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='kitob home1')]
    ]
)






#8-sinf
sinf_8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Adabiyot", callback_data='adabiyot8'), InlineKeyboardButton("Iqtisodiy bilim asoslari", callback_data="iqtisodiy bilim asoslari8")],
        [InlineKeyboardButton("Fizika", callback_data='fizika8'), InlineKeyboardButton("Biologiya", callback_data='biologiya8')],
        [InlineKeyboardButton("Informatika", callback_data='informatika8'), InlineKeyboardButton("Geografiya", callback_data='geografiya8')],
        [InlineKeyboardButton("Ingliz tili", callback_data='ingliz tili8'), InlineKeyboardButton("Algebra", callback_data='algebra8')],
        [InlineKeyboardButton("O'zbekiston davlati va huquqi asoslari", callback_data='huquq8'), InlineKeyboardButton("Ona tili", callback_data="ona tili8")],
        [InlineKeyboardButton("Kimyo", callback_data="kimyo8"), InlineKeyboardButton("Rus tili", callback_data="rus tili8")],
        [InlineKeyboardButton("O'zbekiston tarix", callback_data="uzb tarix8"), InlineKeyboardButton("Jahon tarixi", callback_data='jahon tarix8')],
        [InlineKeyboardButton("Texnologiya", callback_data="texnologiya8"), InlineKeyboardButton("Milliy istiqlol g'oyasi", callback_data="mig'8")],
        [InlineKeyboardButton("Geometriya", callback_data="geometriya8"), InlineKeyboardButton("Jismoniy tarbiya", callback_data="jismoniy tarbiya8")],
        [InlineKeyboardButton("⬅️ Ortga", callback_data="fan orqa1"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='home')],
    ]
)


ortga_kitob8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("⬅️ Ortga", callback_data="kitob orqa8"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='kitob home1')]
    ]
)




#9-sinf
sinf_9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Adabiyot", callback_data='adabiyot9'), InlineKeyboardButton("Iqtisodiy bilim asoslari", callback_data="iqtisodiy bilim asoslari9")],
        [InlineKeyboardButton("Fizika", callback_data='fizika9'), InlineKeyboardButton("Biologiya", callback_data='biologiya9')],
        [InlineKeyboardButton("Informatika", callback_data='informatika9'), InlineKeyboardButton("Geografiya", callback_data='geografiya8')],
        [InlineKeyboardButton("Ingliz tili", callback_data='ingliz tili9'), InlineKeyboardButton("Algebra", callback_data='algebra9')],
        [InlineKeyboardButton("Konstitutsiyaviy huquq asoslari", callback_data='huquq9'), InlineKeyboardButton("Ona tili", callback_data="ona tili9")],
        [InlineKeyboardButton("Kimyo", callback_data="kimyo9"), InlineKeyboardButton("Rus tili", callback_data="rus tili9")],
        [InlineKeyboardButton("O'zbekiston tarix", callback_data="uzb tarix9"), InlineKeyboardButton("Jahon tarixi", callback_data='jahon tarix9')],
        [InlineKeyboardButton("Texnologiya", callback_data="texnologiya9"), InlineKeyboardButton("Milliy istiqlol g'oyasi", callback_data="mig'9")],
        [InlineKeyboardButton("Geometriya", callback_data="geometriya9"), InlineKeyboardButton("Chizmachilik", callback_data="chizmachilik9")],
        [InlineKeyboardButton("⬅️ Ortga", callback_data="fan orqa1"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='home')],
    ]
)


ortga_kitob9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("⬅️ Ortga", callback_data="kitob orqa9"),InlineKeyboardButton("🏠 Asosiy menyu", callback_data='kitob home1')]
    ]
)


tenglama = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("🏠 Asosiy menyu", callback_data='tenglama_menu')],
    ]
)



wikiped = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("🏠 Asosiy menyu", callback_data='wikipedia_m'), InlineKeyboardButton("Qayta yozish", callback_data='wiki')],
    ]
)



tuturia = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("O'qituvchilar uchun", callback_data='teacher')],
        [InlineKeyboardButton("O'quvchilar va ota-onalar uchun", callback_data='reader')],
        [InlineKeyboardButton("Bosh menyu", callback_data='t back')]
    ]
)


t = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("O'qituvchilar uchun video qo'llanma", callback_data='teacherv')],
        [InlineKeyboardButton("Bosh menyu", callback_data='tut back')]
    ]
)


r = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("O'quvchilar va ota-onalar uchun video qo'llanma", callback_data='readerv')],
        [InlineKeyboardButton("Bosh menyu", callback_data='tut back')]
    ]
)


nwb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Yangiliklar guruhi", url='https://t.me/+dFnPJrwBq75lNDFi')],
        [InlineKeyboardButton("Rasmiy yangiliklar", callback_data='official')],
        [InlineKeyboardButton("Menyu", callback_data='wikipedia_m')]  
    ],
)

nwb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Yangiliklar guruhi", url='https://t.me/+dFnPJrwBq75lNDFi')],
        [InlineKeyboardButton("Rasmiy yangiliklar", callback_data='official')],
        [InlineKeyboardButton("Yangiliklarni tahrirlash", callback_data='append')],
        [InlineKeyboardButton("Menyu", callback_data='wikipedia_m')]       
    ],
)
soroq = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
soroq.row('🏠 Menyu')


soroqq = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
soroqq.row('🏠 Menyu')
soroqq.row("❌ Oxirgi yuborilgan yangilikni o'chirish ❌")
soroqq.row("❌ Barcha yangilikni tozalash ❌")
