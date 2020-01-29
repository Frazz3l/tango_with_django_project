print('the magic Beanstalk')
height = 100

hours = int(input('enter a number of hours:'))

print('after one hour, the beanstalk was 100cm tall.')

for i in range(2,hours):
    height = height * 1.5+30
    print("after" , i , "hours, the banstalk was" , height , "cm tall!")

print('and its still growing')
