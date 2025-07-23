MasterBoss = 200

Sword = 20
Gun = 15
Bomb = 80

# while True:
    # choice = input("ต่อสู้กับมอนเตอร์ หรือ ออก: ")
    # if choice == "1":
    #     print("ต่อสู้มอนเตอร์")
    # elif choice == "2":
    #     print("ออก")



while True:
    print("1.โจมตีมอนเตอร์")
    print("2.หนีดีกว่า")
    choice = int(input("พิมพ์ 1 / 2 เพื่อเลือก: "))
    if choice == 1:
        round = int(input("จะตีกี่ที่ใส่เลขไอ่สัส: "))
        for i in range(round):
            weapon = input("เลือกอาวุธที่จะโจมตี Sword / Gun / Bomb")
            if weapon == "Sword":
                MasterBoss=MasterBoss-Sword
                print("คุณโจมตีด้วยตาบ","เลือดคงเหลือ", MasterBoss)
            elif weapon == "Gun":
                MasterBoss=MasterBoss-Gun
                print("คุณโจมตีด้วยปืน","เลือดคงเหลือ", MasterBoss)
            elif weapon == "Bomb":
                MasterBoss=MasterBoss-Bomb
                print("คุณโจมตีด้วยระเบิด","เลือดคงเหลือ", MasterBoss)