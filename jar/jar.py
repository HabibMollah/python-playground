def main():
    jar = Jar()

    print(str(jar.capacity))
    print(str(jar))

    jar.deposit(2)
    print(str(jar))

    jar.withdraw(1)
    print(str(jar))

    jar.withdraw(1)
    print(str(jar))

    jar.deposit(12)
    print(str(jar))

    jar.deposit(1)
    print(str(jar))


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity must be a positive integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("cannot deposit, not enough capacity")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("cannot withdraw, not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


main()
