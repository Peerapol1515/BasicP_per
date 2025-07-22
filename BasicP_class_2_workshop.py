x = int(input("กรอกระยะทาง:"))
if 5 <= x <= 50 :
    print("ค่าส่ง10บาท")
elif 51 <= x <= 100 :
    print("ค่าส่ง15บาท")
elif 101 <= x <= 300 :
    print("ค่าส่ง25บาท")
elif 301 <= x <= 500 :
    print("ค่าส่ง35บาท")
elif 501 <= x :
    print("ค่าส่ง45บาท")
else: 
    print("ส่งฟรี")