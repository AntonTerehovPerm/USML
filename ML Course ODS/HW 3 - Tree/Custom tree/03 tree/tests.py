import unittest
import numpy as np
import tree


class TestStringMethods(unittest.TestCase):

    def test_entropy(self):
        obj_tree = tree.DecisionTree()
        test_arr = []
        test_arr.append({'arr': np.array([1 for x in range(9)] + [0 for x in range(11)]), 
        	             'answer':0.993})
        test_arr.append({'arr': np.array([1 for x in range(8)] + [0 for x in range(5)]), 
        	             'answer':0.961})
        test_arr.append({'arr': np.array([1 for x in range(1)] + [0 for x in range(6)]), 
        	             'answer':0.592})
        test_arr.append({'arr': np.array([1, 2, 3, 4, 5, 6]), 
        	             'answer':2.585})
        for x in test_arr:
        	val = obj_tree._entropy(x['arr'])
        	self.assertEqual(round(val, 3), x['answer'])

    def test_gini(self):
        obj_tree = tree.DecisionTree()
        test_arr = []
        test_arr.append({'arr': np.array([1 for x in range(9)] + [0 for x in range(11)]), 
                         'answer':0.495})
        test_arr.append({'arr': np.array([1 for x in range(8)] + [0 for x in range(5)]), 
                         'answer':0.473})
        test_arr.append({'arr': np.array([1 for x in range(1)] + [0 for x in range(6)]), 
                         'answer':0.245})
        test_arr.append({'arr': np.array([1, 2, 3, 4, 5, 6]), 
                         'answer':0.833})
        for x in test_arr:
            val = obj_tree._gini(x['arr'])
            self.assertEqual(round(val, 3), x['answer'])

    def test_variance(self):
        obj_tree = tree.DecisionTree()
        test_arr = []
        test_arr.append({'arr': np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), 
                         'answer':6.667})
        test_arr.append({'arr': np.array([1, 2, 7, 4, 5, 6, 7, 8, 9]), 
                         'answer':6.469})
        for x in test_arr:
            val = obj_tree._variance(x['arr'])
            self.assertEqual(round(val, 3), x['answer'])

    def test_mad_median(self):
        obj_tree = tree.DecisionTree()
        test_arr = []
        test_arr.append({'arr': np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), 
                         'answer':2.222})
        test_arr.append({'arr': np.array([1, 2, 7, 4, 5, 6, 7, 8, 9]), 
                         'answer':2.111})
        for x in test_arr:
            val = obj_tree._mad_median(x['arr'])
            self.assertEqual(round(val, 3), x['answer'])

    def test_fit_and_predict(self):
        obj = tree.DecisionTree(min_samples_split=2, max_depth=1)
        X = np.array([[1, 2, 3], 
                      [0, 5, 6], 
                      [7, 8, 9], 
                      [2, 2, 4],
                      [1, 1, 3]])
        y = np.array([1, 1, 3, 4, 5])
        obj.fit(X, y)
        X = np.array([[7, 8, 9]])
        result_y = obj.predict(X)
        self.assertEqual(result_y[0], 1)

    def test_chek_y(self):
        obj = tree.DecisionTree()
        X = np.array([[1, 2, 3], 
                      [0, 5, 6], 
                      [7, 8, 9], 
                      [2, 2, 4],
                      [1, 1, 3]])
        result = obj._chek_y(X)
        self.assertEqual(result, True)

        X = np.array([[1, 2, 1], 
                      [0, 5, 1], 
                      [7, 8, 1], 
                      [2, 2, 1],
                      [1, 1, 1]])
        result = obj._chek_y(X)
        self.assertEqual(result, False)

    '''
    def test_predict_proba(self):

        obj = tree.DecisionTree(min_samples_split=2, max_depth=2)
        X = np.array([[1, 2, 3], 
                      [0, 5, 6], 
                      [7, 8, 9], 
                      [2, 2, 4],
                      [1, 1, 3]])
        y = np.array([1, 2, 3, 4, 5])
        obj.fit(X, y)
        X = np.array([[7, 8, 9], [1, 1, 3]])
        print("\n")
        print(obj.predict_proba(X))
    '''


if __name__ == '__main__':
    unittest.main()


'''
Описание модуля unittest:
    https://pythonworld.ru/moduli/modul-unittest.html

Специальные функци:
    def setUp(self):
        # Код настройки - перед запуском тестов
        pass
    def tearDown(self):
        # Код после выполнения тестов
        pass

Пропуск тестов:
    @unittest.skip(reason) - пропустить тест. reason описывает причину пропуска.
    @unittest.skipIf(condition, reason) - пропустить тест, если condition истинно.
    @unittest.skipUnless(condition, reason) - пропустить тест, если condition ложно.
    @unittest.expectedFailure - пометить тест как ожидаемая ошибка.

Функции для проверок:
    assertEqual(a, b) — a == b
    assertNotEqual(a, b) — a != b
    assertTrue(x) — bool(x) is True
    assertFalse(x) — bool(x) is False
    assertIs(a, b) — a is b
    assertIsNot(a, b) — a is not b
    assertIsNone(x) — x is None
    assertIsNotNone(x) — x is not None
    assertIn(a, b) — a in b
    assertNotIn(a, b) — a not in b
    assertIsInstance(a, b) — isinstance(a, b)
    assertNotIsInstance(a, b) — not isinstance(a, b)
    assertRaises(exc, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc
    assertRaisesRegex(exc, r, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc и сообщение соответствует регулярному выражению r
    assertWarns(warn, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение
    assertWarnsRegex(warn, r, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение и сообщение соответствует регулярному выражению r
    assertAlmostEqual(a, b) — round(a-b, 7) == 0
    assertNotAlmostEqual(a, b) — round(a-b, 7) != 0
    assertGreater(a, b) — a > b
    assertGreaterEqual(a, b) — a >= b
    assertLess(a, b) — a < b
    assertLessEqual(a, b) — a <= b
    assertRegex(s, r) — r.search(s)
    assertNotRegex(s, r) — not r.search(s)
    assertCountEqual(a, b) — a и b содержат те же элементы в одинаковых количествах, но порядок не важен

Запуск теста:
	1. Запустив на исполнение файл с тестом
	2. Запустив команду в консоли: python -m unittest

Дополнительные настроийки запуска из консоли:
	-b (--buffer) - вывод программы при провале теста будет показан, а не скрыт, как обычно.
	-c (--catch) - Ctrl+C во время выполнения теста ожидает завершения текущего теста и затем сообщает результаты на данный момент. Второе нажатие Ctrl+C вызывает обычное исключение KeyboardInterrupt.
	-f (--failfast) - выход после первого же неудачного теста.
	--locals (начиная с Python 3.5) - показывать локальные переменные для провалившихся тестов.
'''