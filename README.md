# Merger

### Description:

The merge.py script is a versatile tool designed to merge either text data or files using a specified symbol. It offers flexibility in merging text or file content seamlessly. This script is particularly useful when you need to combine different sets of data, such as logs, CSV files, or any textual information, into a unified format.

### Features:
- Merges text or files seamlessly.
- Allows customization of the merging symbol.
- Handles both text and file inputs intelligently.
- Simple and easy-to-use command-line interface.

### User Guide:

1. Installation:
- Ensure you have Python installed on your system.
- Run:
  ```bash
  apt update -y && apt upgrade -y 
  ```
  ```bash
  git clone https://github.com/Cyber-Programer/Merger.git
  ```
  ```bash
  cd Merger
  ```
2. setup:
    ```bash
    pip install .
    ```
- if the code exicute proparly then, Typing merge in the terminal from anywhere in your system to starts the script.
- also you can use this script as a normal script
   - Open your terminal or command prompt.
   - Navigate to the directory containing the merge.py script.
   - then run the `marge.py` file with python
      ```bash
          python merge.py
      ```

### Commands:

- Get Help:
    ```bash
        python merge.py --help
    ```
    ```bash
        merge --help
    ```
    Displays the help message, providing information on how to use the script along with examples.

- Merge Files:
    ```bash
        python merge.py -f file1.txt file2.txt
    ```
     ```bash
        merge -f file1.txt file2.txt
    ```
  Merges the content of file1.txt and file2.txt, displaying the merged output with a default symbol ( : ) .

- Merge Texts:
    ```bash
        python merge.py -t text1,text2 text1,text2
    ```
    ```bash
        merge -t text1,text2 text1,text2
    ```
    Merges the provided text strings (text1 and text2) with a default symbol ( : ).

- Custom Symbol:
    ```bash
        python merge.py -f file1 file2 -sy :
    ```

    ```bash
        merge -f file1 file2 -sy :
    ```
    Merges files file1 and file2, using the specified custom symbol :.


### Note: You can use either -f or -t options but not both at the same time.

3. Examples:
  - Merge two files data1.txt and data2.txt using the default symbol :.

     ```bash
        python merge.py -f data1.txt data2.txt  
     ```
  - Merge two text strings "Hello" and "World" with a custom symbol ~.
    ```bash
        python merge.py -t Hello,World Hello,World -sy ~
    ```
    Enjoy exploring the capabilities of this tool!

4. Save Output In file:
  - use `-o` to saved output in any file
      ```bash
      python merge.py -f x.txt y.txt -o output.txt
      ```
      ```bash
      merge.py -f x.txt y.txt -o output.txt
      ```

     
