class CollatzStatistics:
    def output_number(self, n):
        self.max = max(self.max, n)
        self.count += 1

    def output_wrapper(self, func):
        self.max = 0
        self.count = 0
        func(self)
        print(f"Max value reached: {self.max}")
        print(f"Sequence length: {self.count}")
