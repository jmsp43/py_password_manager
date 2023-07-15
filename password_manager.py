master_pwd = input("What is the master password? ")


def view():
    #r means read file without making any changes
    with open('passwords.txt', 'r') as file:
      for line in file.readlines():
            print(line)


def add():
  name = input('Account Name: ')
  pwd = input('Password: ')
  
  #using with will automatically close file for you after using it
  #a means append to file end without changing anything else in it, and if it doesn't already exists it will create a new file
  with open('passwords.txt', 'a') as file:
    file.write(name + '|' + pwd + "\n")


    


while True:
    mode = input("Would you like to add a new password, or view existing ones? Enter 'view' or 'add'. Press q to quit. ")
    if mode.lower() == 'q':
      break
    elif mode.lower() == 'view':
      view()
    elif mode.lower() == 'add':
      add()
    else: 
      print('Invalid mode. Choose add or view.')
      continue