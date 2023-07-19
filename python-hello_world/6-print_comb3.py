for i in range(0,9):
     for k in range(0,10):
         if i == 8 and k == 9:
             print("{}{}".format(i,k))
         else:
             print("{}{},".format(i,k), end=" ")
