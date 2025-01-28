import tkinter as tk
from tkinter import messagebox
import random

# Predefined questions
questions = [
    {
        "topic": "Loops",
        "question_text": "What type of loop is used to iterate over a sequence (e.g., list, tuple, string) in Python?",
        "options": ["for loop", "while loop", "do-while loop", "repeat loop"],
        "correct_answer": "for loop"
    },
    {
        "topic": "Lists",
        "question_text": "How do you add an element to the end of a list in Python?",
        "options": ["list.add()", "list.append()", "list.insert()", "list.extend()"],
        "correct_answer": "list.append()"
    },
    {
        "topic": "Strings",
        "question_text": "Which method is used to convert a string to uppercase in Python?",
        "options": ["string.upper()", "string.capitalize()", "string.title()", "string.lower()"],
        "correct_answer": "string.upper()"
    },
    {
        "topic": "Functions",
        "question_text": "What keyword is used to define a function in Python?",
        "options": ["def", "func", "function", "define"],
        "correct_answer": "def"
    },
    {
        "topic": "Dictionaries",
        "question_text": "How do you access the value associated with a key in a dictionary?",
        "options": ["dict.key", "dict[key]", "dict.get(key)", "dict.value(key)"],
        "correct_answer": "dict[key]"
    }
]

class PythonQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz App")

        self.topic_label = tk.Label(root, text="Enter Python topic:")
        self.topic_label.pack()

        self.topic_entry = tk.Entry(root)
        self.topic_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Python Question", command=self.generate_question)
        self.generate_button.pack()

        self.display_frame = tk.Frame(root)
        self.display_frame.pack()

        self.topic_display = tk.Label(self.display_frame, text="")
        self.topic_display.pack()

        self.question_display = tk.Label(self.display_frame, text="")
        self.question_display.pack()

        self.code_display = tk.Label(self.display_frame, text="")
        self.code_display.pack()

        self.options_var = tk.StringVar(value=None)
        self.options_frame = tk.Frame(root)
        self.options_frame.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

        self.current_question = None

    def generate_question(self):
        topic = self.topic_entry.get().strip().lower()
        filtered_questions = [q for q in questions if q["topic"].lower() == topic]

        if not filtered_questions:
            messagebox.showinfo("Info", "No questions found for the given topic.")
            return

        self.current_question = random.choice(filtered_questions)

        self.topic_display.config(text=f"Topic: {self.current_question['topic']}")
        self.question_display.config(text=f"Question: {self.current_question['question_text']}")
        self.code_display.config(text="Code: (Not available for this example)")

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for option in self.current_question["options"]:
            rb = tk.Radiobutton(self.options_frame, text=option, variable=self.options_var, value=option)
            rb.pack(anchor=tk.W)

        self.feedback_label.config(text="")

    def check_answer(self):
        if not self.current_question:
            messagebox.showinfo("Info", "Please generate a question first.")
            return

        selected_answer = self.options_var.get()
        if selected_answer == self.current_question["correct_answer"]:
            self.feedback_label.config(text="Correct! Well done!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonQuizApp(root)
    root.mainloop()

