import Pars
import copy

def check_skobka(stroka,simvol):
    '''
    находит следующую закрывающую скобку, по заданной
    '''
    skobka = {'(':')' ,'{':'}' ,'[':']','d':':'}
    depht = skobka[simvol]
    nomber = 0
    srez = ''
    i = 0
    f = False
    #print(depht)
    while nomber == 0:
        #print(i,':',stroka[i])
        if stroka[i] == depht:
            nomber = i+1 
            f = True
        i += 1
        if i> len(stroka)-1:
            nomber = 'error'
    if type(nomber) == type(int()): srez = stroka[0:nomber]
    #print(f,nomber,srez)
    return f,nomber,srez

def sliv_dict(d1,d2):
    '''
    слияние двух словарей + проще говоря
    '''
    if len(d1) > len(d2):
        for x in d2:
            d1[x] = d2[x]
        return d1
    else:
        for x in d1:
            d2[x] = d1[x]
        return d2
		
def werni_slovar_simvol(parametr_stroka):
    '''
    возвращает словарь символов по правил(у)ам
    '''
    command_push ={'s':1,'e':1,'d':1,'e':1,'r':1,'c':1}
    state_command_parametr = {'s':{' ':1},'e':{'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,'Q':1,'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1,'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1},'d':{'0':1, '1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1},'r':1,'c':{'^':1,'_':1,'`':1,'!':1,'#':1,'$':1,'%':1,'&':1,"'":1,'*':1,'+':1,',':1,'-':1,'.':1,'/':1},'x':{'(':1,')':1,'[':1,']':1,'{':1,'}':1}}
    back = {}
    if len(parametr_stroka) == 1:
        if command_push.get(parametr_stroka) == None:
            back = {parametr_stroka:1}
        else:
            back = {parametr_stroka:state_command_parametr[parametr_stroka]}
    else:
        stroka_l = Pars.pars(parametr_stroka[1:len(parametr_stroka)-1]+',',razdelitel = ',')
        #print('stroka_l:',stroka_l)
        for x in stroka_l:
            #print(x)
            if command_push.get(x) == None:
                back = sliv_dict(back,{str(x):1})
            else:
                back = sliv_dict(back,state_command_parametr[str(x)])
    #print(back)
    return back
	
def position_slash(pure):
    '''
    ищет команды с /  + дополнительно выделяет последовательно следующие символы
    '''
    #nomber_slash = []
    #none_command = []
    slosh = [[],[],[]]
    simvol_reg = {}
    command_reg = {'?':1,'*':1,'s':1,'e':1,'d':1,'e':1,'r':1,'c':1}
    comm = {'*':1,'s':1,'e':1,'d':1,'e':1,'r':1,'c':1}
    s = ''
    i = 0
    #k = 0
    while i < len(pure):
        x = pure[i]
        if x == "/":
            if s != '': 
                #none_command.append(s)
                for y in s:
                    slosh[0].append('c')
                    simvol_reg[y] = 1
                    slosh[1].append(simvol_reg)
                    slosh[2].append(False)
                    simvol_reg = {}
            s = ''
            s += x
            i += 1
            if command_reg.get(pure[i]) != None:
                s += pure[i]
                if comm.get(pure[i]) != None:
                    h = 'n'
                else:
                    h = 'c'
                i+=1
                if pure[i] == '[':
                    p = check_skobka(pure[i:len(pure)]+' ','[')
                    #print('p[2]:',p[2])
                    if p[0]:
                        i += p[1]
                        s += p[2]
                        #nomber_slash.append(s)
                        simvol_reg = {}
                        simvol_reg = werni_slovar_simvol(str(p[2]))
                        #print(simvol_reg)
                        #print(type(simvol_reg))
                        slosh[0].append(h)
                        slosh[1].append(simvol_reg)
                        if simvol_reg.get('') == None:
                            slosh[2].append(False)
                        else:
                            slosh[2].append(True)
                        simvol_reg = {}
                    else:
                        print('Ошибка в синтаксисе')
                        print(i,s)
                else:
                    #nomber_slash.append(s)
                    simvol_reg = {}
                    simvol_reg = werni_slovar_simvol(str(p[2]))
                    #print(simvol_reg)
                    #print(type(simvol_reg))
                    slosh[0].append(h)
                    slosh[1].append(simvol_reg)
                    if simvol_reg.get('') == None:
                            slosh[2].append(False)
                    else:
                            slosh[2].append(True)
                    simvol_reg = {}
            s = ''
        else:
            s += x
            i += 1
    return slosh
	
