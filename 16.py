# 375/412
# 30:59/39:27
from sys import stdin
from math import prod

data = list(stdin.read().strip())
m = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}
bits = ''.join(m[c] for c in data)

class Packet:
    def __init__(self, data):
        self.data = data
        self.v = int(self.data[:3], 2)
        self.skip(3)
        self.t = int(self.data[:3], 2)
        self.skip(3)
        self.subpackets = []
        self.evaluate()

    def skip(self, n):
        self.data = self.data[n:]

    def literal(self):
        assert self.t == 4
        b = ''
        while True:
            x = self.data[0] 
            b += self.data[1:5]
            self.skip(5)
            if x == '0':
                break
        self.value = int(b, 2)

    def operator(self):
        assert self.t in [0, 1, 2, 3, 5, 6, 7]
        if self.t == 0:
            self.value = sum(p.value for p in self.subpackets)
        elif self.t == 1:
            self.value = prod(p.value for p in self.subpackets)
        elif self.t == 2:
            self.value = min(p.value for p in self.subpackets)
        elif self.t == 3:
            self.value = max(p.value for p in self.subpackets)
        elif self.t == 5:
            assert len(self.subpackets) == 2
            self.value = int(self.subpackets[0].value > self.subpackets[1].value)
        elif self.t == 6:
            assert len(self.subpackets) == 2
            self.value = int(self.subpackets[0].value < self.subpackets[1].value)
        elif self.t == 7:
            assert len(self.subpackets) == 2
            self.value = int(self.subpackets[0].value == self.subpackets[1].value)

    def read_0(self):
        assert self.t != 4
        assert self.data[0] == '0'
        self.skip(1)
        l = int(self.data[:15], 2)
        self.skip(15)
        sub = self.data[:l]
        self.skip(l)
        while sub:
            p = Packet(sub)
            sub = p.data
            self.subpackets.append(p)
    
    def read_1(self):
        assert self.t != 4
        assert self.data[0] == '1'
        self.skip(1)
        l = int(self.data[:11], 2)
        self.skip(11)
        for _ in range(l):
            p = Packet(self.data)
            self.data = p.data
            self.subpackets.append(p)

    def evaluate(self):
        if self.t == 4:
            return self.literal()
        
        if self.data[0] == '0':
            self.read_0()
        else:
            self.read_1()

        return self.operator()
    
    def version_sum(self):
        return self.v + sum(p.version_sum() for p in self.subpackets)

p = Packet(bits)
print('a', p.version_sum())
print('b', p.value)
