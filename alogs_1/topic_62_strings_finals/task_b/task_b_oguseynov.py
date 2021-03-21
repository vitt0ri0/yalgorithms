# from collections import deque


class State:
    def __init__(self, identifier, symbol=None, parent=None, success=False):
        self.symbol = symbol
        self.identifier = identifier
        self.transitions = {}
        self.parent = parent
        self.success = success
        self.matched_keyword = None
        self.longest_strict_suffix = None


class KeywordTree:

    def __init__(self):
        self._zero_state = State(0)
        self._counter = 1
        self._finalized = False

    def add(self, keyword):
        if self._finalized:
            raise ValueError('KeywordTree has been finalized. No more keyword additions allowed')
        original_keyword = keyword
        if len(keyword) <= 0:
            return
        current_state = self._zero_state
        for char in keyword:
            try:
                current_state = current_state.transitions[char]
            except KeyError:
                next_state = State(self._counter, parent=current_state, symbol=char)
                self._counter += 1
                current_state.transitions[char] = next_state
                current_state = next_state
        current_state.success = True
        current_state.matched_keyword = original_keyword

    def search_all(self, text, map):
        if not self._finalized:
            raise ValueError('KeywordTree has not been finalized.')
        zero_state = self._zero_state
        current_state = zero_state
        for idx, symbol in enumerate(text):
            current_state = current_state.transitions.get(symbol, zero_state.transitions.get(symbol, zero_state))
            state = current_state
            while state is not zero_state:
                if state.success:
                    keyword = state.matched_keyword
                    value = map[keyword]
                    value.append(idx + 2 - len(keyword))
                    map[keyword] = value
                state = state.longest_strict_suffix
        return map

    def finalize(self):
        if self._finalized:
            raise ValueError('KeywordTree has already been finalized.')
        self._zero_state.longest_strict_suffix = self._zero_state
        self.search_lss_for_children(self._zero_state)
        self._finalized = True

    def search_lss_for_children(self, zero_state):
        processed = set()
        to_process = [zero_state]
        while to_process:
            state = to_process.pop()
            processed.add(state.identifier)
            for child in state.transitions.values():
                if child.identifier not in processed:
                    self.search_lss(child)
                    to_process.append(child)

    def search_lss(self, state):
        zero_state = self._zero_state
        parent = state.parent
        traversed = parent.longest_strict_suffix
        while True:
            if state.symbol in traversed.transitions and traversed.transitions[state.symbol] is not state:
                state.longest_strict_suffix = traversed.transitions[state.symbol]
                break
            elif traversed is zero_state:
                state.longest_strict_suffix = zero_state
                break
            else:
                traversed = traversed.longest_strict_suffix
        suffix = state.longest_strict_suffix
        if suffix is zero_state:
            return
        if suffix.longest_strict_suffix is None:
            self.search_lss(suffix)
        for symbol, next_state in suffix.transitions.items():
            if symbol not in state.transitions:
                state.transitions[symbol] = next_state

filename = '01'

if __name__ == '__main__':
    with open(filename) as f:
        s = f.readline().strip()
        n = int(f.readline().strip())

        samples = list()

        for _ in range(n):
            samples.append(f.readline().strip())
            # samples[f.readline().strip()] = deque()

    t = KeywordTree()

    for sample in samples:
        t.add(sample)

    t.finalize()

    keywords_found = t.search_all(s, samples)

    for sample in samples:
        print(sample, *sorted(keywords_found.get(sample, [])))