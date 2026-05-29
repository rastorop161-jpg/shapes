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

class Canvas:
    """Управляет коллекцией фигур и операциями над ними"""
    
    def __init__(self):
        self._shapes = []  # инкапсуляция — список фигур скрыт
    
    def add_shape(self, shape: Shape):
        """Добавляет фигуру на холст (полиморфизм на входе)"""
        self._shapes.append(shape)
        print(f"✓ Добавлена: {shape}")
    
    def remove_shape(self, index: int):
        """Удаляет фигуру по индексу"""
        if 0 <= index < len(self._shapes):
            removed = self._shapes.pop(index)
            print(f"✗ Удалена: {removed}")
        else:
            print("Неверный индекс")
    
    def total_area(self) -> float:
        """Суммарная площадь всех фигур"""
        return sum(shape.area() for shape in self._shapes)
    
    def total_perimeter(self) -> float:
        """Суммарный периметр всех фигур"""
        return sum(shape.perimeter() for shape in self._shapes)
    
    def draw_all(self):
        """Отрисовывает все фигуры"""
        if not self._shapes:
            print("Холст пуст")
            return
        for i, shape in enumerate(self._shapes):
            print(f"\n--- Фигура {i} ({shape.__class__.__name__}) ---")
            print(shape.draw())
            print(shape)
    
    def get_shapes(self):
        """Возвращает список фигур (для итерации)"""
        return self._shapes.copy()
    
    def __len__(self):
        return len(self._shapes)