class CollatzSequence:
    FUNCTION_NAME = 'Collatz'

    def __init__(self, args):
        self.n = int(args.n)

    def get_next_n(self, n):
        if n % 2 == 0:
            return n // 2
        else:
            return n*3 +1

    def get_collatz_sequence(self, n):
        while n != 1:
            n = self.get_next_n(n)
            yield n
