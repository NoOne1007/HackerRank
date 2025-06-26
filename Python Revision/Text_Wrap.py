import textwrap

'''
def wrap(string, max_width):
    start = 0
    end = max_width
    while end <= len(string)+max_width:
        print(string[start:end])
        start = end
        end += max_width

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
'''

def wrap(string, max_width):
    L = []
    start = 0
    end = max_width
    while end < len(string) + max_width:
        L.append(string[start:end])
        start = end
        end += max_width
    f_str = "\n".join(L)
    return f_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)