# Write your code here
import re


def collect_links(string):
    return re.findall('<a href="(.*)">', string)
