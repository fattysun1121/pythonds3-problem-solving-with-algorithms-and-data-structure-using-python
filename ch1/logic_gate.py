class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin_a = None
        self.pin_b = None

    def set_pin(self, a):
        if self.pin_a is None:
            self.pin_a = a
        elif self.pin_b is None:
            self.pin_b = a

    def get_pin_a(self):
        if self.pin_a is None:
            return int(input(f'Enter pin A input for gate {self.get_label()}: '))
        elif type(self.pin_a) == int:
            return self.pin_a
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b is None:
            return int(input(f'Enter pin B input for gate {self.get_label()}: '))
        elif type(self.pin_b) == int:
            return self.pin_b
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        else:
            if self.pin_b is None:
                self.pin_b = source
            else:
                raise RuntimeError('Error: NO EMPTY PINS')


class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input(f'Enter pin input for gate {self.get_label()}: '))
        return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError('Error: NO EMPTY PINS')


class AndGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return a and b


class OrGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return a or b


class NotGate(UnaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        return 1


class NorGate(OrGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic():
            return 0
        return 1


class NandGate(AndGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic():
            return 0
        return 1


class XorGate(OrGate):
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if (a, b) == (1, 1):
            return 0
        return a or b


class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)
        fgate.set_output_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def main():
    print('case 1: ')
    g1 = AndGate('G1')
    g2 = AndGate('G2')
    g3 = NorGate('G3')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    print(g3.get_output())
    print('case 2: ')
    g1 = NandGate('G1')
    g2 = NandGate('G2')
    g3 = AndGate('G3')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    print(g3.get_output())


class HalfAdder(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.sum = None
        self.carry = None

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        self.carry = a and b
        if a == 1 and b == 1:
            self.sum = 0
        else:
            self.sum = a or b
        print(self.sum)
        return self.carry


class FullAdder(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.x1 = XorGate('X1')
        self.x2 = XorGate('X2')
        self.a1 = AndGate('A1')
        self.a2 = AndGate('A2')
        self.o1 = OrGate('O1')
        c1 = Connector(self.x1, self.x2)
        c2 = Connector(self.x1, self.a1)
        c3 = Connector(self.a1, self.o1)
        c4 = Connector(self.a2, self.o1)

    def perform_gate_logic(self):
        # import pdb
        # pdb.set_trace()
        carry_in = self.carry_in.get_from().get_output()
        a = int(input('Enter pin A: '))
        b = int(input('Enter pin B: '))

        self.x1.set_pin(a)
        self.x1.set_pin(b)
        self.a2.set_pin(a)
        self.a2.set_pin(b)
        self.x2.set_pin(carry_in)
        self.a1.set_pin(carry_in)
        self.sum = self.x2.get_output()
        self.carry = self.o1.get_output()
        print(self.sum)
        return self.carry

    def set_next_pin(self, source):
        self.carry_in = source


class EightBitFullAdder():
    def __init__(self, lbl):
        self.label = lbl
        self.h1 = HalfAdder('H1')
        self.f1 = FullAdder('F1')
        self.f2 = FullAdder('F2')
        self.f3 = FullAdder('F3')
        self.f4 = FullAdder('F4')
        self.f5 = FullAdder('F5')
        self.f6 = FullAdder('F6')
        self.f7 = FullAdder('F7')
        c1 = Connector(self.h1, self.f1)
        c2 = Connector(self.f1, self.f2)
        c3 = Connector(self.f2, self.f3)
        c4 = Connector(self.f3, self.f4)
        c5 = Connector(self.f4, self.f5)
        c6 = Connector(self.f5, self.f6)
        c7 = Connector(self.f6, self.f7)

    def perform_addition(self):
        return self.f7.get_output()


e = EightBitFullAdder('E1')
print(e.perform_addition())
