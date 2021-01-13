def str_reverse(word):
    # word contains n letter
    # assume that we  known hơ to reverse a word with (n-1)
    if len(word) == 1:
        return word
    return str_reverse(word[1:]) + word[0]


#print(str_reverse('abcd'))
#print(str_reverse('a'))


def tower_of_hn(number_of_disks, start_peg, dest_peg, temp_peg):
    if number_of_disks == 1:
        print('Move a disk from', start_peg, 'to', dest_peg)
    else:
        tower_of_hn(number_of_disks - 1, start_peg, temp_peg, dest_peg)
        # move one disk
        print('Move a disk from', start_peg, 'to', dest_peg)
        tower_of_hn(number_of_disks - 1, temp_peg, dest_peg, start_peg)


#tower_of_hn(1, 'A', 'B', 'C')
tower_of_hn(5, 'A', 'B', 'C')
