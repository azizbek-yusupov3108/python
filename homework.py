# 1

# print('sevimli kitobllaringiz')
# savol = 'sevimli kitobingizni kiriting'
# savol+="(dasturni toxtatish uchun 'quit' deb yozing)"
# qiymat=""
# while qiymat !='quit':
#     qiymat = input(savol)
#     print(qiymat)



# 2


# while True:
#     yosh = input("Iltimos, yoshingizni kiriting (yoki 'exit' / 'quit' deb yozing): ")
#
#     if yosh.lower() in ['exit', 'quit']:
#         print("Dastur to'xtatildi.")
#         break
#
#     try:
#         yosh = int(yosh)
#
#         if yosh < 7:
#             chipta_narhi = 2000
#         elif 7 <= yosh < 18:
#             chipta_narhi = 3000
#         elif 18 <= yosh < 40:
#             chipta_narhi = 10000
#         else:
#             chipta_narhi = ("sizga kirish bepul")
#
#         print(f"Sizning chipta narhingiz: {chipta_narhi} ")
#
#     except ValueError:
#         print("Iltimos, to'g'ri yosh kiriting.")


# 3


# buyurtma = []
#
# while True:
#     mahsulot = input("mahsulot kiriting (toxtatiw uchun 'stop' deb yozing): ")
#
#     if mahsulot.lower() == 'stop':
#         break
#
#     buyurtma.append(mahsulot)
#     print(f"'{mahsulot}' mahsuloti buyurtma ro'yxatiga qo'shildi.")
#
# print("\nBuyurtma ro'yxati:")
# for i in buyurtma:
#     print(f"- {i}")
#
#
# 4
#
#
# mahsulotlar = {}
#
# while True:
#     mahsulot = input("Mahsulot nomini kiriting (toxtatiw uchun 'stop' deb yozing): ")
#
#     if mahsulot.lower() == 'stop':
#         break
#
#     narh = input(f"{mahsulot} narhini kiriting: ")
#
#     mahsulotlar[mahsulot] = narh
#
# print("\nSiz kiritgan mahsulotlar va narhlari:")
# for mahsulot, narh in mahsulotlar.items():
#     print(f"{mahsulot}: {narh}")






# 1
#
#
# mashhur_shaxslar = [
#     {
#         "ism": "Alisher NAvoiy",
#         "tug_yil":  1441,
#         "t_joy": "Hirot",
#         "umr": 60,
#     },
#     {
#         "ism": "",
#         "tug_yil":  1894,
#         "t_joy": "Toshkent",
#         "umr": 44,
#     },
#     {
#         "ism": "Erkin Vohidov",
#         "tug_yil":  1936,
#         "t_joy": "Farg'ona",
#         "umr": 80,
#     },
#     {
#         "ism": "Jaloliddin Rumiy",
#         "tug_yil":  1207,
#         "t_joy": "Balx",
#         "umr": 70,
#     }
# ]
#
# for shaxs in mashhur_shaxslar:
#     print(f"{shaxs['ism']} "
#           f"{shaxs ['tug_yil']}-yilda "
#           f"{shaxs['t_joy']}da tavvalud topgan "
#           f"{shaxs['umr']}yil umr ko'rgan.")
#
# 3
#
#
# ismi = "Suroj"
#
# sevimli_kinolar = {
#     "Suroj": ["Qasoskorlar", "Yashil kitob", "DC"]
# }
#
# print(f"{ismi}ning sevimli kinolari:")
# for kino in sevimli_kinolar[ismi]:
#     print(f"{kino}")
# print()
#
#
# ismi = "Asad"
#
# sevimli_kinolar = {
#     "Asad": ["Tinch akeani dahshatlari", "Zamonlar osha", "Titanik"]
# }
#
# print(f"{ismi}ning sevimli kinolari:")
# for kino in sevimli_kinolar[ismi]:
#     print(f"{kino}")
# print()
#
# ismi = "Javohr"
#
# sevimli_kinolar = {
#     "Javohr": ["Abdullajon", "Shum bola", "Shaytanat"]
# }
#
# print(f"{ismi}ning sevimli kinolari:")
# for kino in sevimli_kinolar[ismi]:
#     print(f"{kino}")
# print()
#
# ismi = "Boboxon"
#
# sevimli_kinolar = {
#     "Boboxon": ["Qarib dengizi qaroqchilari", "Joker"]
# }
#
# print(f"{ismi}ning sevimli kinolari:")
# for kino in sevimli_kinolar[ismi]:
#     print(f"{kino}")



# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu aleykum")
#
# salom_ber()



# def salom_ber(ism):
#     """Foydalanuvchini ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu aleykum, hurmatli {ism.title()}")
#
#
# salom_ber("hasan")
#
# salom_ber("azizbek")



# def yosh_hisobla(tugilgan_yil, joriy_yil=2024):
#
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasz")
#
# yosh_hisobla(2008)




# def toliq_ism_yasa(ism, familya):
#
#     toliq_ism = f"{ism} {familya}"
#     return toliq_ism
#
# print(toliq_ism_yasa("Azizbek", "yusupov"))



# print("yusupov Azizbek")



# def toliq_ism_yasa(ism, familya, otasining_ismi):
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familya}"
#     else:
#         toliq_ism = f"{ism} {familya}"
#     return toliq_ism.title()
#
# talaba1 = toliq_ism_yasa("olim", "masharipov", "abrorovich")
# talaba2 = toliq_ism_yasa("hakm", "olimov", "abrohimovich")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")




# homework


# def tugilgan_yil_hisobla(h_yil=2024):
#     ismi = input("Ismingizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))
#     print(f"{ismi}, siz {h_yil-yosh}- yilda tug'ilgansiz")
#
# tugilgan_yil_hisobla()


# def sonni_hisobla():
#     son = int(input("Sonni kiriting: "))
#
#     kvadrat = son ** 2
#     kub = son ** 3
#
#     print(f"{son} ning kvadrati: {kvadrat}")
#     print(f"{son} ning kubi: {kub}")
#
# sonni_hisobla()
#
#
# def j_yoki_t():
#     son = int(input("Sonni kiriting: "))
#
#     if son % 2 == 0:
#         print(f"{son} soni juft son.")
#     else:
#         print(f"{son} soni toq son.")
#
# j_yoki_t()



# def kattason():
#     son1 = int(input("Birinchi sonni kiriting: "))
#     son2 = int(input("Ikkinchi sonni kiriting: "))
#
#     if son1 > son2:
#         print(f"Katta son: {son1}")
#     elif son1 < son2:
#         print(f"Katta son: {son2}")
#     else:
#         print("Sonlar teng.")
#
# kattason()
