def printWelcome(name,times):
  for i in range (0,times):
    print('Hello '+name+' ',end='')
name=input('Please type your name: ')
times=int(input('How many times: '))
printWelcome(name.capitalize(),times+1)
