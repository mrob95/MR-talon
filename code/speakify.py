import re
from talon import clip
from typing import Set, Dict, List

pattern = re.compile(r"[A-Z][a-z]+|[A-Z]+|[a-z]+|\d")
def create_spoken_forms(input: str, max_len: int=3, acronyms: bool = True) -> Set[str]:
    result =  set()
    symbols = [input, input.partition(".")[0]] if "." in input else [input]
    for symbol in symbols:
        words = pattern.findall(symbol)

        acronym_words = []
        for word in words:
            # if len(word) < 4 and word.isupper():
            if len(word) < 4 and acronyms:
                # Maybe acronym
                acronym_words.extend(list(word.upper()))
            else:
                acronym_words.append(word)

        for word_list in [words, acronym_words]:
            result.add(" ".join(word_list))
            # if len(word_list) > max_len:
            #     result.add(" ".join(word_list[:max_len]))

    return result


def test_create_spoken_forms():
    for symbol, result in [
        ("test", {"test"}),
        ("test_simple", {"test simple"}),
        ("test_simple_very_long", {'test simple very long'}),
        ("test_simple_55", {"test simple 5 5"}),
        ("TEST_SIMPLE", {'TEST SIMPLE'}),
        ("README", {'README'}),
        ("test_5_ABC", {'test 5 ABC', 'test 5 A B C'}),
        ("test_5_ABC", {'test 5 ABC', 'test 5 A B C'}),
        ("Action", {'Action'}),
        ("test_filename.py", {'test filename py', 'test filename', 'test filename P Y'}),
        ("fs_watcher", {'fs watcher', 'F S watcher'}),
        ("TestCase", {'Test Case'}),
        ("testCase", {'test Case'}),
        ("s3_ls", {'S 3 L S', 's 3 ls'}),
    ]:
        spoken = create_spoken_forms(symbol)
        assert spoken == result, f"{spoken} != {result}"

test_create_spoken_forms()

raw_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
raw_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

digits = {i: name for i, name in enumerate(raw_digits)}
teens = {i: name for i, name in enumerate(raw_teens, 10)}

def map_numbers_to_spoken(n: int) -> str:
    if n <= 9:
        return digits[n]
    elif 10 <= n <= 19:
        return teens[n]
    else: # TODO
        text = " ".join([digits[int(digit)] for digit in str(n)])
        return text

def create_voice_mapping(items: List[str], *a, **kw) -> Dict[str, str]:
    result = {}
    for item in items:
        for spoken in create_spoken_forms(item, *a, **kw):
            result[spoken] = item
    return result
