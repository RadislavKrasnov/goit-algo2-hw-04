from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError(f"Illegal argument for count_words_with_suffix: pattern = {pattern} must be a string")
        count = 0
        for word in self.keys():
            if word.endswith(pattern):
                count += 1
        return count
    

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for has_prefix: prefix = {prefix} must be a string")
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return self.__has_word_in_subtree(current)
    

    def __has_word_in_subtree(self, node) -> bool:
        if node.value is not None:
            return True
        
        for child in node.children.values():
            if self.__has_word_in_subtree(child):
                return True
        return False


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    suffix_tests = ["e", "ion", "a", "at"]
    for suffix in suffix_tests:
        count = trie.count_words_with_suffix(suffix)
        print(f"Words ending with '{suffix}': {count}")

    prefix_tests = ["app", "bat", "ban", "ca"]
    for prefix in prefix_tests:
        exists = trie.has_prefix(prefix)
        print(f"Prefix '{prefix}' exists: {exists}")
