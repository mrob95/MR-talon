from dataclasses import dataclass
from typing import Set, Dict, List


STATE_INITIAL = 0
STATE_UPPERCASE_START = 1
STATE_NUMBERS = 2
STATE_ACRONYM = 3
STATE_WORD = 4

@dataclass
class State:
    state: int
    word_start: int
    word_end: int

transitions = {
    STATE_INITIAL: (
        (lambda s: s.islower(), lambda i, input, state: (State(STATE_WORD,            i,   i+1), None)),
        (lambda s: s.isupper(), lambda i, input, state: (State(STATE_UPPERCASE_START, i,   i+1), None)),
        (lambda s: s.isdigit(), lambda i, input, state: (State(STATE_NUMBERS,         i,   i+1), None)),
        (lambda s: True,        lambda i, input, state: (State(STATE_INITIAL,         i+1, i+2), input[state.word_start:state.word_end])),
    ),
    STATE_UPPERCASE_START: (
        (lambda s: s.islower(), lambda i, input, state: (State(STATE_WORD,            state.word_start, i+1), None)),
        (lambda s: s.isupper(), lambda i, input, state: (State(STATE_ACRONYM,         state.word_start, i+1), None)),
        (lambda s: s.isdigit(), lambda i, input, state: (State(STATE_NUMBERS,         state.word_start, i+1), None)),
        (lambda s: True,        lambda i, input, state: (State(STATE_INITIAL,         i+1,              i+2), input[state.word_start:state.word_end])),
    ),
    STATE_WORD: (
        (lambda s: s.islower(), lambda i, input, state: (State(STATE_WORD,            state.word_start, i+1), None)),
        (lambda s: s.isupper(), lambda i, input, state: (State(STATE_UPPERCASE_START, i,                i+1), input[state.word_start:state.word_end])),
        (lambda s: s.isdigit(), lambda i, input, state: (State(STATE_NUMBERS,         i,                i+1), input[state.word_start:state.word_end])),
        (lambda s: True,        lambda i, input, state: (State(STATE_INITIAL,         i+1,              i+2), input[state.word_start:state.word_end])),
    ),
    STATE_NUMBERS: (
        (lambda s: s.islower(), lambda i, input, state: (State(STATE_WORD,            i,                i+1), input[state.word_start:state.word_end])),
        (lambda s: s.isupper(), lambda i, input, state: (State(STATE_UPPERCASE_START, i,                i+1), input[state.word_start:state.word_end])),
        (lambda s: s.isdigit(), lambda i, input, state: (State(STATE_NUMBERS,         state.word_start, i+1), None)),
        (lambda s: True,        lambda i, input, state: (State(STATE_INITIAL,         i+1,              i+2), input[state.word_start:state.word_end])),
    ),
    STATE_ACRONYM: (
        (lambda s: s.islower(), lambda i, input, state: (State(STATE_WORD,            i-1,              i),   input[state.word_start:state.word_end-1])),
        (lambda s: s.isupper(), lambda i, input, state: (State(STATE_ACRONYM,         state.word_start, i+1), None)),
        (lambda s: s.isdigit(), lambda i, input, state: (State(STATE_NUMBERS,         i,                i+1), input[state.word_start:state.word_end])),
        (lambda s: True,        lambda i, input, state: (State(STATE_INITIAL,         i+1,              i+2), input[state.word_start:state.word_end])),
    ),
}

def create_spoken_forms(input, max_len=3, acronyms=True)-> Set[str]:
    if len(input) == 0:
        return set()
    words = []
    state = State(STATE_INITIAL, 0, 0)
    for i, s in enumerate(input):
        for condition, transition in transitions[state.state]:
            if not condition(s):
                continue
            state, word = transition(i, input, state)
            if word:
                words.append(word)
            break
    words.append(input[state.word_start:state.word_end])

    acronym_words = []
    for word in words:
        if len(word) < 4 and acronyms:
            # Maybe acronym
            acronym_words.extend(list(word.upper()))
        else:
            acronym_words.append(word)

    result = set(" ".join(word_list) for word_list in [words, acronym_words])
    return result

def test_create_spoken_forms():
    for symbol, result in [
        ("test", {"test"}),
        ("test_simple", {"test simple"}),
        ("test_simple_very_long", {'test simple very long'}),
        ("test_simple_55", {"test simple 55", "test simple 5 5"}),
        ("TEST_SIMPLE", {'TEST SIMPLE'}),
        ("README", {'README'}),
        ("test_5_ABC", {'test 5 ABC', 'test 5 A B C'}),
        ("test_5_ABC", {'test 5 ABC', 'test 5 A B C'}),
        ("Action", {'Action'}),
        ("test_filename.py", {'test filename py', 'test filename P Y'}),
        ("fs_watcher", {'fs watcher', 'F S watcher'}),
        ("TestCase", {'Test Case'}),
        ("testCase", {'test Case'}),
        ("s3_ls", {'S 3 L S', 's 3 ls'}),
        ("DBClient", {'DB Client', 'D B Client'}),
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
