#1)

#import this
zen = '''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

find_count_of_word_better = zen.count('better')
find_count_of_word_never = zen.count('never')
find_count_of_word_is = zen.count('is')
print(f"Better = {find_count_of_word_better}, Never = {find_count_of_word_never}, Is = {find_count_of_word_is}")
uppercase_text = zen.upper()
print(f"uppercase_text = {uppercase_text}")
replace_text = zen.replace('i', '&')
print(f"replace_text = {replace_text}")



