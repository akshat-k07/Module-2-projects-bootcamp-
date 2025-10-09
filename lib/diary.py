def make_snippet(text):
    words = text.split()
    if len(words) == 0:
        return "Text cannot be empty"
    elif len(words) < 6 and len(words) != 0:
        return text
    else:
        snippet = words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " ..."
        return snippet