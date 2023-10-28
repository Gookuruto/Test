def file_to_int_list(path):
    list_of_ints = []
    with open(path, "r") as f:
        line = f.readline()
        while line:
            list_of_ints.append(int(line))
            line = f.readline()
    return list_of_ints


one_list = file_to_int_list("one.txt")
two_list = file_to_int_list("two.txt")

overlap_list = [number for number in one_list if number in two_list] # moga poawic sie duplikaty niektorych liczb

zbior1 = set(one_list)
zbior2 = set(two_list)

overlap = list(zbior1.intersection(zbior2))# tu nie bedzie duplikatów nigdy
overlap.sort()

overlap_list.sort()
print(overlap)
print(overlap_list)
