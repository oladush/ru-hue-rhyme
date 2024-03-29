#              +------------------------------------------------------------------------------------+
#  /\__/\      | usage: python3 hue-rhyme.py черти идут работать чертить черный пол черным маркером |
# ( ⊙ ‿ ⊙) ｡ ◯ +------------------------------------------------------------------------------------+
#  (｡  ｡)

import sys, random

VOWEL_TO_RHYME = {
    'а': 'хуя',
    'е': 'хуе',
    'ё': 'хуё',
    'и': 'хуи',
    'о': 'хуё',
    'у': 'хую',
    'э': 'хуе',
    'ю': 'хую',
    'я': 'хуя'
}


def get_first_vowel(word: str) -> str:
    for let in word:
        if let in VOWEL_TO_RHYME:
            return let


def get_first_syllable(word: str) -> str:
    res = ""
    read_vowel = False

    for let in word:
        is_vowel = let in VOWEL_TO_RHYME
        if (read_vowel and not is_vowel):
            break
        if is_vowel:
            read_vowel = True
        res += let

    return res


def get_rhyme(word: str) -> str:
    first_syllable = get_first_syllable(word)
    try:
        rhyme = VOWEL_TO_RHYME[get_first_vowel(first_syllable)]
    except KeyError:
        return word

    return word.replace(first_syllable, rhyme, 1)


def wrap_lines(lines: list[str], max_width=49) -> list[str]:
    new_lines = []
    for line in lines:
        for line_part in [
            line[i:i+max_width] for i in range(0, len(line), max_width)
        ]:
            new_lines.append(line_part)
    return new_lines


def generate_bubble(text):
    lines = [line.strip() for line in str(text).split("\n")]
    lines = wrap_lines([line for line in lines if line])
    text_width = max([len(line) for line in lines])
    output = []
    output.append("+" + "-" * text_width + "--+")
    for line in lines:
        output.append("| " + line + " " * (text_width - len(line) + 1) + "|")

    output.append("+" + "-" * text_width + "--+")
    return output


def hue_say(text: str):
    bubble = generate_bubble(text)

    hue = [
        "             ",
        " /\__/\      ",
        "( ⊙ ‿ ⊙) ｡ ◯ ",
        " (｡  ｡)"
    ]

    res = []
    len_bubble = len(bubble)
    for i in range(len_bubble):
        if (len_bubble - i) > 2:
            res.append(hue[0] + bubble[i])
        else:
            res.append(hue[len(hue) - len_bubble + i - 1] + bubble[i])

    res.append(hue[-1])

    return res


if __name__ == "__main__":
    words = sys.argv[1:]

    if words:
        hue_words = [get_rhyme(word) for word in words]
    else:
        hue_words = [
            random.choice([
                "еблан?", 
                "ебаная жызнь",
                "купил мужик шляпу, "
                "а она ему как раз",
                ])]

    for line in hue_say(' '.join(hue_words)):
        print(line)
