# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random;
egg=['red','green','blue','yellow','black']
choice=random.choie(egg);
user=input("Enter choice:");
int level=0;
score=0;
attempt=5;
time=10;
motion=0;
challange=10;
bool click=False;
bool allsuccess=False/
def first_step(level,choice):
    if choice in egg:
        print("choice valid")
    else:
        print("choice invalid!")
        while attempt>0&&!click :
            if choice in egg:
                print("First step done.")
                score+=1;
                attempt--;
                time/2;
                motion+=50;
                challange+=10;
                level+=1;
                if attempt ==0 and time==0:
                    print("First step finish")
                    if score==100:
                        print("Win.Go next step")
                        else:
                            print("Fail.Finish")
 def second_step(level,choice):
    if choice in egg:
        print("choice valid")
    else:
        print("choice invalid!")
        while attempt>0&&!click :
            if choice in egg:
                print("Second step done.")
                score+=2;
                attempt-=2;
                time/4;
                motion+=100;
                challange+=20;
                level+=2;
                if attempt ==0 and time==0:
                    print("First step finish")
                    if  score==200:
                        print("Win.go next step.")
                        else:
                            print("Fail.Finish")
def third_step(level,choice):
    if choice in egg:
        print("choice valid")
    else:
        print("choice invalid!")
        while attempt>0&&!click :
            if choice in egg:
                print("First step done.")
                score+=3;
                attempt--;
                time/8;
                motion+=150;
                challange+=30;
                level+=3;
                if attempt ==0 and time==0:
                    print("Third step finish")
  if score==250:
                        print("Win.go next step.")
                        else:
                            print("Fail.Finish")
 def fourth_step(level,choice):
    if choice in egg:
        print("choice valid")
    else:
        print("choice invalid!")
        while attempt>0&&!click :
            if choice in egg:
                print("Fourth step done.")
                score+=4;
                attempt--;
                time/16;
                motion+=200;
                challange+=40;
                level+=4;
                if attempt ==0 and time==0:
                    print("First step finish")
                    if score==5:
                        print("Success")
                          score==300:
                        print("Win.go next step.")
                        else:
                            print("Fail.Finish")
 def fifth_step(level,choice):
    if choice in egg:
        print("choice valid")
    else:
        print("choice invalid!")
        while attempt>0&&!click :
            if choice in egg:
                print("Fifth step done.")
                score+=5;
                attempt--;
                time/32;
                motion+=250;
                challange+=50;
                level+=5;
                if attempt ==0 and time==0:
                    print("First step finish")
                    if score==5:
                        print("Success")
  score==350:
                        print("Win.go next step.")
                        else:
                            print("Fail.Finish")
            def final():
         if !allsuccess:
             print(f"You Won the game.Your score is:{score}")
