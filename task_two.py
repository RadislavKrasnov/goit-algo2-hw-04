from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or len(strings) == 0:
            return ''
        for s in strings:
            if not isinstance(s, str):
                return ''
        shortest = min(strings, key=len)
        for i, char in enumerate(shortest):
            for other in strings:
                if other[i] != char:
                    return shortest[:i]
        return shortest
    

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    print(f"Test 1: {strings} => '{trie.find_longest_common_word(strings)}'")

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"
    print(f"Test 2: {strings} => '{trie.find_longest_common_word(strings)}'")

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    print(f"Test 3: {strings} => '{trie.find_longest_common_word(strings)}'")
