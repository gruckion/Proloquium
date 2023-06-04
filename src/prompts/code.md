# Instructions

Generate a Python program for the following task: {task_description}.

Critical rules:

- Code must be declaritive, pythonic, with readable variable names
- Provide a list of depencies that must be installed to run the program
- If any files are created by the program, they must be saved in the `output` directory
- If any files are read by the program, they must be read from the `input` directory
- The response from the program must be saved in the `rsults` directory as `result.*`
- The result must be a suitable format for the task (e.g. a CSV file, a plot, audio / video file, etc.)

For example:

File: `example.py`

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set directory paths
input_path = 'inputs/titanic.csv'
output_dir = 'output/'

# Load Titanic data from CSV
df = pd.read_csv(input_path)

# Group passengers by class and age, and then compute the survival rate
class_age = df.groupby(['pclass','age'])['survived'].mean().reset_index()

# Create two plots: one for first class, and one for second class
for pclass in [1,2]:
    # Subset data
    class_subset = class_age[class_age['pclass']==pclass]

    # Create plot
    plt.plot(class_subset['age'], class_subset['survived'])
    plt.title(f'Titanic Survival Rate: Class {pclass}')
    plt.xlabel('Age')
    plt.ylabel('Survival Rate')
    plt.ylim(0,1)
    plt.grid(True)

    # Save plot
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(output_dir + f'titanic_class_{pclass}_plot.png')
    plt.clf()
```

Dependencies:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
