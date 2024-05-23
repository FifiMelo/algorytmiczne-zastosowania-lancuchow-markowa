from permutation import Permutation, create_identity, create_random_permutation

chars = 'abcdefghijklmnopqrstuvwxyz0123456789 ,.?!:;'

def encode_text(text: str, permutation: Permutation) -> str:
    out = list(text)
    for i in range(len(out)):
        out[i] = chars[permutation(chars.find(text[i].lower()))]
    return "".join(out)


    

