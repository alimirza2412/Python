import random 

subjects = ["Sharukh khan", "Virat Koli", "Gippi", "JOjo", "Amir Khan", "Salman Khan", "Imran Khan", "Nawaz Sharif", "Shahbaz Sharif", "Yousaf Raza Gilani", "Babar Azam"]

Actions = ["dances with", "cancels", "launches", "eats", "orders", "declare war on", "fights", "celeberates", "smiles", "eats", "jumps", "thinks", "runs", "kicks", "eats bananas"]

places_or_things = ["in Karachi", "in Lahore", "in Faisalabad", "in Islamabad", "in Dehli", "in Pakpattan", "in Sialkot", "in Paris", "in London", "in New york", "in Swat", "in Skardu", "in Rawal Pindi", "Inside Parliment", "during the match", "cup of chai",]


while True:
    subject = random.choice(subjects)
    Action = random.choice(Actions)
    place = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {Action} {place}"
    print("\n" + headline)

    user_input  = input("\n Do you want an other headline? (yes/no)").strip()  # strip removes extra spaces
    
    if user_input == "no":
        break

print("\n Thanks for using using the Fake News Headline Geneator. Have a fun day")