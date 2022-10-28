def decor_int(func):
    def wraper(object,other):
        if type(other) == int:
            return func(object, other)
        else:
            d={'один':1,'два':2,'три':3,'четыре':4,'пять':5,'1':1,'2':2,'3':3,'4':4,'5':5}
            if other in d:
                rez= func(object,d[other])
            else:
                raise TypeError('справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.')
                rez= func(object,0)
            return rez
    return wraper

class Int(int):
    @decor_int
    def __add__(self, other):
        return super().__add__(other)

def iss(x, y):
    id_x = id(x)
    id_y = id(y)
    strs = ''
    if id_x == id_y:
        strs = 'Две переменные ссылаются на один и тот же адрес в памяти,'
    else:
        strs = 'Две переменные ссылаются на разные адреса в памяти,'
    if x == y:
        strs += ' имеют одинаковые значения.'
    else:
        strs += ' имеют разные значения.'
    print(strs)
    print(f'id первой переменной: {id_x}')
    print(f'id второй переменной: {id_y}')
    print(f'Значение первой переменной: {x}')
    print(f'Значение второй переменной: {y}')

if __name__ == '__main__':

    x = [1, [2]]
    y = x.copy()
    y[1] = 2
    iss(x, y)

    x = Int(5)

    print( x + 'два' )

    print(x + '1')

    print(x + 7)

    print( x + 'шесть')







