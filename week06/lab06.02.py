# Write a function that prints out a menu of commands we can perform, ie add, 
# view and quit. The function should return what the user chose

def menu():
    inp = input('\nWhat would you like to do? \n(a) Add new student \
                \n(v) View students \n(q) Quit \n\nType one letter (a/v/q): ')
    return inp

def doAdd():
    print("doAdd function")
    name = 

def doView():
    print('doView function')


ans = menu()

while ans != 'q':
    if ans == 'a':
        ans_a = doAdd()
        print(ans_a)
    elif ans == 'v':
        ans_v = doView()
        print(ans_v)
    print(f'\n\n{menu()}')


#print(f"\nYou chose {ans}")
