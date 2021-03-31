import os

#stov
def stov(s):
  ret = "{"
  first = True
  for c in s:
    if first:
      ret += "'" + c + "'"
      first = False
    else:
      ret += ", '" + c + "'"
  ret += "}"
  return ret

def stov_now():
  s = input("Input String: ")
  ret = "{"
  first = True
  for c in s:
    if first:
      ret += "'" + c + "'"
      first = False
    else:
      ret += ", '" + c + "'"
  ret += "}"
  print(ret)

#length
def length(s):
  return len(s)

def length_now():
  s = input("Input String: ")
  print(len(s))

#sarcasm
def sarcasm(s):
  counter = 0

  for i in range(len(s)):
    skip = ord(s[i]) < 65 or ord(s[i]) > 122
    if skip:
      counter += 1
    if (i + counter) % 2 == 0:
      s = s[0:i] + s[i:].lower()
    else:
      s = s[0:i] + s[i:].upper()
  
  return s

def sarcasm_now():
  s = input("Input String: ")
  counter = 0

  for i in range(len(s)):
    skip = ord(s[i]) < 65 or ord(s[i]) > 122
    if skip:
      counter += 1
    if (i + counter) % 2 == 0:
      s = s[0:i] + s[i:].lower()
    else:
      s = s[0:i] + s[i:].upper()
  
  print(s)

def lorem(i):
  i = int(i)
  ret = ""
  for counter in range(i):
    ret += "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    if i != 1 and counter != i - 1:
      ret += " "
  return ret

def lorem_now():
  print("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")

def comdiv(s):
  numbers = list(map(int, s.split(' ')))
  ret = []
  for i in range(2, min(numbers) + 1, 1):
    add = True
    for j in numbers:
      if j % i != 0:
        add = False
    if add:
      ret.append(i)
  return ret


def comdiv_now():
  s = input("Input numbers: ")
  numbers = list(map(int, s.split(' ')))
  ret = []
  for i in range(2, min(numbers) + 1, 1):
    add = True
    for j in numbers:
      if j % i != 0:
        add = False
        continue
    if add:
      ret.append(i)
  print(ret)


def polish_now():
  litery = "ą ć ę ł ń ó ś ź ż";
  print(litery)
  print(litery.upper())

def shutdown(i):
  os.system("shutdown /s /t " + str(i * 60))

#run them
commands = {
  'lorem' : lorem,
  'lorem_now' : lorem_now,
  'sarcasm' : sarcasm,
  'sarcasm_now' : sarcasm_now,
  'length' : length,
  'length_now' : length_now,
  'stov' : stov,
  'stov_now' : stov_now,
  'comdiv' : comdiv,
  'comdiv_now': comdiv_now,
  'polish_now': polish_now,
  'shutdown' : shutdown;
}

def command(entry, func, aliases):
  if entry.strip() in aliases:
    commands[func + "_now"]()
    return True
  else:
    for i in range(len(aliases)):
      if entry[0:len(aliases[i]) + 1] == aliases[i] + " ":
        print(commands[func](entry[len(aliases[i]) + 1:]))
        return True
  return False

