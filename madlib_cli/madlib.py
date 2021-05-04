def wlcome():
    print(f"""
    Welcome the Madlib Game ....
    In this game I will ask you to enter somethings
    and you will be surprized
    lets go .....
    """)

def inputs():
    first_name = input("Enter your name ...")
    second_name = input("Enter any other name ....")
    adjective = input("Enter an adjective ....")
    past_verb = input("Enter a past verb ....")
    return [first_name,second_name,adjective,past_verb]

def read():
    valList = inputs()
    with open('assets/Game.txt') as fi:
        contents = fi.read()
    yourContent = contents %(valList[0],valList[1],valList[2],valList[3])
    return yourContent

def write():
    yourContent = read()
    with open('assets/user_answer.txt', 'w') as second_fi:
        second_fi.write(yourContent)
    print("  *****************************************************  ")
    print("  also you can find your answer iside user_answer.txt")
    print("  *****************************************************  ")
    print(yourContent)

def read_Game(val):
  striped_string = val.strip()
  return striped_string

def merge(templateString,exList):
  yourContent = templateString %(exList[0],exList[1],exList[2],exList[3])
  return yourContent

def parse(temStr):
  newStr = ""
  newList = []
  i = 0
  while i<len(temStr):
    if temStr[i] == '%':
      newStr = newStr + ''
      i += 1
    else:
      newStr = newStr + temStr[i]  
    i += 1
  for i in range(temStr.count('%s')):
    newList.append('%s')
  return [newStr,newList]

if __name__ == "__main__":
    wlcome()
    write()
