#Coded by Jin Sheng Cao
import time
import random

#Important Lists
inventory = ['fishing rod', 'trash grabber', 'safety equipment', 'sampling kit', 'seeds and trowel']
letters = []
# path_available = ['pond', 'landfill', 'construction', 'forest', 'farm']
path_taken = []

def LandFill():

  print("The town’s garbage collector has worked for over a decade. Every day, he drove his truck through the neighborhoods surrounding Chesapeake Bay, picking up the residents' trash and taking it to the landfill. But lately, he had been troubled by the sight of rubbish spilling over the edges of the landfill. It wasn’t just unsightly; it was harmful to the environment and the community.")
  
  print("This town used to be a beautiful place, but now it's getting out of hand! The landfill is overflowing, and I could use your help to turn things around.")
  
  print("Take these Trash and sort them out for me\n")
  
  #Apple Core
  print("Apple Core")
  
  core = input("\nTrash, Compost, or Recycle?(choose one): ").lower()
  
  while core !="compost":
    if (core == "trash") or (core == "recycle"):
      print("Not quite! Keep in mind an apple core is food and can decompose.")
      core = input("Trash, Compost, or Recycle?(choose one): ").lower()
      
    else:
      print("Check Spelling")
      core = input("Trash, Compost, or Recycle?(choose one): ").lower()

#Plastic Bottle
  print("\nThat’s right! Encouraging composting is crucial. Composting allows foods to decompose and turn into new materials or can be used as fertilizer.")
  print("\nPlastic Bottle")
  
  plastic_bottle = input("\nTrash, Compost, or Recycle?(choose one): ").lower()

  while plastic_bottle !="recycle":
    if (plastic_bottle == "trash") or (plastic_bottle == "compost"):
      print("Wrong! Remember that the bottle is plastic.")
      plastic_bottle = input("Trash, Compost, or Recycle?(choose one): ").lower()
    else:
      print("Check Spelling")
      plastic_bottle = input("Trash, Compost, or Recycle?(choose one): ").lower()

#Plastic Bag
  print("\nCorrect! Recycling Plastic Bottles allows natural resources to be conserved and save energy by repurposing plastics.")
  print("\nPlastic Bag")

  plastic_bag = input("\nTrash, Compost, or Recycle?(choose one): ").lower()

  while plastic_bag !="recycle":
    if (plastic_bag == "trash") or (plastic_bag == "compost"):
      print("Plastic can be reprocessed into new goods and can reduce the amount of plastic in landfills.")
      plastic_bag = input("Trash, Compost, or Recycle?(choose one): ").lower()
    else:
      print("Check Spelling")
      plastic_bag = input("Trash, Compost, or Recycle?(choose one): ").lower()
      
#Shattard Mirror
  print("\nThat's right! Now you\'re getting it")
  print("\nShattered Mirror")
  
  mirror = input("\nTrash, Compost, or Recycle?(choose one): ").lower()
  
  while mirror !="trash":
    if (mirror == "recycle") or (mirror == "compost"):
      print("Wrong! Glass shards are not decomposable and glass cannot be repurposed.")
      mirror = input("Trash, Compost, or Recycle?(choose one): ").lower()
    else:
      print("Check Spelling")
      mirror = input("Trash, Compost, or Recycle?(choose one): ").lower()

# Banana Peel
  print("\nCorrect! We can not recycle or compost mirrors.")
  print("\nBanana Peel")
  
  banana_peel = input("\nTrash, Compost, or Recycle?(choose one): ").lower()
  
  while banana_peel !="compost":
    if (banana_peel == "recycle") or (banana_peel == "trash"):
      print("Wrong! Food waste cannot be refused and throwing food waste into the landfill is not effective as food waste contains nutrients that can be used as fertilizer. ")
      banana_peel = input("Trash, Compost, or Recycle?(choose one): ").lower()
    else:
      print("Check Spelling")
      banana_peel = input("Trash, Compost, or Recycle?(choose one): ").lower()

