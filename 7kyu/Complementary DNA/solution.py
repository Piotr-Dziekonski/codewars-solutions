def DNA_strand(dna):
    output = ""
    for c in dna:
        if c == "A":
            output += "T"
        elif c == "T":
            output += "A"
        elif c == "G":
            output += "C"
        elif c == "C":
            output += "G"
    return output