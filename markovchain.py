from permutation import Permutation, create_identity
import random
import copy


class MarkovChain:
    """
    This is the markov chain with State Space of all passible permutations (see module permutation)
    """
    def __init__(self, initial_state: Permutation = None):
        self.state = initial_state
        if self.state is None:
            self.state = create_identity(len(Permutation.chars))
        self.new_state = None

    def propose_move(self) -> Permutation:
        indexes = random.sample(range(self.state.n), 2)
        self.new_state = copy.deepcopy(self.state)
        self.state.modify(indexes[0], indexes[1])
        return self.new_state
    
    def accept_proposal(self) -> None:
        self.state = copy.deepcopy(self.new_state)
        self.new_state = None
        
    def reject_proposal(self) -> None:
        self.new_state = None
