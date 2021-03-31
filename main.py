from functions import command

print("What do you want to do? Type help")

while True:
  what = input().lower()

  #commands aliases
  cmd_lorem = ['lorem', 'loremipsum', 'lor']
  cmd_sarcasm = ['sarcasm', 'sar', 's']
  cmd_length = ['length', 'len', 'l']
  cmd_stov = ['stov', 'stringtovector']
  cmd_cd = ['commondivisors', 'commondivisor', 'comdiv', 'cd']
  cmd_pol = ['polish', 'pol', 'po', 'p']

  helpp = True
  if command(what, 'sarcasm', cmd_sarcasm):
    helpp = False
  elif command(what, 'length', cmd_length):
    helpp = False
  elif command(what, 'stov', cmd_stov):
    helpp = False
  elif command(what, 'lorem', cmd_lorem):
    helpp = False
  elif command(what, 'comdiv', cmd_cd):
    helpp = False
  elif command(what, 'polish', cmd_pol):
    helpp = False
  
  #show help funkction?
  if helpp or what == "help":
    print("Curly brackets are optional")
    print("[s]arcasm {string}")
    print("[l]ength {string}")
    print("[s]tring [to] [v]ector {string}")
    print("[c]mmon [d]ivisors")
    print("[p]polish")