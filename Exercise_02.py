# دریافت ورودی از کاربر
n = int(input("تعداد اعداد: "))
m = int(input("عدد مورد نظر: "))

# لیستی برای ذخیره اعداد
numbers = []

# دریافت اعداد از کاربر
for _ in range(n):
    number = int(input())
    numbers.append(number)

# بررسی وجود m در لیست
if m in numbers:
    print(numbers.index(m) + 1)  # ایندکس اول + 1 برای چاپ در فرمت خواسته شده
else:
    print(-1)  # اگر m وجود نداشته باشد