class User:
    def __init__(self):
        self.pr = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        if rank in self.pr:
            if rank == self.rank:
                self.progress += 3
            elif self.pr.index(rank) == self.pr.index(self.rank) - 1:
                self.progress += 1
            elif rank < self.rank - 1:
                self.progress += 0
            elif rank > self.rank:
                difference_in_rank = self.pr.index(rank) - self.pr.index(self.rank)
                self.progress += 10 * difference_in_rank * difference_in_rank

            while self.progress >= 100 and self.rank < 8:
                self.progress -= 100
                if self.rank == -1:
                    self.rank = 1
                else:
                    self.rank += 1
            if self.rank == 8:
                self.progress = 0
        else:
            raise ValueError("Rank Invalido")


pessoa1 = User()

pessoa1.inc_progress(1)
pessoa1.inc_progress(1)
pessoa1.inc_progress(1)
pessoa1.inc_progress(1)
pessoa1.inc_progress(1)
pessoa1.inc_progress(2)
pessoa1.inc_progress(2)
pessoa1.inc_progress(-1)
print(pessoa1.rank)
print(pessoa1.progress)
