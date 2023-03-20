# Write your code here
import re


def parse_link(string):
    match = re.fullmatch(r'<a href="(.*)">(.*)</a>', string)
    if match:
        caption = str(match.group(1))
        link = str(match.group(2))
        return (link, caption)
    else:
        return None
