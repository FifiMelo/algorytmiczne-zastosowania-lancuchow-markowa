import markovchain
import permutation
import cryptography
import numpy as np
import random

def main():
    MCMC = markovchain.MarkovChain(permutation.create_random_permutation())
    text = open("text.txt", encoding="utf8").read().lower()
    encrypted_text = cryptography.encode_text(text, permutation.create_random_permutation())
    adjacency_matrix = np.load("adjacency_matrix.npy")
    beta = 0.2

    for i in range(3000):

        # obliczamy likelihood przed ruchem
        decrypted_text1 = cryptography.encode_text(encrypted_text, MCMC.get_state())
        L1 = cryptography.likelihood(adjacency_matrix, decrypted_text1)
        print(L1)

        MCMC.propose_move()

        # obliczmy likelihood proponowanego ruchu
        decrypted_text2 = cryptography.encode_text(encrypted_text, MCMC.new_state)
        L2 = cryptography.likelihood(adjacency_matrix, decrypted_text2)

        alpha = min(1, np.exp(beta*(L2 - L1)))
        if alpha > random.uniform(0, 1):
            MCMC.accept_proposal()
        else:
            MCMC.reject_proposal()
    print(MCMC.get_state())
    print(cryptography.encode_text(encrypted_text, MCMC.get_state()))

        
        

    



if __name__ == '__main__':
    main()
