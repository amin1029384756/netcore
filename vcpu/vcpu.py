class VirtualCPU:
    def __init__(self):
        # Define two registers and a result register
        self.registerA = 0
        self.registerB = 0
        self.result = 0
        self.instruction_pointer = 0
        self.instructions = []

    def load(self, register, value):
        if register == 'A':
            self.registerA = value
        elif register == 'B':
            self.registerB = value

    def add(self):
        self.result = self.registerA + self.registerB

    def subtract(self):
        self.result = self.registerA - self.registerB

    def multiply(self):
        self.result = self.registerA * self.registerB

    def divide(self):
        if self.registerB != 0:
            self.result = self.registerA / self.registerB
        else:
            print("Error: Division by zero!")
            self.halt()

    def jump(self, condition, address):
        if condition == 'zero' and self.result == 0:
            self.instruction_pointer = address
        elif condition == 'positive' and self.result > 0:
            self.instruction_pointer = address
        elif condition == 'negative' and self.result < 0:
            self.instruction_pointer = address

    def halt(self):
        self.instruction_pointer = len(self.instructions)

    def execute(self, instructions):
        self.instructions = instructions
        while self.instruction_pointer < len(self.instructions):
            instruction = self.instructions[self.instruction_pointer]
            if instruction[0] == 'LOAD':
                self.load(instruction[1], instruction[2])
            elif instruction[0] == 'ADD':
                self.add()
            elif instruction[0] == 'SUB':
                self.subtract()
            elif instruction[0] == 'MUL':
                self.multiply()
            elif instruction[0] == 'DIV':
                self.divide()
            elif instruction[0] == 'JUMP':
                self.jump(instruction[1], instruction[2])
            elif instruction[0] == 'HALT':
                self.halt()
            self.instruction_pointer += 1

    def print_register(self, register):
        if register == 'A':
            print(self.registerA)
        elif register == 'B':
            print(self.registerB)
        elif register == 'result':
            print(self.result)