class PresentFactory:
    def __init__(self, presents):
        self.presents = presents

    def __repr__(self):
        return f'{self.presents}'

    @classmethod
    def wedding(cls):
        return cls(['money', 'letter'])

    @classmethod
    def birthday(cls):
        return cls(['letter', 'toy'])

# self documenting and simplify 가능
if __name__ == "__main__":
    wedding_present = PresentFactory.wedding()
    print(wedding_present)
    birthday_present = PresentFactory.birthday()
    print(birthday_present)
