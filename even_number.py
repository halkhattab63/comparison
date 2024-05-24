# قم بعمل مخطط تدفقي يأخذ رقم من المستخدم ويطبع إذا ما كان الرقم فردي أم زوجي.
# (قم بالإستفادة من المود mod وهو باقي عملية القسمة (يمكن تمثيل المود بالإشارة %) )

def is_even( number):
    if number%2 == 0 : 
        return f"the number is even number "
    else : 
        return f"the number is not even number (odd number)" 
    
x= 5
print(is_even(x)) 