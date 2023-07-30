from Operation import Operation

class Add(Operation):
    def execute(self):
        return self.operand1 + self.operand2