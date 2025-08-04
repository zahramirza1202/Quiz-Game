import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "What type is input() by default?",
        "options": ["int", "str", "bool", "float"],
        "answer": "str"
    },
    {
        "question": "Which one is a list in Python?",
        "options": ["{1,2,3}", "(1,2,3)", "[1,2,3]", "<1,2,3>"],
        "answer": "[1,2,3]"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💡 Interactive Python Quiz")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e2f")  # Dark background

        self.q_no = 0
        self.score = 0

        self.card = tk.Frame(root, bg="#2a2a40", bd=0, relief="flat")
        self.card.pack(pady=40, padx=30, fill="both", expand=True)

        self.question_label = tk.Label(
            self.card, text="", font=("Segoe UI", 18, "bold"),
            wraplength=600, justify="left", bg="#2a2a40", fg="#ffffff"
        )
        self.question_label.pack(pady=(30, 20), anchor="w")

        self.var = tk.StringVar()
        self.options = []
        for _ in range(4):
            btn = tk.Radiobutton(
                self.card, text="", variable=self.var,
                font=("Segoe UI", 14), value="", anchor='w',
                bg="#2a2a40", fg="#dddddd", activebackground="#2a2a40",
                activeforeground="#00d4ff", selectcolor="#444466", padx=15
            )
            btn.pack(fill="x", padx=20, pady=5)
            self.options.append(btn)

        self.next_button = tk.Button(
            root, text="Next ➡", command=self.next_question,
            font=("Segoe UI", 13, "bold"), bg="#00d4ff", fg="#1e1e2f",
            activebackground="#0099cc", activeforeground="#ffffff",
            relief="flat", padx=20, pady=10, bd=0
        )
        self.next_button.pack(pady=20)

        self.root.bind("<Enter>", self.add_hover)
        self.root.bind("<Leave>", self.remove_hover)

        self.load_question()

    def add_hover(self, e):
        self.next_button.config(bg="#33e0ff")

    def remove_hover(self, e):
        self.next_button.config(bg="#00d4ff")

    def load_question(self):
        self.var.set(None)
        q = questions[self.q_no]
        self.question_label.config(text=f"Q{self.q_no+1}: {q['question']}")
        for i, option in enumerate(q["options"]):
            self.options[i].config(text=option, value=option)

    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Oops!", "❗ Please select an answer.")
            return
        correct = questions[self.q_no]['answer']
        if selected == correct:
            self.score += 1
        self.q_no += 1
        if self.q_no < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        result_color = "#00ff99" if self.score >= 3 else "#ff5e5e"

        tk.Label(
            self.root, text="🏁 Quiz Completed!", font=("Segoe UI", 26, "bold"),
            fg="#ffffff", bg="#1e1e2f"
        ).pack(pady=40)

        tk.Label(
            self.root, text=f"🎉 You scored {self.score} out of {len(questions)}!",
            font=("Segoe UI", 20), fg=result_color, bg="#1e1e2f"
        ).pack(pady=20)

        tk.Button(
            self.root, text="Exit 🚪", command=self.root.quit,
            font=("Segoe UI", 13, "bold"), bg="#ff4d4d", fg="white",
            activebackground="#cc0000", padx=20, pady=10, relief="flat"
        ).pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()