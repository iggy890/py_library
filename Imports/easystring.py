# String matches function
def get_string_matches(string: str, string2: str):
    matches = 0
    string, string2 = string.lower(), string2.lower()

    for i in string:
        for j in string2:
            if i == j:
                matches += 1

    return matches