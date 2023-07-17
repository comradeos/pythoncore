import random
import os


def get_random_ignore_file():
    adjectives = [
        "adorable",
        "adventurous",
        "aggressive",
        "agreeable",
        "alert",
        "alive",
        "amused",
        "angry",
        "annoyed",
        "annoying",
        "anxious",
        "arrogant",
        "ashamed",
        "attractive",
        "average",
        "awful",
        "bad",
        "beautiful",
        "better",
        "bewildered",
        "black",
        "bloody",
        "blue",
        "blue-eyed",
        "blushing",
        "bored",
        "brainy",
        "brave",
        "breakable",
        "bright",
        "busy",
        "calm",
        "careful",
        "cautious",
        "charming",
        "cheerful",
        "clean",
        "clear",
        "clever",
        "cloudy",
        "clumsy",
        "colorful",
        "combative",
        "comfortable",
        "concerned",
        "condemned",
        "confused",
        "cooperative",
        "courageous",
        "crazy",
        "creepy",
        "crowded",
        "cruel",
        "curious",
        "cute",
        "dangerous",
        "dark",
        "dead",
        "defeated",
        "defiant",
        "delightful",
        "depressed",
        "determined",
        "different",
        "difficult",
        "disgusted",
        "distinct",
        "disturbed",
        "dizzy",
        "doubtful",
        "drab",
        "dull",
    ]
    
    nouns = [
        "Ability",
        "Access",
        "Accident",
        "Account",
        "Act",
        "Action",
        "Activity",
        "Actor",
        "Ad",
        "Addition",
        "Address",
        "Administration",
        "Advantage",
        "Advertising",
        "Advice",
        "Affair",
        "Age",
        "Agency",
        "Agreement",
        "Air",
        "Airport",
        "Alcohol",
        "Ambition",
        "Amount",
        "Analysis",
        "Analyst",
        "Animal",
        "Answer",
        "Anxiety",
        "Apartment",
        "Appearance",
        "Apple",
        "Application",
        "Appointment",
        "Area",
        "Argument",
        "Army",
        "Arrival",
        "Art",
        "Article",
        "Aspect",
        "Assignment",
        "Assistance",
        "Assistant",
        "Association",
        "Assumption",
        "Atmosphere",
        "Attempt",
        "Attention",
        "Attitude",
        "Audience",
        "Aunt",
        "Average",
        "Awareness",
        "Back",
        "Bad",
        "Balance",
        "Ball",
        "Bank",
        "Baseball",
        "Basis",
        "Basket",
        "Bath",
        "Bathroom",
        "Bedroom",
        "Beer",
        "Beginning",
        "Benefit",
        "Bird",
        "Birth",
        "Birthday",
        "Bit",
        "Blood",
        "Board",
        "Boat",
        "Body",
        "Bonus",
        "Book",
        "Boss",
        "Bottom",
        "Box",
        "Boy",
        "Boyfriend",
        "Bread",
        "Breath",
        "Brother",
        "Building",
        "Bus",
        "Business",
        "Buyer",
        "Cabinet",
        "Camera",
        "Cancer",
        "Candidate",
        "Capital",
        "Car",
        "Card",
        "Care",
        "Career",
        "Case",
        "Cash",
        "Cat",
        "Category",
        "Cause",
        "Celebration",
        "Cell",
        "Championship",
        "Chance",
        "Chapter",
        "Charity",
        "Cheek",
        "Chemistry",
        "Chest",
        "Chicken",
        "Child",
        "Childhood",
        "Chocolate",
        "Choice",
        "Church",
        "Cigarette",
        "City",
        "Class",
        "Classroom",
        "Client",
        "Climate",
        "Clothes",
        "Coast",
        "Coffee",
        "Collection",
        "College",
        "Combination",
        "Committee",
        "Communication",
        "Community",
        "Company",
        "Comparison",
        "Competition",
        "Complaint",
        "Computer",
        "Concept",
        "Conclusion",
        "Condition",
        "Confusion",
        "Connection",
        "Consequence",
        "Construction",
        "Contact",
        "Context",
        "Contract",
        "Contribution",
        "Control",
        "Conversation",
        "Cookie",
        "Country",
        "County",
        "Courage",
        "Course",
        "Cousin",
        "Craft",
        "Credit",
        "Criticism",
        "Culture",
        "Currency",
        "Customer",
        "Cycle",
        "Dad",
        "Data",
        "Database",
        "Date",
        "Day",
        "Dealer",
        "Death",
        "Debt",
        "Decision",
        "Definition",
        "Delivery",
        "Demand",
        "Department",
        "Departure",
        "Depression",
        "Depth",
        "Description",
        "Design",
        "Desk",
        "Development",
        "Device",
        "Diamond",
        "Difference",
        "Difficulty",
        "Dinner",
        "Direction",
        "Director",
        "Dirt",
        "Disaster",
        "Discipline",
        "Discussion",
        "Disease",
        "Disk",
        "Distribution",
        "Dog",
        "Drama",
        "Drawer",
        "Drawing",
        "Driver"
    ]
    
    abc = "abcdefghijkklmnopqrstuvwxyz"
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(10, 1000000)
    
    ext = "."
    ext += random.choice(abc)
    ext += random.choice(abc)
    
    result = adjective+noun+str(number)+ext
    return result

def add_auto_commits_to_gitignore():
    target_line = "auto_commits.py\n"
    
    with open(".gitignore", "r") as file:
        lines = file.readlines()
        
    if target_line not in lines:
        lines.append("\n")
        lines.append(target_line)
    
    with open(".gitignore", "w") as file:
        file.writelines(lines)


def add_random_ignore_file():
    with open(".gitignore", "a+") as file:
        random_ignore_file = get_random_ignore_file()
        file.write(f"{random_ignore_file}\n")
        print(random_ignore_file)

def remove_last_line():
    with open(".gitignore", "r") as file:
        lines = file.readlines()
    
    lines = lines[:-1]
    
    with open(".gitignore", "w") as file:
        file.writelines(lines)
 
        
def main():
    current_dir = os.path.dirname(__file__)
    os.chdir(current_dir)
    
    add_auto_commits_to_gitignore()
    
    counter = input("Number of commits: ")
    
    try:
        counter = int(counter)
    except:
        counter = 0
    
    for i in range(counter):
        add_random_ignore_file()
        
        os.system("git add .")
        os.system("git commit . -m updated")
        
        remove_last_line()
        
        os.system("git add .")
        os.system("git commit . -m updated")
        
    os.system("git push --all")
    input()
if __name__ == "__main__":
    main()