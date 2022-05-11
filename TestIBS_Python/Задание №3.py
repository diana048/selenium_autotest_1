numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def filter_odd_num_bigthan50(num):
    if num % 2 != 0 and num > 50:
        return 1
    else:
        return 0

print(list(filter(filter_odd_num_bigthan50, numbers)))