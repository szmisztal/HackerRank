size = int(input())
set_to_working_with = set(map(int, sorted(input().split(), reverse=True)))
number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input().split()
    if len(command)==1:
        set_to_working_with.pop()
    else:
        if command[0]=='remove':
            if int(command[1]) in set_to_working_with:
                set_to_working_with.remove(int(command[1]))
        elif command[0]=='discard':
            set_to_working_with.discard(int(command[1]))

print(sum(set_to_working_with))
