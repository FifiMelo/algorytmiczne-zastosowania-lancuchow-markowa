import random




class Permutation:
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789 ,.?!:;'
    def __init__(self, indexes: list[int]):
        self.indexes = indexes
        self.n = len(self.indexes)

    def __str__(self):
        out = []
        if self.n == len(Permutation.chars):
            for i in range(self.n):
                out.append(f"{Permutation.chars[i]} -> {Permutation.chars[self(i)]}")
        else:
            for i in range(self.n):
                out.append(f"{i} -> {self(i)}")
        return "\n".join(out)
    
    def __repr__(self) -> str:
        return f"Permutation(n = {self.n})"
    
    def __mul__(self, other: 'Permutation') -> 'Permutation':
        assert self.n == other.n
        return Permutation([self(other(i)) for i in range(self.n)])

    def inverse(self) -> 'Permutation':
        out = [0 for i in range(self.n)]
        for i in range(self.n):
            out[self(i)] = i
        return Permutation(out)
    
    def modify(self, index1: int, index2: int) -> None:
        self.indexes[index2], self.indexes[index1] = self(index1), self(index2)
        
    
    def __call__(self, k: int)->int:
        return self.indexes[k]

    
def create_identity(n: int = len(Permutation.chars)) -> Permutation:
    return Permutation([i for i in range(n)])

def create_random_permutation(n: int = len(Permutation.chars)) -> Permutation:
    L = list(range(n))
    random.shuffle(L)
    return Permutation(L)

