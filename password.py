import random



string = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
STRING = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nemad = ["@","#","!","&","*","_","?"]
number = ['1','2','3','4','5','6','7','8','9','0']
space = [' ']
m = []
ran = []
password = ''
print('1:Letters')
le = input('(y,n) ')

print('2:Capital letters')
ca = input('(y,n) ')

print('3:symbol')
sy = input('(y,n) ')

print('4:number')
nu = input('(y,n) ')

print('5:space')
sp = input('(y,n) ')

if le == 'y':
    for i in (string):
        m.append(i)

if ca == 'y':
    for i in (STRING):
        m.append(i)

if sy == 'y':
    for i in (nemad):
        m.append(i)

if nu == 'y':
    for i in (number):
        m.append(i)

if sp == 'y':
    for i in (space):
        m.append(i)

if len(m) != 0:
    x = int(input('How many digits is your password? '))
    for d in range(x):
        pas = random.choice(m)
        ran.append(pas)


    for j in(ran):
        password = password + j

    print('password:\n{}'.format(password))




else:
    print('Error')

input('')
input('')
