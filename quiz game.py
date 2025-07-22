print("")
print("")


print("welcome to the general knowlege quiz!!") 
print("")
print("")


print("INSTRUCTIONS:")
print("         1. There are 5 questions in this quiz.")
print("         2. All questions are MCQ type in which only one option is correct.")
print("         3. Finish the quiz in minimum possible time. Best of luck!")
print("")
print("")

score=0 

start=str(input("ready to start(y/n): "))
if(start=="y"):
    print("")
    print("")
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

    print("question 1:  What is the capital of France?")
    print("(a) london")
    print("(b) paris")
    print("(c) rome")

    answer1=str(input("your answer:" ))

    if(answer1=="b"):
        print("correct")
        score+=1
    else:
        print("wrong")
        print("correct answer is (b)")
        score+=0

    print("")
    print("")

#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    next=str(input("next question(y/n): "))
    if(next=="y"):

        print("")
        print("")
        print("question 2: Which is the biggest planet in our solar system?")
        print("(a) mars")
        print("(b) earth")
        print("(c) jupiter")

        answer2=str(input("Your answer:"))
        if(answer2=="c"):
            print("correct")
            score+=1
        else:
            print("wrong")
            print("correct answer is (c)")

            score+=0



        print("")
        print("")
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    next=str(input("next question(y/n): "))
    if(next=="y"):
        print("")
        print("")
        print("question 3:  When was Environment day celebrated?")
        print("(a) 5 June")
        print("(b) 21 june")
        print("(c) 1 May")

        answer3=str(input("your answer:"))
        if(answer3=="a"):
            print("correct")
            score+=1
        else:
            print("wrong")
            print("correct answer is (a)")
            score+=0

        print("")
        print("")
#44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
    next=str(input("next question(y/n): "))
    if(next=="y"):
        print("")
        print("")
        print("question 4: which team had won the maximum number of icc trophies?")
        print("(a) India")
        print("(b) Australia")
        print("(c) England")

        answer=str(input("your answer:"))
        if(answer=="b"):
            print("correct")
            score+=1
        else:
            print("wrong")
            print("correct answer is (b)")
            score+=0


    print("")
    print("")
#55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    next=str(input("next question(y/n): "))
    if(next=="y"):
        print("")
        print("")
        print("question 5: how much time(approx.) will we take to reach the nearest star(except sun) from Earth if we travel with speed of light?")
        print("(a) 10 days")
        print("(b) 2.5 years")
        print("(c) 4 years")

        answer=str(input("your answer:"))
        if(answer=="c"):
            print("correct")
            score+=1
        else:
            print("wrong")
            print("correct answer is (c)")
            score+=0


    print("")
    print("")

    print("YOUR SCORE:",score)

    if(score==0):
        print("Bad work")

    if(score==1):
        print("get more knowledge")
    if(score==2):
        print("fair")
    if(score==3):
        print("good")
    if(score==4):
        print("better next time")

    if(score==5):
        print("excellent knowledge!!")



    print("")
    print("")
