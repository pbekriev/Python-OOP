class Person:
   min_age = 0
   max_age = 150

   def __init__(self, name, age):
      self.name = name
      self.age = age

   @classmethod
   def __validate_age(cls, value):
      raise ValueError(f'{value} must be between '
                       f'{cls.min_age} and {cls.max_age}')

   @property
   def age(self):
       return self.__age

   @age.setter
   def age(self, value):
       self.__validate_age(value)
       self.__age = value


class Employee(Person):
    min_age = 16
    max_age = 150

    def __init__(self, name, age):
        super().__init__(name, age)


print(Employee._Person__validate_age(10))