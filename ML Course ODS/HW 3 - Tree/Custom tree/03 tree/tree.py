import numpy as np
import math as mt
from sklearn.base import BaseEstimator


class DecisionTree(BaseEstimator):
    
    def __init__(self, max_depth=np.inf, min_samples_split=2, 
                 criterion='entropy', debug=False):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.debug = debug
        self.criterion = criterion

    def fit(self, X, y):
        if self.criterion=='entropy':
            self.criterion_func = self._entropy
            self.type_answer = 'max_count'
        elif self.criterion=='gini':
            self.criterion_func = self._gini
            self.type_answer = 'max_count'
        elif self.criterion=='variance':
            self.criterion_func = self._variance
            self.type_answer = 'avg'
        elif self.criterion=='mad_median':
            self.criterion_func = self._mad_median
            self.type_answer = 'avg'
        data = np.c_[X, y]
        self.y_var = np.unique(y, axis=0)
        self.tree = np.array(self._get_tree(data, '1'))

    def predict(self, X):
        y = []
        for line in X:
            answer = self._get_leaf(line,'1')
            y.append(self._get_answer_val(answer))
        y = np.array(y)
        return(y)

    def predict_proba(self, X):
        y = []
        for line in X:
            answer = self._get_leaf(line,'1')
            var_answer = answer[:,0]
            dif_var = np.array(np.setdiff1d(self.y_var, var_answer))
            p_0 = np.array([0 for x in range(len(dif_var))])
            dif = np.c_[dif_var, p_0]
            answer = np.append(answer, dif, axis=0)
            answer = answer[answer[:,0].argsort()]
            y.append(answer[:,1])
        y = np.array(y)
        return(y)

    # Функции оценки
    def _entropy(self, y):
        proba = self._get_proba(y)
        entropy = 0
        for p in proba:
            entropy -= p[1]*mt.log(p[1], 2)
        return(entropy)

    def _gini(self, y):
        proba = self._get_proba(y)
        gini = 1
        for p in proba:
            gini -= p[1]**2
        return(gini)

    def _variance(self, y):
        variance = y.std()**2
        return(variance)

    def _mad_median(self, y):
        sum_dif_median = (np.abs(y - np.median(y))).sum()
        mad_median = sum_dif_median/y.shape[0]
        return(mad_median)

    def _get_proba(self, y):
        val, count = np.unique(y, return_counts=True, axis=0)
        value_count = np.c_[val, count]
        count_y = y.shape[0]
        proba = np.c_[value_count[:,0], value_count[:,1]/count_y]
        return(proba)
    
    # Построение дерева
    def _information_gain(self, data, data_left, data_right):
        count = data.shape[0]
        count_left = data_left.shape[0]
        count_right = data_right.shape[0]
        fval = self.criterion_func(data)
        fval_left = self.criterion_func(data_left)
        fval_right = self.criterion_func(data_right)
        ig = fval - fval_left*count_left/count - fval_right*count_right/count
        return(ig)

    def _best_split(self, data):
        index_y = data.shape[1]-1
        best_split = {'ig': 0, 'column': 0, 'val': 0}
        for i in range(index_y):
            unique_val = np.unique(data[:, i], axis=0)
            unique_val = np.sort(unique_val)[:-1]
            for val in unique_val:
                data_left = data[data[:,i]<=val]
                data_right = data[data[:,i]>val]
                ig = self._information_gain(data[:, index_y], data_left[:, index_y], data_right[:, index_y])
                
                if ig > best_split['ig']:
                    best_split['ig'] = ig
                    best_split['column'] = i
                    best_split['val'] = val
        if best_split['ig'] == 0:
            return(False)
        else:
            return(best_split)

    def _chek_y(self, data):
        unique_val = np.unique(data[:,-1], axis=0)
        answer = True if unique_val.shape[0]>1 else False
        return(answer)

    def _get_tree(self, data, id_tree):
        split = data.shape[0]>=self.min_samples_split \
                    and self._chek_y(data) \
                    and self._best_split(data)
        if split and len(id_tree) < self.max_depth:
            # Деление ветвей
            id_tree_left = id_tree + '1'
            id_tree_right = id_tree + '2'
            tree = [[id_tree,
                    {'column': split['column'], 
                     'val': split['val'],
                     'id_left': id_tree_left,
                     'id_right': id_tree_right,
                     'is_leaf' : False,
                     'leaf_data': None}]]
            data_left = data[data[:,split['column']]<=split['val']]
            data_right = data[data[:,split['column']]>split['val']]
            tree.extend(self._get_tree(data_left, id_tree_left))
            tree.extend(self._get_tree(data_right, id_tree_right))
            return(tree)
        else:
            # Формирование листа дерева
            proba = self._get_proba(data[:,-1])
            tree = [[id_tree,
                    {'column': None, 
                     'val': None,
                     'id_left': None,
                     'id_right': None,
                     'is_leaf' : True,
                     'leaf_data': proba}]]
        return(tree)

    # Поиск решения по дереву
    def _get_leaf(self, line, id_tree):
        instruction = self.tree[self.tree[:,0]==id_tree][0][1]
        if instruction['is_leaf']:
            return(instruction['leaf_data'])
        else:
            if line[instruction['column']]<=instruction['val']:
                return(self._get_leaf(line, instruction['id_left']))
            else:
                return(self._get_leaf(line, instruction['id_right']))

    def _get_answer_val(self, answer_arr):
        if self.type_answer == 'max_count':
            answer = answer_arr[answer_arr[:,1].argsort()]
            answer = answer[-1][0]
            return(answer)
        elif self.type_answer == 'avg':
            answer = answer_arr[:,0]*answer_arr[:,1]
            answer = answer.sum()
            return(answer)