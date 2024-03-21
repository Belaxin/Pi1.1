maxBody = 20
percenta = float(input("zadaj body: ")) / maxBody * 100
print(f"Ziskal si {percenta:.2f}%")
print(f"Ziskal si {round(percenta, 2)}%")
# if percenta >= 90:
#     znamka = 1
#     print("Vyborny")
# else:
#     if percenta >= 75:
#         print("Chvalitebny")
#         znamka = 2
#     else:
#         if percenta >= 50:
#             print("dobry")
#             znamka = 3
#         else:
#             if percenta >=30:
#                 print("dostatocny")
#                 znamka = 4
#             else:
#                 print("nedostatocny!!!")
#                 znamka = 5

if percenta >= 90 :
    print("Vyborny")
elif 75 <= percenta:
    print("Chvalitebny")
elif 50 <= percenta:
    print("Dobry")
elif 30 <= percenta:
    print("dostatocny")
else:
    print("Nedostatocny!!!!")
