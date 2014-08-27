#menu code
run = True

while run == True:
    x = raw_input('Choose between Menu 1 or Menu 2 or 0 to return to main menu')

    if x == '1':
      print 'Hallo' #[1,1,2,3,5,8,13,21,34,55,89,144]
      #a = 1
      #b = 1
      #if summe <= 100:
      #  n = a + b
      #  a = b
      #  b = n
      #  return summe(n-1) + summe(n-2)

      a, b = 1
      while neu < 100:
        neu = a + b
        a = b
        b = neu
      else:
        print 'trolo'


    if x == '2':
      print 'Hallo2'

    elif x > 2:
        print 'invalid'
