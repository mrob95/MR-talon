from talon.voice import Str


def remove_dragon_junk(word):
    if word == ".\\point\\point":
        return "point"
    elif word == ".\\period\\period":
        return "period"
    elif word == "i\\pronoun":
        return "i"
    else:
        return str(word).lstrip("\\").split("\\", 1)[0].replace("-", " ").strip()

def format_text(text, capitalisation=0, spacing=0):
    if not text: return
    if capitalisation == 0:
        capitalisation = 5
    if spacing == 0 and capitalisation == 3:
        spacing = 1

    if capitalisation == 6:
        text = "".join(text.split(" "))
        text = text.lower()
        punc = "@1/4#9?5%,."
        result = []
        for i in range(len(text)):
            if i%2==0:
                result.append(punc[(i//2)%len(punc)])
            if i%3==0:
                result.append(text[i].upper())
            else:
                result.append(text[i])
        text = "".join(result)
    elif capitalisation != 0:
        if capitalisation == 1:
            text = text.upper()
        elif capitalisation == 2:
            text = text.title()
        elif capitalisation == 3:
            if len(text) > 1:
                text = text.title()
                text = text[0].lower() + text[1:]
            else:
                text = text[0].lower()
        elif capitalisation == 4:
            text = text.capitalize()
        elif capitalisation == 5:
            text = text.lower()
    words = map(remove_dragon_junk, text.split(" "))
    if spacing == 0:
        text = " ".join(words)
    elif spacing == 1:
        text = "".join(words)
    elif spacing == 2:
        text = "-".join(words)
    elif spacing == 3:
        text = "_".join(words)
    elif spacing == 4:
        text = ".".join(words)
    elif spacing == 5:
        text = "/".join(words)
    elif spacing == 6:
        text = "\\".join(words)
    elif spacing == 7:
        text = ", ".join(words)
    Str(text)(None)

def insert_text(capitalisation=0, spacing=0):
    def f(m):
        try:
            t = m["dgndictation"]
        except KeyError:
            t = ""
        format_text(t, capitalisation, spacing)
    return f