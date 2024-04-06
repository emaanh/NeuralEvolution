import sys
import os
from environment import Environment
import time
from datetime import datetime, timedelta
import time
import matplotlib.pyplot as plt

import sys

def process_command_line_arguments():
    # Default values
    args_dict = {
        'height': 10,  # Default board size height
        'width': 10,   # Default board size width
        'filename': "idealWeights.txt",  # Default filename for TESTING
        'runs': 1,  # Default runs
        'total_variations': 1  # Only used for TRAINING
    }
    
    # Parsing key-value pair arguments
    for arg in sys.argv[1:]:  # Skip the script name itself
        if '=' in arg:
            key, value = arg.split('=', 1)
            # Handling different types of arguments
            if key in args_dict:
                if key in ['height', 'width', 'runs', 'total_variations']:
                    args_dict[key] = int(value)  # Convert numerical values to integers
                else:
                    args_dict[key] = value  # Keep string values as is
    
    # Determine option based on the presence of "filename"
    if "filename" in args_dict and args_dict['filename'] != "idealWeights.txt" or len(sys.argv)==1:
        testingOption = True
    else:
        testingOption = False    
        
    
    # Prepare the return value
    height = args_dict['height']
    width = args_dict['width']
    filename = args_dict['filename']
    runs = args_dict['runs']
    total_variations = args_dict['total_variations']
    
    return height, width, testingOption, filename, runs, total_variations


def create_filename():
    current_datetime = datetime.now()
    return current_datetime.strftime('%d_%H-%M')

def format_seconds(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        remaining_seconds = int(seconds % 60)
        return f"{hours} hours, {minutes} minutes, {remaining_seconds} seconds"

def printExecutionTime(totalVariants,runsPerVariant):
    seconds = totalVariants*runsPerVariant*0.00003838510036
    print("Estimated Time:", format_seconds(seconds))
    current_timestamp = time.time()
    current_datetime = datetime.fromtimestamp(current_timestamp)
    finish_datetime = current_datetime + timedelta(seconds=seconds)
    finish_time_str = finish_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Finish time: {finish_time_str}")
    
    
    
    
if __name__ == '__main__':
    
    height, width, testingOption, readWeightsFilename, runsPerVariant, totalVariants = process_command_line_arguments()
    maxMoves = int((width + height)*1.5) #Maximum number of moves before failure
    failureCost = maxMoves+5 #Cost for failing to find (hit wall or run out of moves)


    minCount = float('inf') #Initial Lowest Count
    bestNN = []     
    minHistory = [] #For Plotting
    vHistory = [] # For Plotting
    failed = 0
    sleep = 1
    
    if not testingOption:
        printExecutionTime(totalVariants, runsPerVariant)
    
    for v in range(totalVariants):
        environment = Environment(width, height)
        if testingOption:
            environment.loadWeights(readWeightsFilename)
        totalCount = 0
        
        for i in range(runsPerVariant):
            counter = 0
            found = 0
            
            if testingOption:
                print()

            while found == 0 and counter < maxMoves:

                if testingOption:   
                    print(environment.toString())
                    print("Moves:", counter, "\n")  
                    time.sleep(sleep)
                
                found = environment.tickTime()
                counter +=1
            
            counter -=1
            if testingOption:
                print(environment.toString())
                
            if found == 1:
                totalCount += counter
                if testingOption:  
                    print("Moves:",counter, "–––FOUND–––", "\n")
                    time.sleep(sleep)
                
            elif found == -1:
               
                totalCount += failureCost
                failed +=1
                if testingOption:        
                    print("Moves:",counter, "–––HIT WALL–––", "\n")
                    time.sleep(sleep)
            else:
                totalCount += failureCost
                failed +=1
                if testingOption:
                    print("Moves:",counter, "–––NO MOVES LEFT–––", "\n")
                    time.sleep(sleep)
                
            environment.relocateOrganism()
            environment.relocateGoal()
        
        if not testingOption:
            optimizer = totalCount/runsPerVariant
            
            if optimizer < minCount:
                minCount = optimizer
                bestNN = environment.getWeights()
            
            if v%100 == 0:  
                minHistory.append(minCount)
                vHistory.append(v)
                print("Percent Done:", str(round(v/totalVariants * 100,2))+"%")
            
    if not testingOption:
        print("Minimum Avg Count Found: ",minCount)

        weights_ = bestNN[0]
        architecture = bestNN[1]
        filename = create_filename() + ".txt"

        path = os.path.join("Weights",  filename)
        with open(path, 'w') as file:
            file.write(", ".join(map(str, architecture)) + "\n")
            for layer in weights_:
                for node in layer:
                    file.write(",".join(map(str, node)))
                    file.write(",")
                    
        
        plt.plot(vHistory, minHistory)
        plt.title('Training Graph: '+ filename)
        plt.xlabel('Variants')
        plt.ylabel('Performance')
        plt.show()
            

