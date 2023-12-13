def solve(s):
    s_split = s.split(" ")
    result_list = [string.capitalize() for string in s_split]
    return " ".join(result_list)

print(solve(("hello   world  lol")))
