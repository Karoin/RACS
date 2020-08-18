class ABC:
    def a(self):
        self.data = 1
        DATA = 3
    def b(self):
        self.data = 2
        DATA = 5

classia = ABC()

classia.a()
classia.b()
classia.a()
print(classia.data)
