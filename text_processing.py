#######################
# Test Processing I   #
#######################

def normalize(input_string):
    normalized_string = ' '.join(input_string.rstrip().lstrip().split())
    return normalized_string.lower()

def no_vowels(input_string):
    res = []
    for i in range(len(input_string)):
        is_vowel = False
        for j in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            if input_string[i] == j:
                is_vowel = True
                break
        if not is_vowel:
            res.append(input_string[i])
    no_vowel_string = ''.join(res)
    return no_vowel_string
