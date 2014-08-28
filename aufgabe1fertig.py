#menu code
run = True

while run == True:
  x = raw_input('Choose menu 1 or menu 2 or return with 0')
#menu1
  if x == '1':
    print 'You choose the fibonacci menu'
    a = 1
    b = 1
    neu = 0

    while neu < 100:
      neu = a + b
      a = b
      b = neu
      print a
#menu2
  elif x == '2':
    word = raw_input('Enter word - ') #enter the word that is going to be reversed

    y = list(word)                 #using list instead of iteration
    y.reverse()                    #reverse the letters using reverse() function

    print y                        #display result

    print "Count for a : ", y.count("a")
    print "Count for i : ", y.count("i")
    print "Count for e : ", y.count("e")
    print "Count for o : ", y.count("o")
    print "Count for u : ", y.count("u")

  elif x == '0':
    run = False

  else:
    print 'invalid'
