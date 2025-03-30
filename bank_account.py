class BankAccount:
    def __init__(self, account_number, balance, name):
        
        self.__account_number = account_number
        self.__balance = balance
        self.__name = name
    
    def deposit(self, amount):
        # ฝากเงินเข้าบัญชี
        if amount > 0:
            self.__balance += amount
            print(f"ฝากเงินจำนวน {amount} บาท สำเร็จ")
        else:
            print("ไม่สามารถฝากเงินที่มีค่าน้อยกว่าหรือเท่ากับศูนย์")
    
    def withdraw(self, amount):
        # ถอนเงินจากบัญชี
        if amount > 0:
            # ตรวจสอบว่ามีเงินพอให้ถอนหรือไม่
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"ถอนเงินจำนวน {amount} บาท สำเร็จ")
            else:
                print("ยอดเงินคงเหลือไม่เพียงพอ")
        else:
            print("ไม่สามารถถอนเงินที่มีค่าน้อยกว่าหรือเท่ากับศูนย์")
    
    def get_balance(self):
        # แสดงยอดเงินคงเหลือ
        return self.__balance


if __name__ == "__main__":
    
    my_account = BankAccount(12345, 1000, "สมชาย")
    
    print(f"ยอดเงินเริ่มต้น: {my_account.get_balance()} บาท")
    
    my_account.deposit(500)
    print(f"ยอดเงินหลังฝาก: {my_account.get_balance()} บาท")
    
    my_account.withdraw(300)
    print(f"ยอดเงินหลังถอน: {my_account.get_balance()} บาท")
    
    my_account.withdraw(2000)
    
    my_account.deposit(-100)