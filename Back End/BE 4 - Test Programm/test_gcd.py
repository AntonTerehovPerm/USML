import unittest
import gcd
#можно еще в саму функцию добавить тест

class GCD(unittest.TestCase):
    '''	
    gsd_param - проверка на известных значениях по условиям внутри функции gcd
    gsd_test_of_positions - смена входных данных и проверка верности результата
    gsd_out_check_int- результат работы функции целое число
    '''
    test_array = [[0,10,10],[10,0,10],[10,10,10],[1,1,1],[4,6,2],[10,25,5],[25,10,5],[5,25,5],[15,45,15]]
    n_max_test = 40
    
    def gsd_param(self):
        #Функция для проверки: assertEqual(a, b) — a == b
        for x in self.test_array:
            self.assertEqual(gcd.gcd(x[0], x[1]), x[2])

    def gsd_test_of_positions(self):
        for x in range(0,self.n_max_test):
            for y in range(0,self.n_max_test):
                self.assertEqual(gcd.gcd(x, y), gcd.gcd(x, y))

    def gsd_out_check_int(self):
        for x in range(0,self.n_max_test):
            for y in range(0,self.n_max_test):
                result = gcd.gcd(x, y)
                if result!=0:
                    result = result/int(result)
                    self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()