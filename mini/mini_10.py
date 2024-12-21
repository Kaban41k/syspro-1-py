def singleton(class_to_decorate):
    class SingletonClass(class_to_decorate):
        instance = None

        def __new__(cls, *args, **kwargs):
            if SingletonClass.instance is None:
                SingletonClass.instance = super().__new__(cls)
            return SingletonClass.instance

        def __init__(self, *args, **kwargs):
            try:
                if self._inited:
                    return
            except:
                self._inited = True

            super().__init__(*args, **kwargs)
    return SingletonClass


@singleton
class Node:
    def __init__(self, x):
        self.x = x
        print("Hello from init")
    pass


a = Node(1)
b = Node(2)

assert a.x == b.x, "Wrong answer"
assert a is b, "Wrong answer"

print("ALL TESTS PASSED :D")
