# قم بعمل مخطط تدفقي يأخذ رقمين من المستخدم X و Y ويطبع أي رقم هو الأكبر بينهما للمـــستخدم.
# (ماذا عن المساواة ؟؟)

def max_num(x, y):
    if x == y: 
        return f"The numbers are equal = {x}"
    elif x > y: 
        return  f"The max number is = {x}" 
    else : 
        return f"The max number is = {y}" 

x =292 
y =292 

# print(f"{max_num(x,y)}")




# قم بعمل مخطط تدفقي يأخذ ثلاثة أرقام من المستخدم ويطبع أي رقم هو الأكبر.

def max_numbers(x, y, z):
    if x >= y and x >= z : 
        return f" the maximum number is {x}"
    elif y >= x and y >= z :
        return f"the maximum number is {y}"
    elif z >= x and z >= y :
        return f"the maximum number is {z}"
    else: 
        return f"the numbers are equals = {x} "
    
x = 8
y =8
z =8
print(max_numbers(x,y,z))