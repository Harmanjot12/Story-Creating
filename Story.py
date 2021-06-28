while True:
    umbrella = input("It is a dark and stormy night.  Do you want to take an umbrella?(Y/N): ")
    if umbrella!='Y' and umbrella!='N':    #choosed neither yes nor no
        print("Please choose Y/N")
    else:
        break
    
if umbrella=='Y':   #if having umbreella    
    while True:
        run = input("Its good decision to carry umbrella.  You start to walk down a path and hear a scream.  You realize that the person screaming is you because you see a wolf!  Do you fight with your wolf or run? (F)ight/(R)un ")
   
        if run!='F' and run!='R':
            print("Please choose (F)ight/(R)un : ")
        else:
            break

    if run =='F': #if fight with volf
        print("You take out your umbrella and jab it into the wolf's paw!  It runs away and you live another day.")
        
    elif run =='R': #if run from volf 
        print("You begin running so fast, the umbrella opens and you fly away like Mary Poppins.  You're a little embarrassed, but you see the wolf fading off in the distance.")

         


elif umbrella=='N':   #if not having umbreella    
    while True:
        run = input("You decide not to take an umbrella.You start to walk down a path and hear a scream.  You realize that the person screaming is YOU because you see a wolf!  Do you fight with your volf or run? ((F)ight/(R)un): ")
   
        if run!='F' and run!='R':
            print("Please choose (F)ight/(R)un : ")
        else:
            break

    if run =='F': #if fight with volf 
        print("You begin fighting the wolf only to realize you had just eaten a McGrease® meal earlier.  You fall dead from rigorous exercise, having had a heart attack.")
        
    elif run =='R': #if run from volf 
        print("Are you serious? You can't outrun a wolf!  The wolf catches you and you are somewhat relieved because you don't have to worry about that Calculus exam.")
        
        