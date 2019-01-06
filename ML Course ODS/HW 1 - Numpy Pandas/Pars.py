def pars (stroka, razdelitel = ' '): 
    '''
    Записываем новый список содержащий распарсеную по пробелу строку
    *new_version - добавить изменение по символу считывания
    razdelitel = ' ' - new_version
    '''
    s='' 
    m=[] 
    for x in stroka:
        if x == razdelitel: 
            if (s != '')and(s != '|') :
                #print('s = /',s+'/')
                m.append(s) 
            s='' 
        else: s +=x 
    return m 

def kol_symbol(s):
        kol = 0
        for x in s:
            if x == ':': kol+=1
        return kol

def vhod_str(s,sym):
    for i,x in enumerate(s):
        if sym == x: return i
        
def back_str(s,sym):
    for i,x in enumerate(s):
        if sym == s[len(s)-1-i]: return len(s)-1-i