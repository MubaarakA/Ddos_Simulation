import threading
import time

password= # specify the file path

found_password_event=threading.Event()

print("username is admin")
time.sleep(2)
systempass="liolang"
Found=True
def ddos_attack_simulation(validatedpasswd):

    for i in validatedpasswd:


        if found_password_event.is_set():
            return
        print("attempting password of" ,i)

        if systempass == i:
            found_password_event.set()
            print("you hacked this machine congratulation")
            displayinfo=input("you want to see the password  :)")
            if displayinfo in ["Yes","Y","yes",'y'] :
                print("the password is ",i)
            else:
                return
        time.sleep(0.1)


mylist=[]
try:
    with open(password, 'r') as passw:
        content = passw.read()
except FileNotFoundError as E:
    print(E)


if content:
    mylist = content.split()
    midpoint = (len(mylist) // 2)
    first_half_of_password = (mylist[:midpoint])
    second_half_of_password = (mylist[midpoint:])
    print(first_half_of_password)
    print(second_half_of_password)
    thread_1 = threading.Thread(target=ddos_attack_simulation, args=[first_half_of_password])
    thread_2 = threading.Thread(target=ddos_attack_simulation, args=[second_half_of_password])

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()








