from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Абстрактный базовый класс для всех фигур"""
    
    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Вычисляет периметр фигуры"""
        pass
    
    @abstractmethod
    def draw(self) -> str:
        """Возвращает текстовое представление фигуры (для консольной отрисовки)"""
        pass
    
    def __str__(self) -> str:
        """Красивый вывод информации о фигуре"""
        return f"{self.__class__.__name__}: площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def draw(self) -> str:
    return '◉'

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def draw(self) -> str:
    return '█'

class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.a = side_a
        self.b = side_b
        self.c = side_c
        # Проверка на существование треугольника
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            raise ValueError("Треугольник с такими сторонами не существует")
    
    def area(self) -> float:
        # Формула Герона
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def draw(self) -> str:
    return '▲'
