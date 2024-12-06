
# Genetic algorithm course realizatoin
## Idea
Program created for the course "Genetic algorithms" covers base structure of genetic algorithms scheme, providing flexible environment to experiment with. Script covers topics like population generation, mutation, single and double point crossover on candidates and 3 basic selection functions: roulette, rank and tournament.

## Usage
The script can be executed in 2 modes:
* `normal_run` - user can freely select parameters for the simulation
* `example_run` - predefined set of simulations based on input data files included in the project presenting capabilities of the program

Starting the script is as simple as running: `./run.py` with chosen set of arguments.
### Normal run
In order to fully customize the simulation you should choose `normal_run` option for the execution.

Parameters available for customization:
* `-i, --input` - Path to input file with data to be loaded. Can be either relative or absolute path.
* `-s, --population-size` - Size of the population to be generated and later simulated.
* `-n, --iterations` - Number of iterations or steps that the population will go through. Each step consists of calculation phase to determine candidate with highest fitness, and genetic modification step.
* `-a, --selection-function` - Selection function to be used for creation of new population. Available functions: `ROULETTE, TOURNAMENT, RANK`
* `-c, --crossover-probability` - Crossover chance for each candidate during genetic modification step. Must be between 0.0 and 1.0.
* `-m, --mutation-probability` - Mutation chance for each separate gene of the candidate, evaluated during genetic modification step. Must be between 0.0 and 1.0.
* `-d, --double-point-crossover` - Changes algorithm used by crossover function from single point to double point crossover.

Example usage: `./run.py run_normal -i data/my_input_file.txt -s 1000 -n 500 -a RANK -c 0.1 -m 0.01` 

### Example run
Example dataset has been prepared with multiple simulation tests to show capabilities of the script and behavior of genetic algorithms implemented.
Repository comes with predefined set of data available under `data/` directory.
Each set of tests generates plot as an output, results are also available in the repository under `example/output` directory.

If you want to generate such output yourself, you can execute `example run` by running: `./run.py run_example`

## Results analysis
### Configurations of simulations exectued
### Mutation and crossover probability impact
#### Mutation results
#### Crossover results
### Rank and roulette selection function comparison
### Single and double point crossover comparison
### Rank, roulette and tournament selection function comparison

