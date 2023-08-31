class Node:
    def __init__(self, first_num, operation, second_num):
        self.first_num = first_num
        self.operation = operation
        self.second_num = second_num

    def calc(self):
        if isinstance(self.first_num, Node):
            f_n = self.first_num.calc()
        else:
            f_n = self.first_num
        if isinstance(self.second_num, Node):
            s_n = self.second_num.calc()
        else:
            s_n = self.second_num

        print("calc:")
        if self.operation == "+":
            return self.first_num + self.second_num
        elif self.operation == "-":
            return self.first_num - self.second_num
        elif self.operation == "*":
            return self.first_num * self.second_num
        elif self.operation == "/":
            return self.first_num / self.second_num

        return None


# instance = Node(float(input("Input first number: ")), input("Input operation: "),
#                       float(input("Input second number: ")))
instance = Node(1,"+", (1+4))
print(instance.calc())
