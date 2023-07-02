class Test:
    def __init__(self, name: str, age: int, jobs: list = None) -> None:
        self.name = name
        self.age = age
        self.jobs = jobs

    def display(self) -> None:
        print("My name is %s, I am %d years old" % (self.name, self.age))


def main() -> None:
    t = Test("Marcel", 10)
    t.display()


if __name__ == "__main__":
    main()
