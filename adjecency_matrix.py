import cryptography
import numpy as np


if __name__ == '__main__':
    print(
        """Please tell me path to the .txt file with source text.
(big amount of text is required)"""
        )
    file_path = input()
    text = open(file_path, encoding="utf8").read().lower()
    print(
        """Tell me the name of file to save which adjacency in."""
        )
    adjacency_matrix_file_name = input()
    print("Please wait...")
    adjacency_matrix = cryptography.adjecency_matrix(text)
    np.save(f"{adjacency_matrix_file_name}.npy", adjacency_matrix)
    print("Done!")