# Styrofoam Cup
  print("\nCorrect! A banana peel is considered food waste and can be used to feed plants. This is the last one")
  print("\nStyrofoam Cup")
  
  cup = input("\nTrash, Compost, or Recycle?(choose one): ").lower()
  
  while cup !="trash":
    if (cup == "recycle") or (cup == "compost"):
      print("Wrong! The cup is not food waste and cannot be recycled due to its materials.")
      cup= input("Trash, Compost, or Recycle?(choose one): ").lower()
    else:
      print("Check Spelling")
      cup = input("Trash, Compost, or Recycle?(choose one):  ").lower()

  print("\nThank you for sorting through that trash! Your skills are impressive, and they will be vital as we move forward.")         
#LandFill()
def farm():
  explored1 = False
  explored2 = False
  explored3 = False
  explored4 = False

  print("\nThe villagers have reported being sick from consuming goods from Han’s Farmer Market. You visit Farmer Han to get a better understanding of how he produces his crops. He reports that he has been suffering from headaches and respiratory depression recently. As soon as you walk into the storage room, you notice a copious amount of FastCrops pesticide bottles lying around.")

  while (explored1 != True) or (explored2 != True) or (explored3 != True) or (explored4 != True):
      
    section = input("\nWhich section do you want to investigate?(1,2,3,4): ")
    if section == "1":
      if explored1 == False:
        print("\nYou notice the soil in section 1 has leaves that are colored yellow and brown. The leaves are also beginning to curl and wilt.")
        explored1 = True
          
          
          
      elif explored1 == True:
        print("\nYou already explored this section.")
          
          
  
      
    if section == "2":
      if explored2 == False:
        print("\nThe plant’s heighted as been shorter than the average plant from the past year. Additionally, the plant’s vigor has diminished showing signs of poor health.")
        explored2 = True
          
          
      else:
        print("\nYou already explored this section.")
          
  
      
    if section == "3":
      if explored3 == False:
        print("\nWhen getting close to the plants for inspection, you feel light headed and start to feel dizzy. ")
        explored3 = True
          
          
      else:
        print("\nYou already explored this section.")
          
  
      
    if section == "4":
      if explored4 == False:
        print("\nSmall levels of LD50 means the crops growing have a small tolerance to poison.")
        explored4 = True
          
      else:
        print("\nYou already explored this section.")
          



  print("\nAfter collecting the results, the lab concluded that Triclopyr has been disrupting the soil bacteria which can cause headaches and respiratory irritation.")

  print("Use your investigate skills to narrow down on the problem.")

  question1 = input("\nWhat type of pollution is this? \nA. Air\nB. Soil\nC. Water\nD. Land(Pick A. B. C. or D.): ").lower()

  while question1 !="b":
    
    if question1 == "a":
      print("\nAlthough this is a good solution, there is no place to put the contaminated soil section.. The economic loss for the farmer would shift the economy and ecosystem of Greenville makes this not an effective solution")
      question1 = input("\nWhat type of pollution is this? \nA. Air\nB. Soil\nC. Water\nD. Land(Pick A. B. C. or D.): ").lower()
      
    elif question1 == "b":
      print("\nCorrect! Since the main chemical is paraquat which is a lethal herbicide, microbes can break the herbicide down while also promoting plant growth for the next set of crops.")
      question1 = input("\nWhat type of pollution is this? \nA. Air\nB. Soil\nC. Water\nD. Land(Pick A. B. C. or D.): " ).lower()
  
    elif question1 == "c":
      print("\nNot as effective and there is still residue left after cleaning the produce")
      question1 = input("\nWhat type of pollution is this? \nA. Air\nB. Soil\nC. Water\nD. Land(Pick A. B. C. or D.): " ).lower()
    
    elif question1 == "d":
      print("\nThis can remove any pesticide that contacts the surface of the fruits, there can still be residue present in the flesh.")
      question1 = input("\nWhat type of pollution is this? \nA. Air\nB. Soil\nC. Water\nD. Land(Pick A. B. C. or D.): ").lower()
    
    else:
      print("Make sure to double check if you put a, b, c, or d")
      question1 = input("\nWhat type of pollution is this? \nA. Air\nB. Soil\nC. Water\nD. Land(Pick A. B. C. or D.): ").lower()

  print("\nYou decide to implement soil life (microbes) in order to break down the herbicides in order to solve the issue. Later studies have found that your solutioned helped with pesticide poisoning/soil pollution. Good job!")

  print("OVERVIEW:\nNot only are pesticides toxic to many organisms, pesticides remain in the soil for years and even decades, but with the help of microbes, the pesticides can decrease their presence within months. Additionally, it is important to look out for groundwater contamination because the water containing the pesticide can flow to a nearby river.")

  print("\nMayor Gives you word")
