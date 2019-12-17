class ClassExample:
    classattr = 'A'
    def mthd(self):
        self.__class__.classattr = 'B'
        return 'instance method', self

    @classmethod
    def classmthd(cls):
        return 'class method', cls

    # independent from everything around it
    # method won't modify class ofr instance state
    #  in practice they often help avoid accidental modifications going against the original design.
    @staticmethod
    def staticmthd():
        return 'static method'

if __name__ == "__main__":
    c = ClassExample()
    print(c.classattr)
    print(c.mthd())
    print(c.classattr)
    print(c.classmthd())
    print(c.staticmthd())

