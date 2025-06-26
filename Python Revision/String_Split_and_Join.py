def split_and_join(line):
    # write your code here
    split = line.split(' ')
    joint = '-'.join(split)
    return joint

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)