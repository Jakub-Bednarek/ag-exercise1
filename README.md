
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
### Configurations of simulations executed
### Mutation and crossover probability impact
#### Mutation results
`Low-Dimensional-Data`
![low_dimensional_mutation_results](example/output/mutation_crossover/mutation/low_dimensional/file_1_results.png)
Test was done using 5 values for mutation probability: 2%, 4%, 6%, 8% and 10%.
The most significant difference visible is that lower probability chance yields more stable results over time. Each variant with mutation probability equal or higher than 6% show high variance of results, thus lowering average score for all generations.
`High-Dimensional-Data`
![high_dimensional_mutation_results](example/output/mutation_crossover/mutation/high_dimensional/file_5_results.png)
Similar results can be seen in large scale datasets. The form is slightly different due to very strict constrain on total backpack size resulting in extremely fast degradation of candidates fitness.
For 8% and 10% mutation probability, second iteration already brought highest score to 0 which stayed for the rest of simulation.
6% and 4% runs were slightly better, 0 fitness level was achieved after 4th and 6th iteration respectively.
Last mutation probability candidate - 2%, yield completely different results. Instead of degrading the score it actually improves it with each iteration reaching close to 6500 fitness score mark.
#### Crossover results
`Low-Dimensional-Data`
![low_dimensional_crossover_results](example/output/mutation_crossover/crossover/low_dimensional/file_1_results.png)
At first glance, crossover modification impact is not as extreme as mutation. Probabilities for mutation were exactly the same as for the mutation.
Each run comes with very similar results which are stable, but vary in the overall level.
Lower crossover chance allows to reach highest possible score with ease, which is kept till the end of simulation.
For higher crossover chances, maximum score goes down by up to 10% being most significant with 10% crossover chance.  
`High-Dimensional-Data`
![high_dimensional_crossover_results](example/output/mutation_crossover/crossover/high_dimensional/file_5_results.png)
Large scale dataset doesn't confirm observation from smaller size datasets. Looking at 4% crossover chance, we notice that even though it start strong being in the middle of all simulations, after 5th iteration overall score becomes the lowest among all simulations.
Results seem to be more or less random which is very different from low dataset tests. 
### Rank and roulette selection function comparison
### Single and double point crossover comparison
### Rank, roulette and tournament selection function comparison

