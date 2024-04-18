''' Write a  Python program to display formatted text (width=50) as output.'''
import textwrap

def display_formatted_text(text):
    formatted_text = textwrap.fill(text, width=50)
    print(formatted_text)
example_text = "aaaa ssss dddd ffff ggg hhh jjjj kkkk lll mmm nnn bbb vv ccc xxxx zzzz qqq www rrr tttt yyy uuu iii ooo pp "
display_formatted_text(example_text)
