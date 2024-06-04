import markovchain
import permutation
import cryptography
import numpy as np
import random

def main():
    text = open("tekst_polski.txt", encoding="utf8").read().lower().replace('\n', ' ').replace('\r', '')

    P = permutation.create_random_permutation()
    encrypted_text = cryptography.encode_text(text, P)
    print(encrypted_text)

    MCMC = markovchain.MarkovChain(permutation.create_random_permutation())
    MCMC.load_adjacecny_matrix("./temp/60_adjacency_matrix.npy")
    MCMC.load_encrypted_text(encrypted_text)
    MCMC.load_distribution_vector("./temp/60_distribution_vector.npy")

    T=5300  #np. 87300 dla polskiego najdłuszego
    beta = 1/T 

    for i in range(10000):
        #T=1-(i+1)/4002
        #beta = 1/T                       #1- (k+1)/kmax )
        # obliczamy likelihood przed ruchem
        L1 = MCMC.LOSS(MCMC.get_state())
        if i%100 == 0:
            print(f"Iterations: {i}\nLogLikelihood: {L1}")

        proposal = MCMC.propose_move()

        # obliczamy likelihood proponowanego ruchu
        L2 = MCMC.LogLikelihood(proposal)

        alpha = min(1, np.exp(beta*(L2 - L1)))
        if alpha > random.uniform(0, 1):
            MCMC.accept_proposal()
            
        else:
            MCMC.reject_proposal()
            
        
        beta=beta*1.23    #np. *1.24 dla polskiego najdłuzszego
    print(MCMC.get_state() * P)
    print(cryptography.encode_text(encrypted_text, MCMC.get_state()))




if __name__ == '__main__':
    main()
