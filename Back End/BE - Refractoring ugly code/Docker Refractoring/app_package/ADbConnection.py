from abc import ABC, abstractmethod


class ADbConnection(ABC):
    @abstractmethod
    def exec_sql(self, raw_sql, params):
        pass

    @property
    @abstractmethod
    def cursor(self):
        return None
