# NeuralEvolution V1.0
NeuralEvolution V1.0 simulates the neural evolution of organisms using a genetic algorithm (with one generation) within a grid ecosystem to perform pathfinding to a goal location.

## Installation

Ensure you have Python 3.6 or later installed on your machine. Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/emaanh/NeuralEvolution.git

# Navigate to the project directory
cd NeuralEvolution

# Install dependencies
pip install -r requirements.txt
```

## Configuration Parameters

This section explains the purpose of each command line argument that can be passed to the program. Use these arguments to customize the simulation according to your needs.

- `height`: Specifies the height of the simulation environment (grid). The default value is 10. Represents the number of grid rows.
  
- `width`: Specifies the width of the simulation environment (grid). The default value is 10. Represents the number of grid columns.

- `filename`: In testing mode, this specifies the filename of the weights file to be used. Defaults to ideal weights if not specified.

- `runs`: The number of simulation runs for every variant. The default is 1 for testing mode. This parameter is used for both testing and training modes.

- `total_variations`: Specific to only training mode, this parameter sets the number of variations or mutations to explore during the training process

Each of these parameters tailors the simulation environment and operation mode to specific needs

## Usage
Training Mode
```bash
# Running with specified total_variations and runs
python3 main.py total_variations=100 runs=50

# Running with custom board size and specified total_variations and runs
python3 main.py height=10 width=10 total_variations=50 runs=20
```

Testing Mode
```bash
# Running with ideal weights
python3 main.py

# Running with a specified weights filename for weights
python3 main.py filename=example_data.txt

# Running with a specified weights filename and custom number of runs
python3 main.py filename=example_data.txt runs=10

# Running with custom board size and specified weighs filename and custom number of runs
python3 main.py height=15 width=15 filename=test_data.txt runs=5
```
