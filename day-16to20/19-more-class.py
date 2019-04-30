"""
Day 19
面向对象
"""

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass
class Manager(Employee):
    def get_salary(self):
        return 15000.0
class Programmer(Employee):
    def __init__(self, name, working_hour = 0):
        super().__init__(name)
        self.working_hour = working_hour
    def get_salary(self):
        return 200.0 * self.working_hour
class Salesman(Employee):
    def __init__(self, name, sales = 0.0):
        super().__init__(name)
        self.sales = sales
    def get_salary(self):
        return 1800.0 + self.sales * 0.05
class EmployeeFactory():
    @staticmethod
    def create(emp_type, *args, **kwargs):
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp

def employee_test():
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary() }元')

class SetOnceMappingMixin():
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key, value)
class SetOnceDict(SetOnceMappingMixin, dict):
    pass

def set_once_dict_test():
    my_dict = SetOnceDict()
    try:
        my_dict['username'] = 'jackfrued'
        my_dict['username'] = 'hellokitty'
    except KeyError:
        pass
    print(my_dict)

import threading
class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.Lock()
        super().__init__(*args, **kwargs)
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance
class President(metaclass=SingletonMeta):
    pass

class StreamHasher():
    def __init__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg.lower())()
    def __call__(self, stream):
        return self.to_digest(stream)
    def to_digest(self, stream):
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()
def hash_test():
    hasher1 = StreamHasher()
    with open('./res/ball.png', 'rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open('./res/ball.png', 'rb') as stream:
        print(hasher2(stream))

if __name__ == '__main__':
    employee_test()
    set_once_dict_test()
    hash_test()