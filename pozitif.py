# صهيب طفلٌ في الرابعة من عمره ولا يمكنه تحديد إذا ما كان أي عدد سالباً أم موجباً
#  لذا قم بتصميم برنامج يحدد إذا ما كان العدد 
# الذي يقوم بإدخاله صهيب موجبا أم سالبا و اطبع الناتج.

def pozitiv_number(number):
    if number > 0 :
        return f"positive number"
    else : 
        return f"negative number"

x =4 
print(pozitiv_number(x))