import sys

def cat_shelter_data(datafile):
    '''Analysing the cat's shelter log data and calculating the required statistics.
       
       Parameter : datafile: log file containing all the data about the cat's entry and exit time.
       
       prints: cat's visit, other cat's visit, our cat's total time in house, 
               Average visit length, longest visit , and shortest visit'''
    try:
        with open(datafile, 'rt') as file:#opens and reads the file
            lines= file.readlines()[:-1]
            
            our_cat_entries = 0
            their_cat_entries = 0
            our_cat_total_time = 0
            min_visit_time = float('inf') 
            max_visit_time = 0

            for line in lines:
                

                data = line.strip().split(',') #splits the line where 'comma' is present. (creates list)
                
                type_of_cat, entry_time, exit_time = data  #unpacking data

                #type-casting: string to integer-data-type
                entry_time, exit_time = int(entry_time) , int(exit_time)
                total_duration = exit_time - entry_time
    

                if type_of_cat == 'OURS':
                    our_cat_entries = our_cat_entries + 1
                    our_cat_total_time = our_cat_total_time + total_duration
                    
                    min_visit_time = min(min_visit_time, total_duration)
                    max_visit_time = max(max_visit_time, total_duration)
                
                elif type_of_cat == 'THEIRS':
                    their_cat_entries = their_cat_entries + 1
                 
            print(f"Cat Visits: {our_cat_entries}")
            print(f"Other Cats: {their_cat_entries}")
            print()   
            

            avg_time = our_cat_total_time // our_cat_entries #(//-floor division removes numbers after decimal)
            
            #converting into hour
            total_time_hour = our_cat_total_time // 60
            
            #converting into minutes
            total_time_minutes = our_cat_total_time % 60
            
            print(" Log File Analysis")   
            print("===================\n")
            print(f"Total Time in House: {total_time_hour} Hours, {total_time_minutes} Minutes")
            print()
            print(f"Average Visit Length: {avg_time} Minutes")
            print(f"Longest Visit: {max_visit_time} Minutes")
            print(f"Shortest Visit: {min_visit_time} Minutes")

    except FileNotFoundError:
        print(f"Error!!! File '{datafile}' not found.")
    except Exception as e:
        print("error")


try:
    choice = sys.argv[1]
    cat_shelter_data(choice)
except IndexError:
    print("Error! Please provide the log file as command line argument.")