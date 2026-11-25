#1
#.strip() 

#---------------------------------------

#این برنامه از ما چی میخواد؟

#1
#words_counter
#تابعی که کلمات رو جمع کنه و تعادشو بده
def words_counter(path):
#ورودی همه تابع ها ادرس فایل متنی هست که کاربر میده
    word = []
    with open (path , mode="r", encoding="utf-8") as f :
#with برای اینکه در اخر خودش فایلو ببنده
#openباز کردن فایل
#mode r همون ریدینگه یعنی فقط فایلو بخون
#encoding چون از زبان فارسی استفاده میکنیم 
        for line in f:
            word +=line.split()
#split() رشته رو به کلمه ها میشکنه و لیست مید
    return( word , len(word))
#اگر پرانتز های اولی رو نزاریم این تابع دوتا خروجی داره چون تو مین هم تعداد کلمات خواسته شده و هم طولانی ترین کلمه پس خود کلمات هم باید باشن
#ولی من ترجیح میدم بزارم و شکل گیری تاپل رو واضح تر ببینم ولی نزارمم میشه و خروجی هم.ن تاپله





#2
#line_counter
#تابعی که خطوط غیر خال را بشمارد
def line_counter(path):
    count = 0
    with open (path , mode="r", encoding="utf-8") as f :
        for line in f:
            if len(line.strip()) != 0:
#دستور .strip() برای حذف فاصله بین دو ""دابل کوتیشن یا به اصطلاح یک خطی که ما در این تمرین گرفتیم به اضافه بک اسلش ان موجود در اخر سطر که این سطر را از سطر بعدی جدا میکند
#چون اگر طر ما خالی باشد پایت.ن انرا خالی نمیداند بکاسلش ان را میشمارد
                count += 1
#البته حلقه فورو اینجوری هم میشد رفت
#       for line in f:
#            if line.strip():
#                count += 1
#چون رشته خالی در ایف فالس حساب میشه پس لن گرفتن واجب نیست
    return count





#3
#character_counter
#مجموع ظول همه خطوط با \n
#پس strip نمیزنیم
def character_counter(path):
    total = 0
    with open (path , mode="r", encoding="utf-8") as f :
            for line in f:
                total += len(line)
    return total