
class Node:
    def __init__(self, f_list, operation):
        self.f_list = f_list
        self.operation = operation

    def calc(self):
        s = self.f_list[0]
        print("calc:")
        if self.operation == "+":
            for i in range(1, len(self.f_list)):
                s += self.f_list[i]
            return s
        elif self.operation == "-":
            for i in range(1, len(self.f_list)):
                s -= self.f_list[i]
            return s
        elif self.operation == "*":
            for i in range(1, len(self.f_list)):
                s *= self.f_list[i]
            return s
        elif self.operation == "/":
            for i in range(1, len(self.f_list)):
                s /= self.f_list[i]
            return s

        return None


# instance = Node(float(input("Input first number: ")), input("Input operation: "),
#                       float(input("Input second number: ")))
instance = Node([1, 2 ,3, 4],"/")
print(instance.calc())