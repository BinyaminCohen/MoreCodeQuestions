def sum_list(items):
    """returns the sum of items in a list. Assumes the list contains numeric values.
    An empty list returns 0"""

    sum = 0
    if not items:  # this is one way to check if list is empty we have more like if items is None or if items is []
        return 0
    else:
        for x in items:
            sum += x
        return sum


def remove_duplicates(items):
    """remove all the duplicates from a list, and return the list in the original order
	   a copy of the list (with the modifications) is returned 
	   :type items: object

    listNoDup = []

    if len(items) < 2:
        return items

    else:
        for x in items:
            for y in listNoDup:
                if x is not y:
                    listNoDup.append(x)
    return listNoDup"""

    exsist = set()
    listNoDup = []

    for x in items:
        if x not in exsist:
            exsist.add(x)
            listNoDup.append(x)
    return listNoDup


def remove_longer_than(words, n):
    """remove all the words from the words list whose length is greater than N"""
    return [x for x in words if len(x) <= n]


def have_one_in_common(list1, list2):
    """return True if the lists have at least one element in common
    for x in list1:
        for y in list2:
            if x is y:
                return True
    return False"""
    return len(set(list1).intersection(set(list2))) > 0


def word_count(words):
    """takes a list of words and returns a dictionary that maps to each word how many times it appears in the list"""
    d = {}
    for x in words:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d


# start tests

def test_sum_list():
    assert (sum_list([]) == 0)
    assert (sum_list([1]) == 1)
    assert (sum_list([1, 2, 3]) == 6)


def test_remove_duplicates():
    assert (remove_duplicates([1, 3, 2, 1, 3, 1, 2]) == [1, 3, 2])
    assert (remove_duplicates(["a", "b", "a"]) == ["a", "b"])
    assert (remove_duplicates([]) == [])


def test_remove_longer_than():
    l = ["", "a", "aa", "aaa", "aaaa"]
    assert (remove_longer_than(l, -1) == [])
    assert (remove_longer_than(l, 0) == [""])
    assert (remove_longer_than(l, 2) == ["", "a", "aa"])


def test_have_one_in_common():
    assert (have_one_in_common([1, 2, 3], [4, 5, 6]) == False)
    assert (have_one_in_common([], []) == False)
    assert (have_one_in_common([1, 2, 3], [1]) == True)
    assert (have_one_in_common(["a", "b", "c"], ["a", "x", "c"]) == True)


def test_word_count():
    assert (word_count([]) == {})
    assert (word_count(["a", "b", "a"]) == {"a": 2, "b": 1})


if __name__ == "__main__":
    test_sum_list()
    test_remove_duplicates()
    test_remove_longer_than()
    test_have_one_in_common()
    test_word_count()
    print("Done")
