def reading_time(text):
    words = text.split()
    if text == "" or text == " ":
        return "Number of words cannot be less than 1"
    else:
        return len(words)/200
    
def check_grammar(text):
    if text[0].isupper():
        return text[-1] in ".?!"
    else:
        return False
