def calculate_choices(n, k):
    """
    این تابع تعداد انتخاب‌های ممکن را محاسبه می‌کند.

    پارامترها:
    n: تعداد افراد (2 < n < 10^6)
    k: تعداد انتخاب‌ها (1 < k < 10^6)

    بازگشت:
    تعداد انتخاب‌های ممکن به عنوان یک عدد صحیح
    """

    # محاسبه تعداد انتخاب‌ها
    total_choices = 1
    for i in range(k):
        total_choices *= (n - i)
        total_choices //= (i + 1)  # محاسبه combinação

    return total_choices


def main():
    """تابع اصلی برنامه برای دریافت ورودی و نمایش خروجی."""
    x = int(input("تعداد بازی‌ها (x): "))

    for _ in range(x):
        n, k = map(int, input("تعداد افراد (n) و تعداد انتخاب‌ها (k) را وارد کنید: ").split())

        # چک کردن شرایط محدوده
        if 1 < n < 10 ** 6 and 1 < k < n:
            result = calculate_choices(n, k)
            print(result)
        else:
            print("ورودی معتبر نیست.")

        # اجرای برنامه


if __name__ == "__main__":
    main()