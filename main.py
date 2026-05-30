def main():
    canvas = Canvas()
    
    while True:
        print()
        print(' Холст. Выберите действие, введя соответствующую цифру.')
        print('1. Добавить круг')
        print('2. Добавить прямоугольник')
        print('3. Добавить треугольник')
        print('4. Показать информацию о добавленных фигурах')
        print('5. Удалить фигуру')
        print('6. Показать общую площадь и периметр')
        print('7. Нарисовать все фигуры')
        print('0. Выход')
        print()
        
        choice = input('Ваш выбор: ')
        add_circle_choice = ['1','1.','1)']
        add_rectangle_choice = ['2','2.','2)']
        add_triangle_choice = ['3','3.','3)']
        show_info_choice = ['4','4.','4)']
        delete_choice = ['5','5.','5)']
        show_sum_info_choice = ['6','6.','6)']
        sign_choice = ['7','7.','7)']
        exit_choice = ['0','0.','0)']

        if choice in add_circle_choice:
            try:
                r = float(input('Введите числовое значение радиуса добавляемого круга: '))
                canvas.add_shape(Circle(r))
            except ValueError:
                print('Ошибка ввода. Попробуйте снова.')
        
        elif choice in add_rectangle_choice:
            try:
                w = float(input('Введите числовое значение ширины добавляемого прямоугольника: '))
                h = float(input('Введите числовое значение высоты добавляемого прямоугольника: '))
                canvas.add_shape(Rectangle(w, h))
            except ValueError:
                print('Ошибка ввода. Попробуйте снова.')
        
        elif choice in add_triangle_choice:
            try:
                a = float(input('Введите числовое значение первой стороны добавляемого треугольника: '))
                b = float(input('Введите числовое значение второй стороны добавляемого треугольника: '))
                c = float(input('Введите числовое значение третьей стороны добавляемого треугольника: '))
                canvas.add_shape(Triangle(a, b, c))
            except ValueError as e:
                print(f'Ошибка ввода: {e}. Попробуйте снова.')
        
        elif choice in show_info_choice:
            if len(canvas) == 0:
                print('Фигуры не добавлены')
            else:
                for i, shape in enumerate(canvas.get_shapes()):
                    print(f'{i}: {shape}')
        
        elif choice in delete_choice:
            if len(canvas) == 0:
                print('Фигуры не добавлены')
            else:
                try:
                    idx = int(input(f'Введите индекс удаляемой фигуры (диапазон: 0-{len(canvas)-1}): '))
                    canvas.remove_shape(idx)
                except ValueError:
                    print('Ошибка ввода. Попробуйте снова.')
                    continue
                    
        elif choice in show_sum_info_choice:
            print(f'Суммарная площать добавленных фигур: {canvas.total_area():.2f}')
            print(f'Суммарный периметр добавленных фигур: {canvas.total_perimeter():.2f}')
        
        elif choice in sign_choice:
            canvas.draw_all()
        
        elif choice in exit_choice:
            print('Работа программы завершена')
            break
        
        else:
            print('Ошибка ввода. Попробуйте снова.')

if __name__ == '__main__':
    main()