# _*_ coding:utf-8 _*_
# FileName: str.py
# IDE: PyCharm

_str = str


class str(_str):
    __metaclass__ = _str

    @staticmethod
    def object2str(obj: (_str, int, bool, list, tuple, dict, set), skip_key: (list, tuple) = None):
        string = []
        if isinstance(obj, (list, tuple)):
            for o in obj:
                string.append(str.object2str(obj=o, skip_key=skip_key))
            string = f'[{", ".join(string)}]'
        elif isinstance(obj, set):
            for o in obj:
                string.append(str.object2str(obj=o, skip_key=skip_key))
            string = f'{{{", ".join(string)}}}'
        elif isinstance(obj, dict):
            for o in obj:
                if not (isinstance(skip_key, (list, tuple)) and o in skip_key):
                    string.append(f'{str.object2str(obj=o, skip_key=skip_key)}: {str.object2str(obj=obj[o], skip_key=skip_key)}')
            string = f'{{{", ".join(string)}}}'
        # elif isinstance(obj, (_str, int, bool)):
        else:
            string = repr(obj)
        return string

    def __init__(self, o: (object, bytes), encoding: _str = 'utf-8', errors: _str = 'strict'):
        if isinstance(o, bytes):
            self.__string = _str(o, encoding, errors)
        elif isinstance(o, object):
            self.__string = _str(o)  # self.object2str(o, skip_key=__import__('sys').argv.pop() if __import__('sys').argv else None)
        else:
            raise TypeError("Attribute o must be <class 'object'> or <class 'bytes'>")

    def __str__(self):
        return self.__string

    def __repr__(self):
        return self.__string

    def __setitem__(self, key: (int, slice), value: (object, bytes)):
        value = str(value)
        old = self.__string
        if isinstance(key, int):
            assert key < len(old), IndexError('string index out of range')
            assert len(value) == 1, ValueError('value length must be 1')
            self.__string = old[: key] + value + old[key + 1:]
        elif isinstance(key, slice):
            arange = list(range((key.start or 0), (key.stop or len(old)), (key.step or 1)))
            assert max(arange) < len(old) and min(arange) >= 0, IndexError('string index out of range')
            assert len(value) == len(arange), ValueError('length must be equal')
            for index, item in zip(arange, value):
                self.__string = old[: index] + item + old[index + 1:]
                old = self.__string
