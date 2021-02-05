import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa
gtcanaana@gmail.com
MetaCharacters(Should be escaped):
. * $ ? \ | { } + [ ] ( )

google.com
321-555-1323
123.232.2313
123*232*2313
800.232.2313
900.232.2313

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robertson
Mr. T

cat
mat
pat
bat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match.group())
