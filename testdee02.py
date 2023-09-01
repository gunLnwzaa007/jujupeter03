#การรับค่าข้อมูลทางเเป้นพิมพ์ด้วย python
NAME = input("ใส่ชื่อ : ")
YEAR_BORN = input("ใส่ปีเกิด : ")
print('--------------------------')
#ฟังก์ฃั่นในการเเปลงข้อมูลจากข้อความเป็นตัวเลข int(), float()
#ฟังก์ฃั่นในการเเปลงข้อมูลจากตัวเลขเป็นข้อความ str()
print(f'Welcome.. {NAME} Born.. {YEAR_BORN} Year.. {2023 -int(YEAR_BORN)}')
print("Welcome..",NAME,"Born..",YEAR_BORN,"Year..",2023-int(YEAR_BORN))
print("Welcome.. "+NAME+" Born.. "+YEAR_BORN+" Year.. "+str(2023-int(YEAR_BORN)))
print("Welcome.. {} Born.. {} Year.. {}".format(NAME,YEAR_BORN,2023 - int(YEAR_BORN)))
print("welcome.. %s Born.. %s Year.. %d"%(NAME,YEAR_BORN,2023 - int(YEAR_BORN)))

