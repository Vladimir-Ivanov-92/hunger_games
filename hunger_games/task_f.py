import time


def runtime(method):
    """
    Вспомогательный декоратор будет декорировать каждый метод класса
    """
    def wrapper(*args, **kw):
        time_start = time.time()
        result = method(*args, **kw)
        time_stop = time.time()
        delta = (time_stop - time_start) * 1000
        print(f"{method.__name__} выполнялся {delta:.5f} ms")
        return result

    return wrapper


def runtime_all_methods(cls):
    """
    Основной декоратор к классу, который будет выводить в консоль время выполнения
    каждого метода.
    """
    class NewCls:
        def __init__(self, *args, **kwargs):
            # проксируем полностью создание класса
            # как создали этот NewCls, также создадим и декорируемый класс
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                # узнаем, является ли s нашим атрибутом (атрибут класса декоратора)
                x = super().__getattribute__(s)
            except AttributeError:
                # если нет, то пропускаем
                pass
            else:
                # если это атрибут класса декоратора - возвращаем и ничего не делаем
                return x
            # Иначе, вероятно, это атрибут исходного класса – получим его у него.
            attr = self._obj.__getattribute__(s)
            # метод ли он?
            if isinstance(attr, type(self.__init__)):
                # да, обернуть его в измеритель времени
                return runtime(attr)
            else:
                # не метод, что-то другое
                return attr

    return NewCls
