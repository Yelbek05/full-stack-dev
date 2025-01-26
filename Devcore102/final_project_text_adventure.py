
# scenario written by Yelbek
"""
You are a detective in a small town. You have been called to
investigate a criminial case(specifically a murder). You can done the investigation successfully
If you follow the 1 way other than 2, but overall 3 ways to solve it:
1. Investigate the crime scene by asking questions to the witness and collecting evidence
    - talk to the witnesses, but they cannot be free all the time to talk to you,
    so it depends on the minute if the minute is "even" you can talk to them, If the minute is "odd" you failed, investigate it watching crime scene
      -- if the minute is even it doesn't mean the witnesses know all the things which means they may not see imporatant things,
      If you ASKED THE WRONG PERSON and FOLLOW HIS/HER thoughts, you are gonna fail, but If you ask the right person you are gonna win
--Overall if you fail it does not mean you just failed, you can do it by following the 2nd way

2. Investigate the crime scene by watching for cameras
    -watch the cameras, if the cameras were not blank by accident you are gonna see what happened and find out the Guilty Criminal and search 
    him / her through interntet, if her / him information exists you will win
    --If the cameras are blank by accident you are gonna fail, and go to the 3rd way

-follow the third way
3. Or Investigate the case by following and hanging out with suspects
    --You have to make the suspect get drunk, If you make him / her drunk you go to the next step, if you cannot make the suspect drunk you FAIL
"""
from datetime import datetime
class Forinit:
    def __init__(self):
        self.used_choices = set()

class Investigation:
    def investigate_witness(self, time_now):
        #Name, what happened?
        record_of_witnesses = [
            ("Marlan", "I am a neighbour nearby, I was sleeping, but heard some screams outside, but I thought that was just coincidence, and I kept sleep"),
            ("Karla", "I was walking by street coming from my long hours of work, \nI was dead tired but heard a bit of a strange noise going on in the house,\nI thought there might be accidental, but I heard it twice, and frequently called the police to come and check, and I saw he man coming out of the house,\n he was tall fat white man,\n I was scared turned back to home and locked my doors")
        ]

        if time_now.minute % 2 == 0:
            ask = input("Who is her / him name and what happeneded? ")
            marlan_name, marlan_statement = record_of_witnesses[0]
            print(f"Name: {marlan_name}\nWhat happened?\n{marlan_statement}\n")

            enough = input("Was this enough for evidence?(no/yes) ")
            if enough.lower() == "no":
                karla_name, karla_statement = record_of_witnesses[1]
                print(f"Name: {karla_name}\nWhat happened?\n{karla_statement}\n")
                print("Great you almost won the half of the battle, \nbut you should have more evidence,\nLook in other ways given")
            elif enough.lower() == "yes":
                print("This was not even an evidence, you FAILED this way, go and check the next ways")
        else:
            print("No witnesses, go to the next way")

                
    
    def watch_cameras(self, time_now):
        if time_now.minute % 2 == 0:
            print(f"Camera was not blank, it was working great and you see 2 suspects from the record of camera, but they are still a bit unkown,\nbecause they worn masks on their face, \nbut you have got their heights and body shapes, even noticable clothes")
        elif time_now.minute % 2 != 0:
            print(f"Ohh the camera is BLANK, the 2nd strategy is failed please go to the next round!")

    def befriend(self, time_now):
        
        welcome_ask_question = input("Say Hi to the suspect: ")
        he_answers = print("Hey do I know you?!")

        ask_his_name = input("Ask his name, and what he does: ")
        print("My name is Karen, I am a plumber, how about you?!")  
        you_answer = input("Explain what you do, you are a investigator, aren't you?!: ").lower()

        if "investigator" in you_answer:
            print("You failed. It was a suspect, and you shouldn't have revealed that you are an investigator.")
            return  # Exit the method if failed
        
        
        ask_for_bar = input("Ask him if he likes to have a drink on the bar ")

        if time_now.minute % 2 == 0:
            print("Yes, why not to go now? (In the end you made him go drunk, but he still didn't drink a lot)")
        
        elif time_now.minute % 2 != 0:
            print("You failed he doesn't wanted to go drunk, you FAILED the investigation")
        


def main():  
    print("You are Detective Morgan, \na seasoned investigator in the small but mysterious Cedarwood Town. \nA murder has occurred, and the town is shaken. Your mission is to solve the case and bring the perpetrator to justice. \nThere are three distinct ways to solve the case, and each comes with its own risks and challenges. Follow your instincts and the clues to unravel the mystery.")
    
    Investigating = Investigation()
    Init = Forinit()
    while True:
        print("Choose one: ")
        print("1. Interrogating Witnesses and Collecting Evidence")
        print("2. Watching Surveillance Cameras")
        print("3. Following and Befriending Suspects")
        
        choice = input("Enter your choice: ")
        
        if choice in Init.used_choices:
            print(f"This option is already been used, please choose OTHER THAN {choice}")
            continue
            
        time_now = datetime.now()
        
        if choice == '1':
            Investigating.investigate_witness(time_now)

        elif choice == '2':
            Investigating.watch_cameras(time_now)
        
        elif choice == '3':
            Investigating.befriend(time_now)

        Init.used_choices.add(choice)

if __name__ == '__main__':
    main()