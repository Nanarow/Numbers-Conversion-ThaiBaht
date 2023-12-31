thaiNum = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
unit = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
unit = unit + (unit[1:]*6)  # ทำได้ถึงหลัก ล้านล้านล้านล้านล้านล้าน

thaiText = ""
numberInput = list(map(int, list(input("กรอกตัวเลข : "))))
length = len(numberInput)
unit = unit[:length]  # slice จาก unit ว่าถึงหลักไหน
unit = unit[::-1]  # reverse หลัก

for idx, num in enumerate(numberInput):  # emurate เอาทั้งindexและ item ของindexนั้นๆ
    current = length - idx
    numThai = thaiNum[num]
    if num == 0:
        continue
    if num == 2 and current % 6 == 2:  # หลักสิบของเลข 2
        numThai = "ยี่"
    if num == 1 and current % 6 == 2:  # หลักสิบของเลข 1
        numThai = ""
    if num == 1 and current % 6 == 1 and current != length:  # หลักหน่วยของเลข 1 
        numThai = "เอ็ด"
    thaiText += numThai + unit[idx]

print(thaiText, "บาทถ้วน")
