import Pars 
class Data_Analysis():
    history = [] #история работы с БД
    l_data = [] #основное хранилище БД
    error_str = [] #ошибочные строки, которые были получены при чтении новой БД
    zapros_data = {} #история запросов, чтобы не вычислять ответ три часа, а получить готовый
    name_file = 'test.txt' #имя новой бд
    name_data = []#название столбцов бд, чтобы было проще обращаться, а не через циферки столбцов
    test_err = False 
    read_name_data = False
    test_inf = {}
    id_array_individual ={}
    leng = 0
    
    #Раздел истории БД
    def info_data_history(self,history):
        '''
        Вывод истории работы с БД
        '''
        for x in self.history:
            print(x)
            
    def write_history(self,s):
        '''
        Запись истории работы с БД
        '''
        self.history.append(str(len(self.history)+1)+'.'+s)
    #Раздел обработки новой бд на ошибки репозитории и т.д.
    
    def pr_znach(self,znach_test):
        for x in znach_test:
            print(x, ': ',znach_test[x])
            print(' ')
    
    def  test_znach(self,x,znach_test,i):
        for j,y in enumerate(x):
                      if  znach_test.get(j) == None:
                          znach_test[j] = {} 
                          znach_test[j][y] = 1,[[i,j]] 
                      else:
                         if znach_test[j].get(y) == None:
                            znach_test[j][y] = 1,[[i,j]] 
                         else:
                            znach_test[j][y][1].append([i,j])
                            znach_test[j][y] = znach_test[j][y][0] + 1, znach_test[j][y][1]
        return znach_test
    
    def y_n(self,s):
        print(s)
        if input() == 'yes': return True
        else: return False
        
    def in_data(self,mas,d):
        for x in mas:
            if d == int(x): return True
        return False
    
    def dell_data(self,l,dell_cells):
        new_l = []
        #print(l)
        for x in l:
            one_l = []
            for i,y in enumerate(x):
                #print('y = ',y)
                if self.in_data(dell_cells,i) == False:
                        one_l.append(y)    
            #print('one_l  ',one_l)
            new_l.append(one_l)
        #print('new_l  ',new_l)
        return new_l
    
    def vvod(self):
        print('Ввдите через пробел все номера столбцов в одну строку')
        a = input()+' '
        a = Pars.pars(a)
        return a
    
    def small_analysis(self,znach_test,len_test,l):
        max_z = len(znach_test[0])
        i_max = 0
        dell_data_1 = []
        dell_data_2 = []
        new_l = []
        for i,x in enumerate(znach_test):
            #print(znach_test[i])
            if max_z<=len(znach_test[i]):
                max_z = len(znach_test[i])
                i_max = i
            if len(znach_test[i]) == 1: dell_data_1.append(i)
            if len(znach_test[i]) == 2: dell_data_2.append(i)
        #print(dell_data_1)
        #print(dell_data_2)
        if len(dell_data_1) >= 1: 
           if self.y_n('Стоит удалять эти столбцы '+str(dell_data_1)+' в них содержится единственное значение? Выполнить данное действие? (yes|no)'):
              new_l = self.dell_data(l,self.vvod())
              #нужно придумать куда соранять измененную БД
            
        if len(dell_data_2) >= 1: 
            print('Тут несколько столбцов бинарного вида - это так?')
            print(dell_data_2)
        #return new_l - не помню, что тут возвращается
        
    def test_err_data(self,test_inf):
        '''
        Тестирую БД при вводе на ошибки, пропуски исключения
        Reg.exp - необходимы регулярные выражения и проверка на соответствия
        '''
        self.write_history('Тестирую и исправляю новую БД из файла: '+self.name_file)
        self.write_history('Ошибки тестирования: '+self.name_file)
        l = self.l_data
        len_test = {'Ошибка':0}
        znach_test = {}
        for i,x in enumerate(l):
            try: 
                len_test[len(x)][1].append(i)
                len_test[len(x)] = len_test[len(x)][0] + 1, len_test[len(x)][1]
                znach_test = self.test_znach(x,znach_test,i)
            except KeyError: 
                len_test[len(x)] = 1,[i]
                len_test['Ошибка'] = len_test['Ошибка'] + 1
                znach_test = self.test_znach(x,znach_test,i)
            except AttributeError:     
                pass
        #print(len_test)      
        #print(znach_test)
        #data.pr_znach(znach_test)
        #new_l = self.small_analysis(znach_test,len_test,l) - что тут возвращается
        self.id_array_individual = znach_test 
        #return new_l - что тут возвращается
        
    #Раздел наполнения БД
    def data_read(self, name_file = 'test.txt', r = ' ', l_data = [], first_read_data = True, name_data = [], test_err = False, 
              read_name_data = False):    
        #name_data - список названия столбцов
        #read_name_data - нулевой столбец содержит названия внутри всей БД
        '''
        В будущем основная часть создания массива списка класса, возможно из-за каких-то ошибок неправильная запись
        нужно добавить показатель количества считываемых строк
        файл закрываем, чтобы долго с ним не работать и он не наполнял память
        first_read_data - проверка первого заполнения класса данными
        test_err - включает тестирование БД на ошибки, пропуски исключения
        read_name_data - первая строка содержит название всех столбцов name_data - сразу изменение названия
        '''
        self.write_history('Добавляю новую БД из файла: '+name_file)#проверять и подумать над логами вывода
        #if test_err : test_err_data(name_file)
        self.name_file = name_file
        f = open(name_file, 'r')
        if first_read_data: l_data = []
        for i,line in enumerate(f):
            if (i == 0)and(read_name_data == True):
                #print(line)
                s = line[0:len(line)-2]+r
                self.name_data = Pars.pars(s, razdelitel = r)
            else:
                s = line[0:len(line)-2]+r
                l_data.append(Pars.pars(s, razdelitel = r))
        f.close()
        self.l_data = l_data
        self.leng = len(l_data)
    #информация о БД
    
    def head(self,n):
        self.write_history('Вывожу строки из новой БД с начала и до строки № '+str(n))
        '''
        Считываем 5 строк из новосозданного списка содержащего элементы строки файла
        '''
        #print(n)
        l = self.l_data
        for x in range(0,n):
            print(l[x])
            
    def head_sl(self,p):
        self.write_history('')
        '''
        Считываем 5 строк из новосозданного списка содержащего элементы строки файла
        '''
        #print(len(l))
        if type(p) == type(dict()):
            l = p
        else:
            l = self.id_array_individual[p]
        for x in l:
            print(x,' : ',l[x][0])
            #print(l[x][0])
        print(len(l))
        
    def info(self):
        self.write_history('Вывожу информацию из новой БД')
        '''
        Получаем информацию определенную из созданного списка
        v_0 вставить true false подключаемых методов к анализу списка
        v_1 вставить анализатор + функцию сохранения таблицы в новый файл
        v_2 поиск пробелов и исключений список error - для строк, возможно проверка 
            reg_edit(регулярными выражениями на соответствие строки или анализ 
            строки для выделения информации)
        '''
        print('Длина Базы Данных =',self.leng)
        print('Количество признаков(столбцов/Data Frame) в Базе Данных =',len(self.name_data))
    #Раздел запросов к БД
    def analisys_data():
        '''
        Анализирую БД
        '''
        write_history('Анализирую новую БД из файла: '+name_file)
        
    def zapros_str(self,zapr,poll):
        new_slovar = {}
        for i,x in enumerate(poll):
            #print(x)
            #print(poll[x])
            f = True
            i = 0
            while f:
                if i+len(zapr) >= len(x): f = False
                else:
                    if x[i:i+len(zapr)] == zapr: 
                        f = False
                        new_slovar[x] = poll[x]
                i +=1
        print(len(new_slovar))
        return new_slovar
    def check_zapros(self,s):
        '''
        Профверка правильности сформированности запроса из строки
        '''
        return True   
    
    def check_zapros_er(self,s):         
        '''
        Профверка существования запроса в памяти.
        Был уже запрос или нет
        '''
        try:
            print(self.zapros_data[s]) 
            return True
        except KeyError:
            return False  
        
    def realized_zapr(self,s,poll):
        type_zapr = s[0:Pars.vhod_str(s,':')]
        zapr_s = s[Pars.vhod_str(s,':')+2:Pars.back_str(s,"'")]
        #print('type_zapr = ',type_zapr)
        #print('zapr_s = ',zapr_s)
        if type_zapr == '%':
            for x in poll:
                if zapr_s == x: 
                    return poll[x][0] / self.leng * 100
                
        if type_zapr == 'max':
            ma_x = 0
            ima_x = ''
            for x in poll:
                if ma_x < int(x): 
                    ma_x = int(x)
                    ima_x = x
            return "Max = "+ima_x+" - "+str(poll[ima_x][0])   
        
        if type_zapr == 'min':
            mi_n = poll[0]
            imi_n = ''
            for x in poll:
                if mi_n > int(x): 
                    mi_n = int(x)
                    imi_n = x
            return "Min = "+imi_n+" - "+str(poll[imi_n][0])  
        
        if type_zapr == 'p':
            summary = 0
            kolich = 0
            for x in poll:
                kolich += poll[x][0]
                summary += int(x)*poll[x][0]
            return summary / kolich
        
        if type_zapr == 'k':
            new_zapr = {}
            #print('poll = ',poll)
            for x in poll[1]:
                #print(x)
                #print(new_zapr)
                if new_zapr.get(self.l_data[x[0]][int(zapr_s)]) == None:
                          new_zapr[self.l_data[x[0]][int(zapr_s)]] = 1,[x]
                else:
                    new_zapr[self.l_data[x[0]][int(zapr_s)]][1].append(x)
                    new_zapr[self.l_data[x[0]][int(zapr_s)]] = new_zapr[self.l_data[x[0]][int(zapr_s)]][0] + 1, new_zapr[self.l_data[x[0]][int(zapr_s)]][1]
                    
            return new_zapr
        
    def razlosh_zapr(self,s):
        pass
    
    def zapros_in_data(self,zapr,poll):
        #s - запроса, вид zpr - все запросы poll - массив на запрос 
        '''
        Обработка БД по запросу пользователя
        '''
        if len(zapr) == 0: print('Ошибка запросов. Нет ни оного запроса')
        else:
            if type(zapr) == type(str()):
                #print(type(zapr))
                #print('stroka')
                if self.check_zapros(zapr):
                    if self.check_zapros_er(zapr) == False:
                         if Pars.kol_symbol(zapr) > 1: self.razlosh_zapr(zapr)
                         else: 
                             self.zapros_data[zapr] = self.realized_zapr(zapr,poll)
                             #print(self.zapros_data[zapr])
                             return self.zapros_data[zapr]
            else:
                #print(type(zapr))
                #print('massiv')
                for x in zapr:
                    resh = {}
                    if self.check_zapros(x):
                        if self.check_zapros_er(x) == False:
                             if Pars.kol_symbol(x) > 1: self.razlosh_zapr(x)
                             else: self.realized_zapr(x)
                          
                      
        
            #if check_zapros(zapr)[0] == False: print(check_zapros(zapr)[1])
            #else:
                #print(check_zapros(zapr)[1])
                #if s == 'str': self.zapros_data[s+':'+zapr] = self.zapros_str(zapr,poll)
        #zapros_data[s+zapr] = result


    #специальное хранения БД - сохранение
    def save_data(self,l_data):
        '''
        Сохранение БД
        '''
        pass
    #Ужас Садамия и прочее!
    def read_all_base(l_data = []):
        '''
        Вывод всей БД
        '''
        write_history('Вывожу ВСЮ БД')
        print('Вы уверены, что хотите считать ВСЮ Базу Данных? Не слипнется ли у вас кеш?!??!')
        print('yes/no')
        f_podtverzhdenia = 'no'
        if f_podtverzhdenia == 'yes':
            for x in l_data:
                print(x)
        print('Этот ужас закончился!!!')