def caesar_cipher(text , key):
    result = ""

    for char in  text:

        if char.isupper():
            number= ord(char) - ord("A")
            #چون خود Aهم از 65 شروع میشه و باید همون محاسبات را انجام دهیم 
            number = (adad +key ) % 26
            result = result + chr(number + ord("A"))

        elif char.islower():
            number = ord( char ) - ord("a") 
            #حروف کامپیوتر از 97 شروع میشه برا همین برشون میگردونیم به اعداد یک تا بیستوشیش 
            number = (number + key ) % 26
            #به علاوه کلید و تقسیم بر 26 تا اگه لازمه برگرده به اول حاقه و حروفو از اول بره
            number = number + ord("a")
            #چون در نهایت کامپیوتر قراره کد مارو بخونه و اون با عداد خودش ینی 97 به بالا کار داره دوباره تبدیل به اون اعداد میکنیم
            result = result + chr(number)

        else:
            resulte = result + char
            #اگر فاصله و نقطه و هرچیزی جز حرف بود بدون تغییر میگذاریم

    return result


#دو تابع بر حسب نوع درخواست کاربر که ایا میخواهد رمزگشایی انجام دهد یا رمزنگاری درست میکنیم
def encrypt (text , key):#رمزنگاری
    return caesar_cipher(text , key)

def decrypt (text , key):#رمزگشایی
    return caesar_cipher(text , -key)#کار همونه فقط با کلید منفی تا به عقب بره

