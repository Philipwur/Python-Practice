#%%

#https://edabit.com/challenge/MGALfBAXhXqqdFyqo

#look into translate python module

key = dict(zip("abcdefghijklmnopqrstuvwxyz",
                "zyxwvutsrqponmlkjihgfedcba"
                ))

def atbash(txt):
	
    txt = list(txt)
    
    for i in range(len(txt)):
        
        if txt[i].lower() in key:

            if txt[i].isupper():
                txt[i] = key[txt[i].lower()].upper()
            
            else:
                txt[i] = key[txt[i]] 
    
    return "".join(txt)
