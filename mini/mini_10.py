def singleton(class_to_decorate):
    class SingletonClass(class_to_decorate):
        instance = None

        def __new__(cls):
            if SingletonClass.instance is None:
                SingletonClass.instance = super().__new__(cls)
            return SingletonClass.instance
    return SingletonClass


@singleton
class Node():
    pass


a = Node()
b = Node()

print(a)
print(b)
print(a is b)
