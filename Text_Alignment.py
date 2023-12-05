n = int(input())

#Head
for i,j in zip(range(1, (2* n),2), range(n-1,-1,-1)):
    left_up = ' ' * j + 'H' * i
    print(left_up)
#Arms
for _ in range(n+1):
    left_right_lines = ' ' * (n//2) + 'H' * n + ' ' * (n*3)+ 'H' * n
    print(left_right_lines)
#body
for _ in range((n//2)+1):
    print(' ' * (n//2)+ 'H' * (n + (n*3)) + 'H' * n)
#legs
for _ in range(n+1):
    print(left_right_lines)
#feet
for i,j in zip(range((2* n - 1), 0,-2), range(0,n,1)):
    right_down = ' ' * (j+(n*4)) + 'H' * i
    print(right_down)