def use_rule(stroka,rule):
    '''
    проверка совподает ли правило и текстовая строка, которая была выбрана
    '''
    #print('+'*100)
    #print(stroka)
    #print(rule)
    step = 0
    i = 0
    end_str = ''
    perv_proverka = False
    #print(len(rule[0]))
    while (i<len(stroka))and(step<len(rule[0])):
        #print('-'*100)
        #print('step: ',step)
        #print('stroka[i]: ',stroka[i])
        #print('rule: ',rule[0][step])
        #print('rule: ',rule[1][step])
        #print('rule: ',rule[2][step])
        f_step = False
        #один повтор
                
        if (((rule[0][step] == 'c')and(rule[2][step] == False)and(rule[1][step].get(stroka[i]) == None))or((rule[0][step] == 'c')and(rule[2][step] == True)and(rule[1][step].get(stroka[i]) == None)))and not(f_step):
                #print('c3')  
                f_step = True
                end_str = 'error'
                return end_str 
                
                    #NNNNNNNNN       
        if (rule[0][step] == 'n')and not(f_step)and(rule[2][step] == False)and(rule[1][step].get(stroka[i]) != None)and(perv_proverka == False):
                #print('n1')  
                f_step = True
                perv_proverka = True
                end_str += stroka[i]
                    
        if (rule[0][step] == 'n')and not(f_step)and(rule[2][step] == False)and(rule[1][step].get(stroka[i]) == None)and(perv_proverka == False):
                #print('n2')     
                f_step = True
                end_str = 'error'
                return end_str 
                
        if (rule[0][step] == 'n')and not(f_step)and(rule[2][step] == True)and(rule[1][step].get(stroka[i]) != None)and(perv_proverka == False):
                #print('n3')     
                perv_proverka = True
                end_str += stroka[i]
                f_step = True
            
        if (rule[0][step] == 'n')and not(f_step)and(rule[2][step] == True)and(rule[1][step].get(stroka[i]) == None)and(perv_proverka == False):
                #print('n4')    
                perv_proverka = True
                f_step = True
        try:            
            if (rule[0][step] == 'c')and(rule[2][step] == False)and(rule[1][step].get(stroka[i]) != None)and not(f_step):
                    #print('c1')
                    f_step = True
                    end_str += stroka[i]
                    step += 1  
            if (rule[0][step] == 'c')and(rule[2][step] == True)and(rule[1][step].get(stroka[i]) != None)and not(f_step):
                    #print('c2')  
                    f_step = True
                    step += 1 
        except IndexError:
                pass
                
                    #NNNNNNNNN - второй бесконечный проход
        if  (perv_proverka == True):
            try:
                if (rule[0][step+1] == 'c')and not(f_step)and(rule[2][step+1] == False)and(rule[1][step+1].get(stroka[i]) != None):
                        #print('n+c1') 
                        f_step = True
                        end_str += stroka[i]
                        step += 2 
                        perv_proverka = False

                if (rule[0][step+1] == 'c')and not(f_step)and(rule[2][step+1] == False)and(rule[1][step+1].get(stroka[i]) == None):
                    #print('n+c2') 
                    f_step = True
                    if rule[1][step].get(stroka[i]) != None:
                        #print('n+c2.1') 
                        end_str += stroka[i] 
                    else:
                        #print('n+c2.2')
                        end_str = 'error'
                        return end_str

                if (rule[0][step+1] == 'c')and not(f_step)and(rule[2][step+1] == True)and(rule[1][step+1].get(stroka[i]) != None):  
                        #print('n+c3')
                        f_step = True
                        end_str += stroka[i]
                        step += 1
                        perv_proverka = False

                if  (rule[0][step+1] == 'c')and not(f_step)and(rule[2][step+1] == True)and(rule[1][step+1].get(stroka[i]) == None):
                    #print('n+c4')
                    f_step = True
                    i=1
                    st = copy.deepcopy(step)
                    f = False
                    while (i<len(rule[0])):
                        if (rule[2][step+i] == True):
                            if (rule[1][step+i].get(stroka[i]) == None):
                                i+=1
                        if (rule[2][step+i] == False):
                            if (rule[1][step+i].get(stroka[i]) != None):
                                f = True
                                end_str += stroka[i]
                                step += i

                    if not(f):
                        step = copy.deepcopy(st)
                        if (rule[1][st].get(stroka[i]) != None):
                            end_str += stroka[i]
                        else:
                            end_str = 'error'
                            return end_str                        
                    #прочекать все последующие, до того, который встретится


                if (rule[0][step+1] == 'n')and not(f_step)and(rule[2][step+1] == False)and(rule[1][step+1].get(stroka[i]) != None):
                        #print('n+c5')
                        f_step = True
                        end_str += stroka[i]
                        step += 1    

                if (rule[0][step+1] == 'n')and not(f_step)and(rule[2][step+1] == False)and(rule[1][step+1].get(stroka[i]) == None):
                        #print('n+c6')
                        f_step = True
                        if rule[1][step].get(stroka[i]) != None:
                            #print('n+c6.1')
                            end_str += stroka[i] 
                        else:
                            #print('n+c6.2')
                            end_str = 'error'
                            return end_str

                if (rule[0][step+1] == 'n')and not(f_step)and(rule[2][step+1] == True)and(rule[1][step+1].get(stroka[i]) != None):
                        #print('n+c7')
                        f_step = True
                        end_str += stroka[i]
                        step += 1

                if (rule[0][step+1] == 'n')and not(f_step)and(rule[2][step+1] == True)and(rule[1][step+1].get(stroka[i]) == None): 
                        #print('n+c8')
                        f_step = True
                        i=1
                        st = copy.deepcopy(step)
                        f = False
                        while (i<len(rule[0])):
                            if (rule[2][step+i] == True):
                                if (rule[1][step+i].get(stroka[i]) == None):
                                    i+=1
                            if (rule[2][step+i] == False):
                                if (rule[1][step+i].get(stroka[i]) != None):
                                    f = True
                                    end_str += stroka[i]
                                    step += i

                        if not(f):
                            step = copy.deepcopy(st)
                            if (rule[1][st].get(stroka[i]) != None):
                                end_str += stroka[i]
                            else:
                                end_str = 'error'
                                return end_str  
                        #прочекать все последующие, до того, который встретится
            except IndexError:
                pass

        #print(perv_proverka)
        #print('end_str: ',end_str)
        i+=1
    #print('end_str = ',end_str)
    return end_str
	
