import asyncio
from handlaers.startFor import *
from handlaers.admin_panel import *
import requests
from bs4 import BeautifulSoup



@dp.message_handler(commands='help')
async def helper(message: types.Message):
	await message.reply_photo(photo='AgACAgIAAxkBAAMEYuyTsH2d797nKsyeaO2fTVK0xW0AAl27MRuWmWhLj6R4yYWDbjEBAAMCAANzAAMpBA', caption="""<b>NAMUNA!</b>

Abituriyent ID'si qayerdan olish haqida!\n\n\nMurojaat uchun admin: @perevodlive""")

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def f(message: types.Message):
	sql.execute(f"""UPDATE users SET tel_Num =  '{message.contact.phone_number}' WHERE user_id = '{message.from_user.id}'""")
	db.commit()
	await message.reply("<b>Abituriyent ID raqamini yuboring va imtihon natijalaringiz bilan tanishing!</b>", reply_markup=types.ReplyKeyboardRemove())
	await message.reply_photo(photo="AgACAgIAAxkBAAMEYuyTsH2d797nKsyeaO2fTVK0xW0AAl27MRuWmWhLj6R4yYWDbjEBAAMCAANzAAMpBA", caption="""<b>NAMUNA!</b>

Abituriyent ID'si qayerdan olish haqida!""")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def f(message: types.Message):
	if message.text.isdigit() == True:
		try:

			send = await message.reply("Iltimos biroz kuting...")
			try:
				URL1 = f"https://mandat.dtm.uz/Home2022/AfterFilter?name={message.text}&region=0"
				text = await one_data_get(URL1)
			except:
				URL1 = f"http://mandat.dtm.uz/Home2022/AfterFilter?name={message.text}&region=0"
				text = await one_data_get(URL1)
			await send.delete()
			await message.reply(text[0])
			name = text[1]
			if name == "Ma'lumot topilmadi":
				pass
			else:
				sent = await message.reply("Keyingi ma'lumotlar yuklanmoqda\nIltimos biroz kuting...⌛️")
				try:
					URL2 = f'https://mandat.dtm.uz/Home2022/Details/{message.text}'
					text2 = await two_data_get(URL2)
				except:
					URL2 = f'http://mandat.dtm.uz/Home2022/Details/{message.text}'
					text2 = await two_data_get(URL2)
				await sent.delete()
				await message.reply(text2)


		except:
			await message.reply("Sayt bilan aloqa uzilib qoldi, iltimos 3 daqiqadan keyin yana urinib ko'ring yana ko'ring")
	else:
		await message.reply("Abiturent ID sini to'g'ri kiriting")


if __name__=="__main__":
	executor.start_polling(dp)