def convert_index_to_alphabet(index):
    return chr(64 + index)


def evacuate_senators(senators_list):
    max_dict = {

    }
        max = senators_list[0]
    second_max = max - 1
    for senators in senators_list:
        senators_length = len(senators)
        if max < senators_length:
            max = senators_length
        elif second_max < senators_length:


# T = int(input())
# for _ in range(T):
#     N = input()
#     senators_list = list(map(int, input().split()))
#     print(N)
#     print(senators_list)

if __name__ == '__main__':
    entry = [2, 3, 4]
    evacuate_senators(entry)
