

try:

    v1=int(input('Начальная скорость: '))
    v2=int(input('Конечная скорость: '))
    t=int(input('Время: '))


    def decorator(acceleration):
        def inner():
            acceleration()
            s=(v1*t)+((a*t**2)/2)
            print('Расстояние: ',round(s,2),' м')
        return inner


    def acceleration():
        global a
        a=(v2-v1)/t
        print('Ускорение: ',round(a,2),' м/с')

    acceleration=decorator(acceleration)
    acceleration()

except ZeroDivisionError:
    print('делить на 0 нельзя')
except ValueError:
    print('неправильный тип данных')

