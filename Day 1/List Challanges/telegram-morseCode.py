codes = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___']

text = 'edcba'
code = ''

for items in text:
    indxNm = ord(items) - ord('a')
    code += codes[indxNm] + " "
print(code)
