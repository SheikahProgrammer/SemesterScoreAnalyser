# SemesterScoreAnalyser

SemesterScoreAnalyser is a Python script that helps students analyse their academic performance for a given semester. It reads a CSV file containing the student's grades and generates a report with statistics such as average score, highest score, lowest score, and grade distribution.

## Usage

To use SemesterScoreAnalyser, you must have Python 3 installed on your system. Once you have Python installed, you can run the script by executing the following command in your terminal:

Replace `[csv_file]` with the path to the CSV file containing your grades. The script will generate a report in the terminal.


## Classes

The script includes the following classes:

### `CourseTheory`

Calculates the score, grade, and grade point for a theory course.

#### Arguments

- `code` (string): The course code.
- `cats` (list): A list of integers representing the scores obtained in continuous assessment tests.
- `fat` (int): The score obtained in the final assessment test.
- `ias` (list): A list of integers representing the scores obtained in internal assessment tests.
- `avg` (float): The class average.
- `std` (float): The standard deviation.

#### Methods

- `ShowScore()`: Prints the absolute score and grade point.
- `Save()`: Saves the course score to a CSV file.

### `CourseLab`

Calculates the score for a lab course.

#### Arguments

- `code` (string): The course code.
- `fat` (int): The score obtained in the final assessment test.
- `ias` (list): A list of integers representing the scores obtained in internal assessment tests.

#### Methods

- `ShowScore()`: Prints the score.
- `Save()`: Saves the course score to a CSV file.

### `CourseEmbedded`

Calculates the score for an embedded course.

#### Arguments

- `code` (string): The course code.
- `fat` (int): The score obtained in the final assessment test.
- `pats` (list): A list of integers representing the scores obtained in periodic assessment tests.
- `mat` (int): The score obtained in the midterm assessment test.

#### Methods

- `ShowScore()`: Prints the score.
- `Save()`: Saves the course score to a CSV file.


## Contributing

If you would like to contribute to SemesterScoreAnalyser, feel free to submit a pull request. Please ensure that your code follows PEP 8 guidelines and includes tests.

## License

SemesterScoreAnalyser is licensed under the MIT license. See `LICENSE` for more information.


