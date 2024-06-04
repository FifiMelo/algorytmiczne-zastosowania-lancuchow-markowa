import cryptography
import numpy as np


if __name__ == '__main__':
    print(
        """Please tell me path to the .txt file with source text.
(big amount of text is required)"""
        )
    file_path = input()
    text = open(file_path, encoding="utf8").read().lower().replace('\n', ' ').replace('\r', '')
    print(
        """Tell me the index under which data will be saved"""
        )
    output_file_name = input()
    print("Please wait...")
    adjacency_matrix = cryptography.adjecency_matrix(text)
    vect = cryptography.distribution_vector(text)
    np.save(f"./temp/{output_file_name}_adjacency_matrix.npy", adjacency_matrix)
    np.save(f"./temp/{output_file_name}_distribution_vector.npy", vect)
    print("Done!")