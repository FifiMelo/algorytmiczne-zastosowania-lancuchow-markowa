import markovchain
import permutation
import cryptography
import numpy as np
import random

def main():
    text = open("text.txt", encoding="utf8").read().lower()

    P = permutation.create_random_permutation()
    encrypted_text = cryptography.encode_text(text, P)

    MCMC = markovchain.MarkovChain(permutation.create_random_permutation())
    MCMC.load_adjacecny_matrix("./temp/adjacency_matrix.npy")
    MCMC.load_encrypted_text(encrypted_text)

    beta = 0.2

    for i in range(6000):

        # obliczamy likelihood przed ruchem
        L1 = MCMC.LOSS(MCMC.get_state())
        print(L1)

        MCMC.propose_move()

        # obliczmy likelihood proponowanego ruchu
        L2 = MCMC.LOSS(MCMC.new_state)

        alpha = min(1, np.exp(beta*(L2 - L1)))
        if alpha > random.uniform(0, 1):
            MCMC.accept_proposal()
        else:
            MCMC.reject_proposal()
    print(MCMC.get_state() * P)
    print(cryptography.encode_text(encrypted_text, MCMC.get_state()))

        
        

    



if __name__ == '__main__':
    main()