def Reg_Exp_more_rule(stroka,rule):
    '''
    выводит все схожие по правилам строки из главной строки
    Передается список правил и после проверятеся вся строка
    '''
    otvet = []
    for x in rule:
        #print(x)
        otvet.append(Reg_Exp_all(stroka,x))
    return otvet

def Reg_Exp_all(stroka,rule):
    '''
    выводит все схожие по правилу строки из главной строки
    Передается 1 правило? и после проверятеся вся строка
    '''
    rule_new = position_slash(rule)
    otvet = []
    #print('rule_new:',rule_new)
    i = 0
    while i<len(stroka):
        x = stroka[i]
        if rule_new[1][0].get(x) != None:
            ret_otv = use_rule(stroka[i:len(stroka)-1],rule_new)
            otvet.append(ret_otv)
            i+=len(ret_otv)-1
        i+=1
    return otvet
	
def Reg_Exp_one(stroka,rule):
    '''
    выводит один схожий элемент по правилу строки из главной строки
    '''
    rule_new = position_slash(rule)
    #print(rule_new)
    i = 0
    while i<len(stroka):
        x = stroka[i]
        if rule_new[1][0].get(x) != None:
            otvet = use_rule(stroka[i:len(stroka)-1],rule_new)
            return otvet
        i+=1