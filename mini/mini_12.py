def coroutine(f):
    def gen_with_next(*args, **kwargs):
        gen = f(*args, **kwargs)
        next(gen)
        return gen

    return gen_with_next


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
print(st.send(42))  # False
print(st.send(42))  # True
