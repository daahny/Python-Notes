import re

text = ('### this is sample text with several words')

var = '<h{}>{}'.format(len(text.split()[0]), text)

print(var)
