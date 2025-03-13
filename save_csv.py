import os

# CSV content
csv_content = """Subject,Code,Modules
Complex Variables and Linear Algebra,BMAT201L,Module - 1 : Analytic Functions
,,Module - 2 : Conformal and Bilinear transformations
,,Module - 3 : Complex Integration
,,Module - 4 : Vector Spaces
,,Module - 5 : Linear Transformations
,,Module - 6 : Inner Product Spaces
,,Module - 7 : Matrices and System of Equations
Microprocessors and Microcontrollers,BECE204L,Module - 1 : Overview of Microprocessors
,,Module - 2 : Microprocessor Architecture and Interfacing: Intel x86
,,Module - 3 : Microcontroller Architecture: Intel 8051
,,Module - 4 : Microcontroller 8051 Peripherals
,,Module - 5 : I/O interfacing with Microcontroller 8051
,,Module - 6 : ARM Processor Architecture
,,Module - 7 : ARM Instruction Set
Operating Systems,BCSE303L,Module - 1 : Introduction
,,Module - 2 : OS Principles
,,Module - 3 : Scheduling
,,Module - 4 : Concurrency
,,Module - 5 : Memory Management
,,Module - 6 : Virtualization and File System Management
,,"Module - 7 : Storage Management, Protection and Security"
Theory of Computation,BCSE304L,Module - 1 : Introduction to Languages and Grammars
,,Module - 2 : Finite State Automata
,,Module - 3 : Regular Expressions and Languages
,,Module - 4 : Context Free Grammar
,,Module - 5 : Pushdown Automata
,,Module - 6 : Turing Machine
,,Module - 7 : Recursive and Recursively Enumerable Languages
Design and Analysis of Algorithms,BCSE204L,"Module - 1 : Design Paradigms: Greedy, Divide and Conquer Techniques"
,,"Module - 2 : Design Paradigms: Dynamic Programming, Backtracking and Branch & Bound Techniques"
,,Module - 3 : String Matching Algorithms
,,Module - 4 : Graph Algorithms
,,Module - 5 : Geometric Algorithms
,,Module - 6 : Randomized algorithms
,,Module - 7 : Classes of Complexity and Approximation Algorithms
Probability and Statistics,BMAT202L,Module - 1 : Introduction to Statistics
,,Module - 2 : Random variables
,,Module - 3 : Correlation and Regression
,,Module - 4 : Probability Distributions
,,Module - 5 : Hypothesis Testing-I
,,Module - 6 : Hypothesis Testing-II
,,Module - 7 : Reliability
Web Programming,BCSE203E,Module - 1 : Introduction
,,Module - 2 : Hypertext Markup Language
,,Module - 3 : Cascading Style Sheets
,,Module - 4 : JavaScript
,,Module - 5 : Advanced JavaScript
,,Module - 6 : ReactJS
,,Module - 7 : Advanced ReactJS
Computer Networks,BCSE308L,Module - 1 : Networking Principles and Layered Architecture
,,Module - 2 : Circuit and Packet Switching
,,Module - 3 : Data Link Layer
,,Module - 4 : Network Layer
,,Module - 5 : Routing Protocols
,,Module - 6 : Transport Layer
,,Module - 7 : Application layer"""

# Save to file
csv_file_path = 'subjects_modules.csv'
with open(csv_file_path, 'w', encoding='utf-8') as file:
    file.write(csv_content)

print(f"CSV file saved to {os.path.abspath(csv_file_path)}") 