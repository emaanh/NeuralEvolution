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

## Usage
###Training Mode
```bash
# Running with specified total_variations and runs
python3 main.py total_variations=100 runs=50

# Running with custom board size and specified total_variations and runs
python3 main.py height=10 width=10 total_variations=50 runs=20
```

###Testing Mode
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
