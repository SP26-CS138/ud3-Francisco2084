'''
DEVELOPER(S): Francisco Segovia
Collaborator: Real Python website for help with methods
DATE: 04/27/2026
'''

"""
A hike finder within San Diego that filters using elevation gain and distance.


This Program reads a database of local hikes. Allows the user to set their physical limits then uses boolean logic to sort
the hikes, and outputs the sorted list of matches on the screen and into a file. The program also utilizes a
while loop to repeat the program until the user is done. 

Sources:
Hike info, https://www.alltrails.com/
"""


##########################################
# FUNCTIONS:
##########################################
def get_hike_data(filename):
    """Read hikes.txt data and return a list"""
    hike_list = []
    #opening file in read mode
    infile = open(filename, "r")
    for line in infile:
        data = line.strip().split(",")
        # Creating a list for each hike: [Name, Difficulty, Distance, Elevation]
        hike_info = [data[0], data[1], float(data[2]), int(data[3])]
        hike_list.append(hike_info)
    infile.close()
    return hike_list

def sort_by_distance(hike):
      """Function to return distance variable for sorting method"""
      return hike[2]


##########################################
# MAIN PROGRAM:
##########################################
def main():
    """Handle the user interface and the primary filtering logic."""
    #I am using a List instead of Dictionary because the data needs to be filtered and sorted. 
    #Lists are easier to re-order using the .sort() method in comparison to Dictionaries.

    #load the data
    all_hikes = get_hike_data("hikes.txt")

    #Introduction text and data ranges
    print("Welcome to the san Diego hike finder!")
    print("Hiking is a great way to get exercise and socialize,")
    print("we have a great range of options for hikes in San Diego")
    print("We have distances ranging from 2.1 to 11.3 miles,")
    print("And elevation gain ranging from 78 to 3,532 feet")
    print("lets learn more about your preffered hikes. \n")
    repeat_program = "yes"
    while repeat_program.lower() == "yes":
        #user preferences
        try:
            user_max_dist = float(input("Enter you maximum distance in miles: "))
            user_max_elev = int(input("Enter you maximum elevation gain in feet: "))
        except ValueError:
             print("Please enter a valid number for distance and elevation.")
             continue
        if (user_max_dist < 2.1 or user_max_dist > 11.3) or (user_max_elev < 78 or user_max_elev > 3532):
            print("Values out of acceptable ranges!")
            continue
        
        #filtering logic
        matches = []
        for hike in all_hikes:
             #Check to see hike limtis are under user preferences
             if hike[2] <= user_max_dist and hike[3] <= user_max_elev:
                  matches.append(hike)

        #sorting hikes from shortest to longest
        matches.sort(key=sort_by_distance)

        #displaying results by category
        if len(matches) > 0:
             print(f"\n---Recommended Hikes Under {user_max_dist} Miles---")
             outfile = open("my_hikes.txt", "w")
             outfile.write(f"Results for Max Distance: {user_max_dist} miles \n")

             for h in matches:
                #Displays hike and categorizes is (Easy/Medium/Hard)
                result = f"- {h[0]} [{h[1]}] - {h[2]} miles ({h[3]} ft gain)"
                print(result)
                outfile.write(result + "\n")
            
             outfile.close()
             print("\nYour list has been saved to'my_hikes.txt'.")
        else:
            print("\nNo hikes found matching those specific limits.")

        # Loop control
        repeat_program = input("\nWould you like to search again? (yes/no): ").strip().lower()

    print("\nThank you for using the Trail Guide. Enjoy your hike!")

if __name__ == "__main__":
    main()
    


