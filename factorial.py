# Created by: Ferdous Sediqi
# Created on: April. 17 2022
# created by: Ferdous Sediqi
# Modified on: April 20, 2022
# This program asks the user to enter a whole number
# and then uses a do while loop to calculate and display the factor
# of the number

def main():
    # initialize the loop counter and sum
    loop_counter = 0
    factor = 1

    # get the user number as a string
    user_num_as_string = input("Enter a whole number: ")
    print("")

    try:
        # change input to int
        user_num_as_int = int(user_num_as_string)
        if user_num_as_int < 0:
            print("Input was not a positive number.")
            exit()
        else:
            # calculate the factore
            while True:
                loop_counter = loop_counter + 1
                print("Tracking {} times through loop.".format(loop_counter))
                factor = factor * loop_counter
                print("")
                if loop_counter >= user_num_as_int:
                    break
       
            
    # display invalid input
    except Exception:
        print("")
        print("input is not an integer.")
        exit()
        
    print("{}! = {}". format(user_num_as_int, factor))



if __name__ == "__main__":
    main()
