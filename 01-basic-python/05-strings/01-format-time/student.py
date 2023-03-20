# Write your code here
def format_time(hours, minutes, seconds):
    str_a = str(hours)
    str_b = str(minutes)
    str_c = str(seconds)
    if len(str_a) == 1:
        str_a = f'0{str_a}'
    if len(str_b) == 1:
        str_b = f'0{str_b}'
    if len(str_c) == 1:
        str_c = f'0{str_c}'

    return f'{str_a}:{str_b}:{str_c}'
