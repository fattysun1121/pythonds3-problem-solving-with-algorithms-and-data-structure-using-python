def my_anagram_solution(s1, s2):
    if len(s1) != len(s2):
        return False

    a_list = list(s2)
    for char in s1:
        if char in a_list:
            a_list[a_list.index(char)] = None
    if [i for i in a_list if i is not None] == []:
        return True
    return False


print(my_anagram_solution('apple', 'pleap'))
print(my_anagram_solution('abcd', 'dcda'))


def anagram_solution_1(s1, s2):
    still_ok = True
    if len(s1) != len(s2):
        still_ok = False

    a_list = list(s2)
    pos_1 = 0

    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = False
        while pos_2 < len(a_list) and not found:
            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 += 1
        if found:
            a_list[pos_2] = None
        else:
            still_ok = False

        pos_1 += 1

    return still_ok


def anagram_solution_2(s1, s2):
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    a_list_1.sort()
    a_list_2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list_1[pos] == a_list_2[pos]:
            pos += 1
        else:
            matches = False

    return matches


def anagram_solution_4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False

    return still_ok
