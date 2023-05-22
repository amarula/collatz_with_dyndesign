import matplotlib.pyplot as plt

class CollatzGraph:
    def output_number(self, n):
        self.sequence.append(n)

    def output_wrapper(self, func):
        self.sequence = []
        func(self)
        plt.plot(self.sequence)
        plt.xlabel("Step")
        plt.ylabel("Value")
        plt.title(f"{self.FUNCTION_NAME} Function")
        plt.show()
