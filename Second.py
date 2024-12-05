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
