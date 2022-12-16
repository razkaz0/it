class Singleton:
    instance = None

    def new(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).new(cls)
        return cls.instance


obj1 = Singleton()
obj2 = Singleton()

print(f'{obj1 is obj2}\n {obj1}\n {obj2}')