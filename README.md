<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
# data_py
 
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
# data_cook

data_cook is a library that helps you accelerate the data preprocessing process efficiently and easily. The library provides powerful tools for manipulating, cleaning, and normalizing data, saving time and improving workflow efficiency.

## Key Features
- Supports CSV & DataFrame processing
- Smart merging (merge) methods
- Image and video preprocessing (frame extraction, brightness adjustment, flipping, etc.)
- Extract frames based on keyframes or significant changes
- Built-in powerful data filtering tools
- Highly compatible with Pandas & OpenCV

## Installation
You can install **data_cook** via pip:
```sh
pip install data_cook
```
To install the latest development version from GitHub:
```sh
git clone https://github.com/AutoCookies/data_cook.git
cd data_cook
pip install .
```

## Usage
Here is a simple example of how to use **data_cook**:
```python
import data_cook
from data_cook.csv import group_and_merge

# Example usage
import pandas as pd

data = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B'],
    'value': [10, 20, 30, 40]
})

result = group_and_merge(data, 'group', 'value')
print(result)
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License
<<<<<<< Updated upstream
<<<<<<< Updated upstream
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
>>>>>>> Stashed changes
=======
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
>>>>>>> Stashed changes
=======
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
>>>>>>> Stashed changes
