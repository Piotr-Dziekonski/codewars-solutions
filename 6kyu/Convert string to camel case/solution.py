def to_camel_case(text):
    for c in range(0,len(text)):
        if text[c] in ["-","_"]:
            text = list(text)
            text[c+1] = text[c+1].upper()
            text = ''.join(text)
    text = text.replace("-","").replace("_","")
    return text