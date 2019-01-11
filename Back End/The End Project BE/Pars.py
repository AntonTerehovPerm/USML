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
        '''
        Вхождение определенного символа в строку - количество
        '''
        kol = 0
        for x in s:
            if x == ':': kol+=1
        return kol

def vhod_str(s,sym):
    '''
    Поиск символа с начала строки
    '''
    for i,x in enumerate(s):
        if sym == x: return i
        
def back_str(s,sym): 
    '''
    Поиск символа с конца строки
    '''
    for i,x in enumerate(s):
        if sym == s[len(s)-1-i]: return len(s)-1-i
        
def leng_str(stroka):
    '''
    Длина строки
    '''
    return len(stroka)
        
def symbol_str(stroka):
    '''
    Все символы в строке и их количество + место расположения
    '''
    symbol = {}
    for i,x in enumerate(stroka):
        if symbol.get(x) == None:
            symbol[x] = 1,[i]
        else:
            symbol[x][1].append(i)
            symbol[x] = symbol[x][0]+1,symbol[x][1]
    return symbol

def in_str(stroka,sumbol_array):
    '''
    проверка вхождения определенного массива символов в строку распаршенную по символам
    '''
    #sumbol_array = ['.',',','!','?','-','_','<','>','[',']','{','}',';',"'"]
    f = False
    for x in sumbol_array:
        if stroka.get(x) != None:
            f = True
    return f
    
def clear_word(stroka):
    s_new = ''
    f = False
    for x in stroka:
        if not(in_str(symbol_str(x),['.',',','!','?','-','_','<','>','[',']','{','}',';',"'"])):
           s_new += x 
        else:
            f = True
            
    return f,s_new

def clear_word_classter(stroka):
    s_new = ''
    f = False
    for x in stroka:
        if not(in_str(symbol_str(x),['.',',','!','?','-','_','<','>',';',"'",'#',"/",'*',':'])):
           s_new += x 
        else:
            f = True
            
    return s_new

def odnokorennie_str(stroka,stroka_2):
    '''
    Проверка двух слов на то, что они однокоренные
    возвращает да/нет, символы по которым оно влется однокоренным
    '''
    if len(stroka) > len(stroka_2):
        d_max = stroka
        d_min = stroka_2
    else:
        d_max = stroka_2
        d_min = stroka
        
    if d_min == d_max[0:len(d_min)]:
        return True,d_min

def in_str_one(stroka):
    '''
    Проверка, что символ есть в массиве
    '''
    sumbol_array = {'.':0,'!':0,'?':0}
    f = False
    if sumbol_array.get(stroka) != None:
            f = True
    return f