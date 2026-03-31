# Digital Voting System with AI Prediction Engine

A Python-based terminal application designed to simulate a secure digital voting environment. This project features user registration, duplicate vote prevention, and a mock **AI Prediction Engine** that analyzes real-time voting trends to forecast a winner.

---

## 🚀 Features

* **Voter Registration:** Allows users to create unique Voter IDs and secure passwords.
* **Secure Authentication:** Validates credentials before allowing a vote to be cast.
* **Integrity Check:** Prevents double-voting by tracking Voter IDs in a session-based blacklist.
* **AI Prediction Engine:** Simulates trend analysis using probability distributions to predict the outcome based on current data.
* **Real-time Results:** Displays the final tally and vote counts upon system shutdown.

---

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **Libraries:** * `time`: Used for simulating data processing delays.
    * `random`: Integrated for logic expansion and trend simulation.

---

## ⚙️ How to Run

1.  **Clone the repository:**
    
    git clone [https://github.com/vikrantbarnwal2008-tech/Fundamentals-of-AI-and-ML-Evaluated-Course-Project/blob/main/online_voting_system.py](https://github.com/vikrantbarnwal2008-tech/Fundamentals-of-AI-and-ML-Evaluated-Course-Project/blob/main/online_voting_system.py)

2.  **Navigate to the directory:**

    cd digital-voting-system

3.  **Run the application:**

    python voting_system.py

## 🤖 AI Logic & Mathematics

The **AI Prediction Engine** inside this script serves as a conceptual introduction to **Trend Analysis**. 

It calculates the probability of a win for each candidate based on the current sample size. The prediction is determined by the highest probability:

$$P(c) = \left( \frac{V_c}{V_{total}} \right) \times 100$$

Where:
* $P(c)$ is the probability of the candidate winning.
* $V_c$ is the number of votes for that specific candidate.
* $V_{total}$ is the total number of votes cast.

The engine requires a minimum of **3 votes** to ensure a baseline of data before generating a confidence level.

---

## 📝 Roadmap & Future Improvements

- [ ] **Security:** Implement `hashlib` to store passwords as secure hashes rather than plain text.
- [ ] **Data Persistence:** Integrate a JSON or SQL database to save voter records and results between sessions.
- [ ] **GUI:** Develop a graphical user interface using `Tkinter` or `CustomTkinter`.
- [ ] **Complex Modeling:** Use `scikit-learn` to implement actual machine learning models for demographic-based forecasting.

---

