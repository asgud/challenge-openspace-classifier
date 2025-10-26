## 🪑 OpenSpace Organizer

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Welcome to my very first Python project — the OpenSpace Organizer! 🎉

This simple program simulates how people can be randomly assigned to seats at tables inside an open office space.
It was built as part of a learning challenge to practice object-oriented programming (OOP) in Python — using classes, objects, and file handling.


## 💡 Project Overview

The goal of this project is to organize colleagues into random seats across multiple tables in an open workspace.
It’s made up of three main parts:

1. Seat – represents a single seat (free or occupied).
2. Table – contains a set of seats and handles seat assignments.
3. Openspace – manages all the tables and distributes people randomly into available seats.

Each class lives in its own file to keep the project clean and modular.

![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)


## 🧱 Project Structure

challenge-openspace-classifier/
│
├── main.py                  # Main script that runs the program
├── new_colleagues.csv       # Input file with list of colleague names
├── seating_plan.txt         # Output file with the final seating plan
├── dev_notebook.ipynb       # Development/testing notebook used during coding
├── README.md                # Project documentation (this file!)
└── utils/
    ├── __init__.py          # Marks utils as a Python package
    ├── table.py             # Contains Seat and Table classes
    └── openspace.py         # Contains Openspace class and random assignment logic



## 🧠 How It Works

1. The program reads a list of colleagues’ names from a CSV file (colleagues.csv).
2. You define how many tables you want and how many seats per table.
3. Everyone is randomly assigned to available seats.
4. The final seating plan is displayed in the console and saved to seating_plan.txt.


## ⚙️ How to Run


1️⃣. Clone the repository to your local machine.
2️⃣. Make sure your folder has a colleagues.csv file.
3️⃣. Run the program, you can execute the 'main.py' file from command line:

```
   python main.py
```
4️⃣. View the result: The seating plan will print in your terminal and be saved as a text file. 


## ✨ What I Learned

This project taught me how to:

- Use object-oriented programming in Python (classes, objects, methods)
- Keep code modular by splitting it into separate files (table.py, openspace.py, main.py)
- Work with CSV files and text file output
- Use loops, lists, and conditions in a real-world context
- Write clear and reusable code, even as a beginner


## ⏱️ Timeline

This project took two days for completion.


## 🧑‍💻 Author

Astha Gudgilla
🌱 This project was done as part of the AI Boocamp at BeCode.org.
📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/asthagudgilla/).




