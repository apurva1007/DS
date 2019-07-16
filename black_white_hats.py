import random


class BlackWhiteHats:
    colors = []
    responses = []
    n = 0

    def __init__(self, n):
        self.n = n
        for i in range(self.n):
            self.colors.append(random.randrange(0, 2))

        print("colours:", self.colors)

    def get_count(self, start, color):
        counter = 0
        for i in range(start, self.n):
            if self.colors[i] == color:
                counter += 1
        return counter

    # [1, 1, 0, 1, 0, 1, 0, 0, 0, 0]

    def get_first_colour(self):
        white_counter = self.get_count(1, 1)
        black_counter = self.get_count(1, 0)
        if white_counter % 2 == 0:
            self.responses.append(1)
        else:
            self.responses.append(0)
        # if self.first_response != self.colors[0]:
        # 	self.colors.pop(0)

    def get_next(self):
        i = 1
        while i < self.n:
            count_next = self.get_count(i + 1, self.responses[0])
            count_prev = self.responses[1:i].count(self.responses[0])
            total_count = count_next + count_prev
            # print(i, count_prev, count_next, total_count)
            if total_count % 2 != 0:
                self.responses.append(self.responses[0])
            else:
                self.responses.append(int(not(self.responses[0])))
            i += 1
        print("responses:", self.responses)

    def kill(self):
        temp = []
        for i in range(0, self.n):
            if self.colors[i] != self.responses[i]:
                temp.append(i)
        print("Killed :", temp)


bw = BlackWhiteHats(10)
bw.get_first_colour()
bw.get_next()
bw.kill()
