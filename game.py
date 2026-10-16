import time as t
game_running = True
air_mastered=False
earth_mastered=False
tokens=0
password=24
print("Mysterious voice: Welcome, traveller....")
t.sleep(1)
print("Mysterious voice: You are here to master EARTH and AIR. Remember, if any element is not mastered you will be unable to do both of them. EARTH and AIR go hand-in-hand")
while game_running:
    t.sleep(2)
    print("")
    print("----------------------START ROOM----------------------")
    print("Mysterious voice: I see you are now at the start...")
    t.sleep(1)
    print("You look up and see a list inscribed on the wall.. (1):Earth (2):Air (3):Escape")
    action =int(input("Mysterious voice: Please enter the digit of your action(1-3): "))
    if action ==1:
        if earth_mastered==True:
            print("King Bhumi: Hey! why are you back here. You already mastered the Earth Element")
        else:
            print("")
            print("----------------------EARTH ROOM----------------------")
            print("King Bhumi:Welcome to the Earth Room")
            t.sleep(1)
            print("King Bhumi:To master the Earth element you must correctly answer the riddle as shown..")
            t.sleep(1)
            print("A question started to shift onto the wall. You see in front of you..")
            t.sleep(1)
            print("I'm always moving but I never walk. I carry life across the Earth. What am I?")
            print("a: The Wind")
            print("b: a River")
            print("c: a Duck")
            print("d: Sand")
            answer=input("Your answer(a-d): ").lower()
            if answer == "b":
                print("King Bhumi: Correct! You have mastered the Earth Element.")
                tokens+=1
                earth_mastered=True
            elif answer=="a" or answer=="c" or answer=="d":
                print("King Bhumi: Incorrect")
                print("The floor tilts and you slide all the way back to the start")
            else:
                print("King Bhumi: You have not entered a choice")
                print("The floor tilts and you slide all the way back to the start")
    if action ==2:
        if air_mastered==True:
            print("Aang: Hey! why are you back here. You already mastered the Air Element")
        else:
            print("")
            print("----------------------AIR ROOM----------------------")
            print("Aang: Hello! Welcome to the Air room")
            t.sleep(1)
            print("Aang: To master the Air element you must...")
            t.sleep(1)
            print("Aang: guess my iphone password. I forgot it")
            t.sleep(1)
            print("Aang: It is a number between 1 to 100 and I have a helper that will constantly tell you whether your answer is higher or lower")
            t.sleep(1)
            print("A platform slowly rises up and has buttons for you to enter a number")
            while True:
                number=int(input("Enter a number(1-100): "))
                if number==password:
                    print("Aang:Correct! You have mastered the Air Element")
                    tokens+=1
                    air_mastered=True
                    break
                elif number>password and 0<number<101:
                    print("Machine: Your answer is higher than the password")
                elif number<password and 0<number<101:
                    print("Machine: Your answer is lower than the password")
                else:
                    print("Machine: You have not entered a number within the boundary!")
    if action== 3:
        print("")
        print("----------------------TEST ROOM----------------------")
        print("Mysterious voice: I see you now think you have mastered the element of AIR and EARTH..")
        t.sleep(1)
        print("Mysterious voice: PROVE IT I will now test you before you can escape")
        t.sleep(1)
        if tokens>=2:
            print("You close your eyes and take a deep breath..")
            t.sleep(1)
            print("You stomp your foot. The ground shakes and a wall of rock rises in front of you")
            t.sleep(1)
            print("You swining your arrms. A huge gust of wind smashes the rock wall into pieces")
            t.sleep(2)
            print("behind the rubbles, a door starts to glow")
            t.sleep(2)
            print("Mysterious voice: Impressive.. You have truly mastered EARTH and AIR. You may Leave")
            t.sleep(2)
            print("You begin to walk through the glowing door...")
            t.sleep(2)
            print("----------------------YOU ESCAPED----------------------")
            break
        else:
            print("You close your eyes and take a deep breath..")
            t.sleep(1)
            print("You stomp your foot as hard as you can to summon the Earth...")
            t.sleep(1)
            print("Nothing happens. You stubbed your toe..")
            t.sleep(1)
            print("You swing your arms and only a tiny breeze comes out")
            t.sleep(2)
            print("Mysterious voice: Is that it??")
            t.sleep(2)
            print("Mysterious: Come back when you have actually mastered all elements")
            t.sleep(2)
            print("The floor tilts and you slide all the way back to the start")
            t.sleep(2)


        




            

        



