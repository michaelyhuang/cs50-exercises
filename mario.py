while True:
    num_str = input("How high is the pyramid?\n")
    num = int(num_str)
    if num > 0:
        break

print(f'Height: {num}')

for i in range(1,num+1):
    n_spaces = num - i
    n_hashes = i
    print(" " * n_spaces, "#" * n_hashes, " ", "#" * n_hashes, " " * n_spaces)


