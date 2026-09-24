while True:
 Speed = float(input("กรุณาระบุค่าความเร็ว (km):"))
 if Speed >= 0:
     break
 print("ค่าความเร็วต้องไม่ติดลบ กรุณากรอกใหม่!")
while True:
    Time = float(input("กรุณาระบุเวลา (hours):"))
    if Time > 0:
      break
    elif Time == 0:
     print("เวลาต้องมากกว่า 0 (ไม่สามารถหารด้วยศูนย์ได้) กรุณากรอกใหม่!")
    else:
     print("เวลาต้องไม่ติดลบ กรุณากรอกใหม่!")
Velocity = Speed / Time
print("คำตอบคือ: "+str(Velocity)+" km/h")

