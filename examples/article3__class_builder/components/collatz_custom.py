class CollatzCustom:
    FUNCTION_NAME = 'Collatz-like ternary'

    def get_next_n(self, n):
        if n % 3 == 0:
            return n // 3
        elif n % 3 == 1:
            return n*2 +1
        else:
            return n*3 -2
