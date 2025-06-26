# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())  # n is an odd natural number, and m is 3 times n

a = "-"
b = ".|."
for i in range(n//2):
    print(f"{(m-3*(2*i+1))//2*a}{b*(2*i+1)}{(m-3*(2*i+1))//2*a}")
    
print(f"{(m-7)//2*a}WELCOME{(m-7)//2*a}")

for i in range(n//2):
    print(f"{(m-3*(2*(n//2-i-1)+1))//2*a}{b*(2*(n//2-i-1)+1)}{(m-3*(2*(n//2-i-1)+1))//2*a}")