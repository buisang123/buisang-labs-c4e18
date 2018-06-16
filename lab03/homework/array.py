import re

def remove_dollar_sign(s):
    
    array = re.sub("\$","",s)  
    
    return array

# print(remove_dollar_sign("$80 sang $"))
