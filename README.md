# 🎓 Interactive Quiz Application
### A College Project

This is a robust and interactive Quiz Application developed using **Python** and the **Tkinter** GUI framework. This project was designed and implemented as part of our academic curriculum to demonstrate GUI programming, file handling, and real-time logic.

---

## 👥 Project Contributors
This project was collaboratively developed and maintained by:
* 👨‍💻 **Bhaskar Dubey**
* 👩‍💻 **Aastha Agrawal**
* 👨‍💻 **Madhav Gadge**

---

## 📝 Project Overview
The **Interactive Quiz App** is a user-friendly desktop application designed to evaluate a student's knowledge across various categories. It focuses on a seamless user experience, featuring real-time logic and data persistence.

### ✨ Key Features
* **Graphical User Interface (GUI):** Built with the `Tkinter` library for a clean, intuitive, and responsive desktop experience.
* **Dynamic Data Management:** Questions are fetched dynamically from a `JSON` database, allowing for easy updates and scalability without modifying the source code.
* **Timer-Based System:** Includes a real-time countdown for each question to simulate a competitive exam environment.
* **Negative Marking Logic:** Implements an automated scoring system:
    * ✅ **+4 Points** for every correct answer.
    * ❌ **-1 Point** for every incorrect answer.
    * ⚠️ **-1 Point** penalty for Time-Out.
* **Persistent Leaderboard:** Scores are recorded in a local file, ensuring that high scores and rankings are preserved across different sessions.

---

## 🛠️ Tech Stack & Architecture
* **Programming Language:** Python 3.x
* **GUI Framework:** Tkinter (Standard Python Interface)
* **Data Storage:** * `JSON`: Used for structured question-bank management.
* `TXT`: Used for secure leaderboard logging and data persistence.

---

## 📂 Project Structure
* `main.py` – Contains the core logic, GUI architecture, and event handling.
* `questions.json` – A structured database containing categorized MCQs, options, and correct answer keys.
* `leaderboard.txt` – A data file used to store and retrieve user performance records.

---

## 🚀 Installation & Execution

Follow these steps to set up and run the application on your local machine:
