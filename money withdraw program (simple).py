# money withdraw program
cb=10000   #  i am taking an assumption that user has 10000 in his account

while True:
    wb=int(input("enter amount:"))

    try:
      if(cb<wb):
        raise ValueError()
      else:
        cb=cb-wb
        print("money sent")
        print("current balance is :",cb)
    except ValueError:
          print("insufficient Balance.")
          print("current balance is :",cb)

'''
 output

 enter amount:12
money sent
current balance is : 9988
enter amount:4324
money sent
current balance is : 5664
enter amount:123
money sent
current balance is : 5541
enter amount:231
money sent
current balance is : 5310
enter amount:1231
money sent
current balance is : 4079
enter amount:1323
money sent
current balance is : 2756
enter amount:3131
insufficient Balance.
current balance is : 2756



  another scenario when user try to withdraw more than current balance

                enter amount:3313131
                insufficient Balance.
                current balance is : 10000
                enter amount:

'''