#farm()

#Prints out the Chesapeake Bay path
def pond():
    while True:
            #path1 = input('\nWhere would you like to investigate first.\nA. The Chesapeake Bay\nB. Farmstead\nC. Construction\nD. Landfill\nE. Forest\n').upper()
            #if path1 == ('A'):
        global letters
        print('You check the Chesapeake Bay where you encounter a fisherman. He looks destressed. You ask him what\'s wrong.')
        print('Fisherman: Recently, a lot of algae has been blooming in the water which causes coloration in the fishes.')
        print('You interview one of the locals nearby and one of the locals tells you that they\'ve been coming here every day to feed the fish. Another local tells you that excess fertilizers used by the local farm have been washed into the pond.')
        print('To investigate the problem further, you decide to take out your [Fishing Rod] from your inventory\n')
        fishing()
        while True:
            print('You noticed something odd. A bottle of fertilzer? This might be connected to the algae blooms\n')
            answer1 = input('What type of environmental issue is this?\nA. Water pollution\nB. Unauthorized Access to the Pond\nC. Littering\nD.increasing\n').upper()
            if answer1 == 'A':
                print('Correct\n')
                break
            else:
                print('Wrong. Try again.')
                    
        while True:
            answer2 = input('What do you think the direct cause of the issue?\nA. Overfeeding of fish\nB. Nutrient run off\nC. Climate change and rising temperature\nD. Increased rainfall and runoff\n').upper()
            if answer2 == 'A':
                print('Incorrect. Increase in fish population can contribute to nutrient levels by contributing organic material to the water, it is not a primary cause of significant algae blooms.')
            elif answer2 == 'B':
                print('Correct: Algae blooms are caused by excess nutrients in water. When they proliferate and then die, their decomposition consumes a significant amount of oxygen from the water. This depletion of oxygen suffocates fish and other wildlife.')
                break
            elif answer2 == 'C':
                print('Incorrect. Yes it can affect, it is not a direct cause')
            else:
                print('Incorrect. While runoff can wash pollutants into the water, it is not the main cause')

        while True:
            answer3 = input('What is the best course of action in order to combat water pollution, specifically algae buildup?\nA. Lowering pH by adding natural elements such as peat moss which is eco-friendly and aesthetically pleasing\nB. Use chemicals to kill the algae\nC. Fostering vegetarian that can absorb the excess nutrients in the pond waters\nD. Feed the fishes to improve their health\n').upper()
            if answer3 == 'A':
                print('Many water organisms are sensitive to changes in the water such as pH levels, they may do more harm than good.')
            elif answer3 == 'B':
                print('This may seem like a quick solution, this can lead to more problems. These chemicals can negatively affect the ecosystem.')
            elif answer3 == 'C':
                print('Correct solution. Fast growing stem plants like hornwort, wisteria and teardrop Rotala is effective at absorption excess nutrients')
                break
            else:
                print('Although it can help with fishes’ health, this will make the bloom worse because the fish will produce excess waste resulting in more nutrients in the pond. ')
        print('You decide to encourage the locals to plant fast growing stem plants that thrive under the unique situation of the pond in order to solve the issue. Later studies have found that your solutioned helped with the algae booming. Good job!\nThe mayor rewards you with a word\n')
        letters.append('Letter 1 - Act')
        print('Overview: Algae blooms are caused by excess amounts of nutrients like nitrogen and phosphorus in the water. This is normally caused by these nutrients, often found in fertilizer, running off into the water. When algae proliferate and then die, their decomposition consumes a significant amount of oxygen in the water, This is known as “Hypoxia”. Fishes and other water based organisms suffocate and die, negatively affecting the ecosystem. ')
        break             
#Print out the fishing command for pond
def fishing():
    global inventory
    while True:
        going_fish = input('Type \"fish\" to going fishing ').upper()
        if (going_fish == ('FISH')):
            print('Preparing to fish')
            break
        else:
            print('Incorrect. Please try again. This is case sensitive')

    #List of items that is count as "Junk"
    junk_list = ['Seaweed', 'Shoe', 'Can', 'Log']

    #Wait 3 seconds
    print('Fishing please wait.')
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)

    #Grabs a random item from list
    random_item = random.choice(junk_list)
    print(f'You collected a {random_item} and a bottle of fertilizer')
    inventory.remove('fishing rod')

