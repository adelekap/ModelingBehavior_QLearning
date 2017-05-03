# Modeling Animal Behavior using Q-Learning
This codebase includes a description of a common spatial alternation task (Frank et al., 2000) used to test memory in animals as a Markov Decision Process (MDP). The agent can learn the reward function, given some experience, and choose the best policy in order to learn the task. In order to change the performance of the agent, several parameters can be modified: alpha (learning rate), gamma (discount), and epsilon (exploration probability). The user can run the algorithm using the default parameters, provide constants for the parameters, or use the implemented parameter functions.

### Getting Started

Modeling Animal Behavior using Q-Learning requires a few dependencies:

```
python 2
numpy
matplotlib
```

### Running the Algorithm
Two example rat datasets are provided as txt files. There are both response files (positions that the animal visited on the maze) and decision files (indicating whether the animal made the correct or incorrect decision at that moment).

To run the q-learning algorithm, just run:  `python qLearning.py`

### Parameter Options

![alt tag](https://github.com/adelekap/ModelingBehavior_QLearning/blob/master/Untitled.jpg)

## License

This project is licensed under the MIT License 

This project was written as part of the requirements to complete University of Arizona's INFO550 Artificial Intelligence course.
Some of the functions/classes included in this project are modified versions from class homework files: http://w3.sista.arizona.edu/~clayton/courses/ai/projects/reinforcement/reinforcement.html
