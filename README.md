
# Genetic algorithm course realizatoin
## Idea
Program created for the course "Genetic algorithms" covers base structure of genetic algorithms scheme, providing flexible environment to experiment with.\
Script covers topics like population generation, mutation, single and double point crossover on candidates and 3 basic selection functions: roulette, rank and tournament.

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
Example dataset has been prepared with multiple simulation tests to show capabilities of the script and behavior of genetic algorithms implemented.\
Repository comes with predefined set of data available under `data/` directory.\
Each set of tests generates plot as an output, results are also available in the repository under `example/output` directory.\
\
If you want to generate such output yourself, you can execute `example run` by running: `./run.py run_example`

## Results analysis
### Configurations of simulations executed
### Mutation and crossover probability impact
#### Mutation results
`Low-Dimensional-Data`
![low_dimensional_mutation_results](example/output/mutation_crossover/mutation/low_dimensional/file_1_results.png)
\
Test was done using 5 values for mutation probability: 2%, 4%, 6%, 8% and 10%.\
The most significant difference visible is that lower probability chance yields more stable results over time. Each variant with mutation probability equal or higher than 6% show high variance of results, thus lowering average score for all generations.\
`High-Dimensional-Data`
![high_dimensional_mutation_results](example/output/mutation_crossover/mutation/high_dimensional/file_9_results.png)
\
Similar results can be seen in large scale datasets. The form is slightly different due to very strict constrain on total backpack size resulting in extremely fast degradation of candidates fitness.\
For 6%, 8% and 10% mutation probability, second or even first iteration already brought highest score to 0 which stayed for the rest of simulation.\
4% runs much better, allowing the population to staty at respectable level throughout the simulation.\
Last mutation probability candidate - 2%, yield the best different results. Instead of degrading the score it actually improves it with each iteration reaching close to 1500 fitness score mark.
#### Crossover results
`Low-Dimensional-Data`
![low_dimensional_crossover_results](example/output/mutation_crossover/crossover/low_dimensional/file_1_results.png)
At first glance, crossover modification impact is not as extreme as mutation. Probabilities for mutation were exactly the same as for the mutation.
Each run comes with very similar results in terms of stability, but vary in the overall fitness level.
Lower crossover chance allows to reach close to the highest possible score with ease, which is kept till the end of simulation.\
For higher crossover chances, maximum score goes down by up to 40%. \
`High-Dimensional-Data`
![high_dimensional_crossover_results](example/output/mutation_crossover/crossover/high_dimensional/file_9_results.png)
\
Large scale dataset doesn't confirm observation from smaller size datasets.\
Looking at 4% crossover chance, we notice that even though it start strong being in the middle of all simulations, after 5th iteration overall score becomes the lowest among all simulations.\
Results seem to be much closer to the highest overall score, which is achieved by 6% crossover chance probability. 
### Rank and roulette selection function comparison
`Low-Dimensional-Data`
![low_dimensional_rank_vs_roulette_results](example/output/rank_vs_roulette/low_dimensional/file_1_results.png)
\
For small size datasets there is visible difference. As presented above, roulette selection method takes more time to improve and has difficulties getting to the optimal score.\
The theory is that on bigger datasets, rank selection should yield better overall and highest adaptation score. Next paragraph should confirm or deny the thesis.\
`High-Dimensional-Data`
![high_dimensional_rank_vs_roulette_results](example/output/rank_vs_roulette/high_dimensional/file_9_results.png)
\
As visible above, theory is not correct. Roulette selection algorithm not only reaches higher best score, but allows improvement on fitness score throughout the simulation.\
Rank selection on the other hand shows high variance, which is mitigated with later iterations. The situation is completly opposite to small dataset results.
### Single and double point crossover comparison
`Low-Dimensional-Data`
![low_dimensional_single_vs_double_crossover_results](example/output/single_vs_double_point_crossover/low_dimensional/file_1_results.png)
\
With small sample size it's hard to determine whether single or double point crossover algorithm yields better results. The only observation that is worth noting is that double point crossover has smaller steps in terms of highest fitness level for first few iterations. \
Single point crossover is more aggressive and risky - it seems that we are facing a high risk, high reward type of approach.\
`High-Dimensional-Data`
![high_dimensional_single_vs_double_crossover_results](example/output/single_vs_double_point_crossover/high_dimensional/file_9_results.png)
\
This time, we can see slight domination of double point crossover over single point. Theory from previous tests seems to be somewhat false as increases between each iteration are more significant for double point crossover. In this case, double point crossover is a clear winner achieving higher fitness level throughout the iteration.
\
### Rank, roulette and tournament selection function comparison
`Low-Dimensional-Data`![low_dimensional_rank_vs_roulette_vs_tournament_results](example/output/rank_vs_roulette_vs_tournament/low_dimensional/file_2_results.png)
\
In addition to already analysed rank and roulette algorithm we can take a look at tournament selection method. Low size datasets yield very similar results to rank selection. Fitness score is kept on stable and high level throughout the simulation. Again, only roulette selection algorithm acts very different having high variance from the beginning till the end of run.\
`High-Dimensional-Data`
![high_dimensional_rank_vs_roulette_vs_tournament_results](example/output/rank_vs_roulette_vs_tournament/high_dimensional/file_9_results.png)
\
Surprisingly, tournament selection method shows very mediocre results for large scale datasets. Even though improvement was the fastest for first 7 iterations, later on the fintess level of population stabilized without any ground braking improvements. Additionally, fitness score of roulette method noted significant improvement with almost every iteration excluding, whereas rank selection had a hard time for pretty much half of the run only to show the highest improvement in the second half of the simulation.\
