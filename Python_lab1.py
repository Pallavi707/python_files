#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Game:
        
        animals = [
            "Aardvark",
            "Albatross",
            "Alligator",
            "Alpaca",
            "Ant",
            "Anteater",
            "Antelope",
            "Ape",
            "Armadillo",
            "Donkey",
            "Baboon",
            "Badger",
            "Barracuda",
            "Bat",
            "Bear",
            "Beaver",
            "Bee",
            "Bison",
            "Boar",
            "Buffalo",
            "Butterfly",
            "Camel",
            "Capybara",
            "Caribou",
            "Cassowary",
            "Cat",
            "Caterpillar",
            "Cattle",
            "Chamois",
            "Cheetah",
            "Chicken",
            "Chimpanzee",
            "Chinchilla",
            "Chough",
            "Clam",
            "Cobra",
            "Cockroach",
            "Cod",
            "Cormorant",
            "Coyote",
            "Crab",
            "Crane",
            "Crocodile",
            "Crow",
            "Curlew",
            "Deer",
            "Dinosaur",
            "Dog",
            "Dogfish",
            "Dolphin",
            "Dotterel",
            "Dove",
            "Dragonfly",
            "Duck",
            "Dugong",
            "Dunlin",
            "Eagle",
            "Echidna",
            "Eel",
            "Eland",
            "Elephant",
            "Elk",
            "Emu",
            "Falcon",
            "Ferret",
            "Finch",
            "Fish",
            "Flamingo",
            "Fly",
            "Fox",
            "Frog",
            "Gaur",
            "Gazelle",
            "Gerbil",
            "Giraffe",
            "Gnat",
            "Gnu",
            "Goat",
            "Goldfinch",
            "Goldfish",
            "Goose",
            "Gorilla",
            "Goshawk",
            "Grasshopper",
            "Grouse",
            "Guanaco",
            "Gull",
            "Hamster",
            "Hare",
            "Hawk",
            "Hedgehog",
            "Heron",
            "Herring",
            "Hippopotamus",
            "Hornet",
            "Horse",
            "Human",
            "Hummingbird",
            "Hyena",
            "Ibex",
            "Ibis",
            "Jackal",
            "Jaguar",
            "Jay",
            "Jellyfish",
            "Kangaroo",
            "Kingfisher",
            "Koala",
            "Kookabura",
            "Kouprey",
            "Kudu",
            "Lapwing",
            "Lark",
            "Lemur",
            "Leopard",
            "Lion",
            "Llama",
            "Lobster",
            "Locust",
            "Loris",
            "Louse",
            "Lyrebird",
            "Magpie",
            "Mallard",
            "Manatee",
            "Mandrill",
            "Mantis",
            "Marten",
            "Meerkat",
            "Mink",
            "Mole",
            "Mongoose",
            "Monkey",
            "Moose",
            "Mosquito",
            "Mouse",
            "Mule",
            "Narwhal",
            "Newt",
            "Nightingale",
            "Octopus",
            "Okapi",
            "Opossum",
            "Oryx",
            "Ostrich",
            "Otter",
            "Owl",
            "Oyster",
            "Panther",
            "Parrot",
            "Partridge",
            "Peafowl",
            "Pelican",
            "Penguin",
            "Pheasant",
            "Pig",
            "Pigeon",
            "Pony",
            "Porcupine",
            "Porpoise",
            "Quail",
            "Quelea",
            "Quetzal",
            "Rabbit",
            "Raccoon",
            "Rail",
            "Ram",
            "Rat",
            "Raven",
            "Red deer",
            "Red panda",
            "Reindeer",
            "Rhinoceros",
            "Rook",
            "Salamander",
            "Salmon",
            "Sand Dollar",
            "Sandpiper",
            "Sardine",
            "Scorpion",
            "Seahorse",
            "Seal",
            "Shark",
            "Sheep",
            "Shrew",
            "Skunk",
            "Snail",
            "Snake",
            "Sparrow",
            "Spider",
            "Spoonbill",
            "Squid",
            "Squirrel",
            "Starling",
            "Stingray",
            "Stinkbug",
            "Stork",
            "Swallow",
            "Swan",
            "Tapir",
            "Tarsier",
            "Termite",
            "Tiger",
            "Toad",
            "Trout",
            "Turkey",
            "Turtle",
            "Viper",
            "Vulture",
            "Wallaby",
            "Walrus",
            "Wasp",
            "Weasel",
            "Whale",
            "Wildcat",
            "Wolf",
            "Wolverine",
            "Wombat",
            "Woodcock",
            "Woodpecker",
            "Worm",
            "Wren",
            "Yak",
            "Zebra"
         ]

       
        def __init__(self,name,place,animal,thing,first):
       
            
            self.name = name
            self.place = place
            self.animal = animal
            self.thing = thing
            self.r = first
            self.n = self.name.capitalize()
            self.p = self.place.capitalize()
            self.a = self.animal.capitalize()
            self.t = self.thing.capitalize()
            self.score = 0
       
        def test(self):
            x=range(10)
            for i in x:
                if str(i) in self.name or str(i) in self.place or str(i) in self.thing:
                    return True           
                             
                
               
            for i in "!|/,.@#$%^&*()_+":
                if i in self.name or i in self.place or i in self.thing:
                    return True
           
            if self.animal.capitalize() not in Game.animals:
                return True           
            if self.n[0] != self.r or self.p[0] != self.r or self.t[0] != self.r or self.a[0] != self.r:
                return True
            
            return False
       
            # for x in self.name or x in self.place or x in self.thing :
#                 if type(x) == int or self.animals not in Game.animals:
#                      return True
#                 elif x == y in "!|/,.@#$%^&*()_+":                
#                      return True
                       
               
        def scoreMe(self):
            print(f'self.test: {self.test()}')
            if self.test()== True:
                self.score = 0

            else:
                self.score = 1
         
       
   
        def __str__(self):
            return "\nYour score is {} : \n".format(self.score)
        
           








# In[5]:


import random


# In[7]:



       first = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')



       print("The names must begin with the letter {}".format(first))
       print("PLAYER 1")

       n1 = input("Enter a name : \n")
       p1 = input("Enter a place: \n ")
       a1 = input("Enter a animal : \n")
       t1 = input("Enter a thing : \n")

       player1 = Game(n1,p1,a1,t1,first)
       player1.scoreMe()
       p1_score = player1.score
       print(player1)


       "PLAYER 2"
       print("PLAYER 2")
       n2 = input("Enter a name : \n")
       p2= input("Enter a place :\n ")
       a2= input("Enter a animal :\n ")
       t2= input("Enter a thing : \n")


       player2 = Game(n2,p2,a2,t2,first)
       player2.scoreMe()
       p2_score = player2.score
       print(player2)

       print(f'p1:{p1_score},p2:{p2_score}')
       if(p1_score > p2_score):
           print("\nPlayer_1 wins")
       elif p1_score == p2_score:
           print("\nIt's a Tie")

       else:
           print("\nPlayer_2 wins")


# In[ ]:





# In[ ]:




