class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "\U0001F36A" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("No space to add more cookies")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("No enough cookies to withdraw")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Jar cannot be created")
        self._capacity = capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(12)
    jar.deposit(2)
    print(jar)
    jar.deposit(4)
    print(jar)

if __name__ == "__main__":
    main()
