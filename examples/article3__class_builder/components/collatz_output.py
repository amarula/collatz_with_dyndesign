from dyndesign import decoratewith

class CollatzOutput:
    def output_number(self, n):
        print(f"{n}; ", end='')

    @decoratewith("output_wrapper")
    def output_sequence(self):
        print(f"{self.FUNCTION_NAME} sequence starting from {self.n} is:")
        self.output_number(self.n)
        for n in self.get_collatz_sequence(self.n):
            self.output_number(n)
        print()
