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
