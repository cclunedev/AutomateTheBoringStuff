def regexStrip(inputString, regexChars = None):
  import re
  if regexChars == None:
    stripRegex = re.compile(r'[\S].*[\S]')
    strip = stripRegex.search(inputString)
    print(strip.group())

  else:
    
    regex = "[" + regexChars + "]"
    stripRegex = re.compile(regex)
    strip = stripRegex.sub('',inputString)
    print(strip)


regexStrip('  slhoth   ', regexChars='h')