#Intro to the game
print('Welcome to Eco-Detectives\n')
name = input('What is your name detective?\n').capitalize()
print(f'\nHello {name}. Today is your first day at department of Environmental Investigation Agency. Better known as EIA. I am your Senior, Jin Johnson.\n \nAs your first mission, you are assigned to investigate the environmental issues that is occuring in Baltimore Maryland. Head there immedietely and meet with the Mayor White.\n')
print('Ready for your first mission. You pack [fishing rod], a [trash grabber], [safety equipment], [sampling kit], and [seeds and trowel]. You can view your inventory at any time. You leave and travel to Baltimore.')

#Display waiting period (3 seconds)
def wait():
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)

wait()
print('You arrive at Baltimore Maryland. Something smells... fishy. The mayor greets you when you arrive.\n')
print('Mayor White: Hello. Thank you for coming. We have been in shambles lately! It seems like there are issues popping up everywhere and the environment is taking a toll. After every successful investigation, you will obtain a word that contributes to a phrase which will earn you a badge. You can access how much words you have at any given time.\n')

#What the user wants to do first
while True:
    choice1 = input('What would you like to do first? \n A. Investigate\n B. Check inventory\n C. Check your letters\n').upper()
    if choice1 == 'A':
        path1 = input('\nWhere would you like to investigate first.\nA. The Chesapeake Bay\nB. Farmstead\nC. Construction\nD. Landfill\nE. Forest\n').upper()
        if path1 == ('A'):
            if 'pond' not in path_taken:
                path_taken.append('pond')
                pond()
                break
            else:
                print('Overview: Algae blooms are caused by excess amounts of nutrients like nitrogen and phosphorus in the water. This is normally caused by these nutrients, often found in fertilizer, running off into the water. When algae proliferate and then die, their decomposition consumes a significant amount of oxygen in the water, This is known as “Hypoxia”. Fishes and other water based organisms suffocate and die, negatively affecting the ecosystem.') 
        elif path1 == 'B':
            if 'farm' not in path_taken:
               path_taken.append('farm')
               farm()
               break
            else:
               print('FILLER')
        elif path1 =='C':
            if 'landfill' not in path_taken:
               path_taken.append('landfill')
               LandFill()
               break
            else:
                print('FILLER')

    elif choice1 == 'B':
        print('\nThis is your current inventory')
        for items in inventory:
            # if item in inventory:
            print(", ".join(inventory) + '\n')
            break
        else:
            print('Nothing is here')
            break
    else:
        print('\nHere is all letters you have collected:' + '\n')
        print(', '.join(letters) + '\n')
    
#What the user wants to do second
while True:
    choice2 = input('What would you like to do next? \n A. Investigate\n B. Check inventory\n C. Check your letters\n').upper()
    if choice2 == 'A':
        path2 = input('\nWhere would you like to investigate next. Feel free to go back and relearn about the problem\nA. The Chesapeake Bay\nB. Farmstead\nC. Construction\nD. Landfill\nE. Forest\n').upper()
        if path2 == ('A'):
            if 'pond' not in path_taken:
                path_taken.append('pond')
                pond()
                break
            else:
                print('Overview: Algae blooms are caused by excess amounts of nutrients like nitrogen and phosphorus in the water. This is normally caused by these nutrients, often found in fertilizer, running off into the water. When algae proliferate and then die, their decomposition consumes a significant amount of oxygen in the water, This is known as “Hypoxia”. Fishes and other water based organisms suffocate and die, negatively affecting the ecosystem.') 
        elif path2 == 'B':
            if 'farm' not in path_taken:
               path_taken.append('farm')
               farm()
               break
            else:
               print('FILLER')
        elif path2 =='C':
            if 'landfill' not in path_taken:
               path_taken.append('landfill')
               LandFill()
               break
            else:
                print('FILLER')  
    elif choice2 == 'B':
        print('\nThis is your current inventory')
        for items in inventory:
            # if item in inventory:
            print(", ".join(inventory) + '\n')
            break
        else:
            print('Nothing is here')
            break
    else:
        print('\nHere is all letters you have collected:' + '\n')
        print(', '.join(letters) + '\n')