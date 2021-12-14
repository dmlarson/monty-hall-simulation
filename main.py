import argparse
import random
import copy
from multiprocessing import Pool

def main():
    parser = argparse.ArgumentParser(description='Simulator for the monty hall problem')
    parser.add_argument('-p', '--parallel', help='run simulations in parallel', action="store_true")
    parser.add_argument('doors', type=int, help='number of doors for this simulation', default=3)
    parser.add_argument('iterations', type=int, help='number of times to run the simulation', default=100)
    args = parser.parse_args()

    wins = 0
    if args.parallel:
        inputs = [args.doors] * args.iterations
        with Pool(16) as p:
            outputs = p.map(simulate, inputs)
            wins = sum(outputs)
    else:
        for x in range(args.iterations):
            wins += simulate(args.doors)
    
    exp_win_rate = wins/args.iterations
    hyp_win_rate = 1/(args.doors-1)

    print(F" {exp_win_rate} vs {hyp_win_rate}")
    
def simulate(num_of_doors):
    door_list = list(range(1, num_of_doors+1))
    #select correct
    correct = random.choice(door_list)
    #make door choice
    first_choice = random.choice(door_list)
    #remove door that doesnt contain correct or choice
    removed_door_list = copy.deepcopy(door_list)
    removed_door_list.remove(correct)
    if first_choice != correct:
        removed_door_list.remove(first_choice)
    door_to_remove = random.choice(removed_door_list)
    door_list.remove(door_to_remove)
    #move the door choice
    final_choice = random.choice(door_list)
    #check if win or lose
    if final_choice == correct:
        return 1

    return 0


if __name__ == "__main__":
    main()
