class FreqStack:

    def __init__(self):
        self.stack = []
        # { val: freq }
        self.freqMap = defaultdict(int)
        # { freq: [vals] }
        self.group = defaultdict(list)
        # max freq
        self.maxFreq = 0

        # freq[val] = current frequency
        # group[freq] = stack of values with that frequency
        # maxFreq = highest frequency seen

    def push(self, val: int) -> None:
        self.freqMap[val] += 1
        f = self.freqMap[val]
        self.group[f].append(val)
        self.maxFreq = max(self.maxFreq, f)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freqMap[val] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()