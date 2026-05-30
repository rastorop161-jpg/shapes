from abc import ABC, abstractmethod
import math

class Shape(ABC):
    'Абстрактный базовый класс для всех фигур'
    
    @abstractmethod
    def area(self) -> float:
        'Вычисляет площадь фигуры'
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        'Вычисляет периметр фигуры'
        pass
    
    @abstractmethod
    def draw(self) -> str:
        'Выводит знак фигуры'
        pass

class Circle(Shape):
    'Класс для кругов'
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def draw(self) -> str:
        return '◉'

    def __str__(self) -> str:
        'Возвращает информацию о круге'
        return f"{self.__class__.__name__}: радиус = {self.radius:.2f}, площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

class Rectangle(Shape):
    'Класс для прямоугольников'
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def draw(self) -> str:
        return '█'

    def __str__(self) -> str:
        'Возвращает информацию о прямоугольнике'
        return f"{self.__class__.__name__}: ширина = {self.width:.2f}, высота = {self.height:.2f} площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

class Triangle(Shape):
    'Класс для треугольников'
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.a = side_a
        self.b = side_b
        self.c = side_c
        # Проверка на существование треугольника
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            raise ValueError('Треугольник с такими сторонами не существует')
    
    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def draw(self) -> str:
        return '▲'

    def __str__(self) -> str:
        'Возвращает информацию о треугольнике'
        return f"{self.__class__.__name__}: сторона a = {self.a:.2f}, сторона b = {self.b:.2f}, сторона c = {self.c:.2f}, площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

class Canvas:
    'Управляет содержимым холста'
    
    def __init__(self):
        self._shapes = []
    
    def add_shape(self, shape: Shape):
        'Добавляет фигуру на холст'
        self._shapes.append(shape)
        print(f"Добавлена: {shape}")
    
    def remove_shape(self, index: int):
        'Удаляет фигуру с выбранным индексом с холста'
        if 0 <= index < len(self._shapes):
            removed = self._shapes.pop(index)
            print(f'Удалена: {removed}')
        else:
            print('Неверный индекс')
    
    def total_area(self) -> float:
        'Возвращает сумму площадей добавленных фигур'
        return sum(shape.area() for shape in self._shapes)
    
    def total_perimeter(self) -> float:
        'Возвращает сумму периметров добавленных фигур'
        return sum(shape.perimeter() for shape in self._shapes)
    
    def draw_all(self):
        'Выводит пронумерованные знаки добавленных фигур'
        if not self._shapes:
            print('Фигуры не добавлены')
            return
        for i, shape in enumerate(self._shapes, start = 1):
            print(f'\n{i} - ({shape.__class__.__name__})')
            print(shape.draw())
            print(shape)
    
    def get_shapes(self):
        'Возвращает копию списка добавленных фигур'
        return self._shapes.copy()
    
    def __len__(self):
        'Адаптирует встроенную функцию len для пользовательского типа canvas'
        return len(self._shapes)