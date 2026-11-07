

import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import  Button
from kivy.uix.progressbar import ProgressBar


class MindlyApp(App):

    def build(self):

        # Main screen
        self.root_layout = FloatLayout()

        # Find background image
        bg_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "bg",
            "mindly_bg1.png"
        )

        print("Background path:", bg_path)
        print("Image exists:", os.path.isfile(bg_path))

        # Check image file
        if not os.path.isfile(bg_path):
            raise FileNotFoundError(
                f"Background image not found: {bg_path}"
            )

        # Background image widget
        self.bg_image = Image(
            source=bg_path,
            fit_mode="fill",
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )

        # Add background first
        self.root_layout.add_widget(self.bg_image)

        # App content
        self.layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15,
            size_hint=(1, 1)
        )

        self.root_layout.add_widget(self.layout)



        # Questions
        self.questions = [
            "How often have you felt nervous or anxious?",
            "How often have you found it difficult to stop worrying?",
            "How often have you had trouble relaxing?",
            "How often have you felt restless?",
            "How often have you worried that something bad might happen?"
        ]

        # Answers
        self.answers = [
            ("Not at all", 0),
            ("Several days", 1),
            ("More than half the days", 2),
            ("Nearly every day", 3)
        ]

        self.current_question = 0
        self.total_score = 0

        self.show_home()

        return self.root_layout

    # Home screen
    def show_home(self):

        self.layout.clear_widgets()

        title = Label(
            text="Welcome to MindlyApp",
            font_size=80,
            bold=True,
            color=(0.1, 0.1, 0.2, 1)
        )

        description = Label(
            text="Take a moment to understand your feelings.",
            font_size=38,
            color=(0.1, 0.1, 0.2, 1)
        )

        start_button = Button(
            text="Start Assessment",
            font_size=60,
            size_hint_y=round(0.2),
            height=80
        )

        start_button.bind(on_press=self.start_assessment)

        self.layout.add_widget(title)
        self.layout.add_widget(description)
        self.layout.add_widget(start_button)

    # Start assessment
    def start_assessment(self, instance):

        self.current_question = 0
        self.total_score = 0

        self.show_question()

    # Display questions
    def show_question(self):

        self.layout.clear_widgets()

        progress = ProgressBar(
            max=len(self.questions),
            value=self.current_question,
            size_hint_y=None,
            height=20
        )

        self.layout.add_widget(progress)

        progress_text = Label(
            text=f"Completed: {self.current_question} / {len(self.questions)}",
            font_size=36,
            color=(0.1, 0.1, 0.2, 1)
        )

        self.layout.add_widget(progress_text)

        question_number = Label(
            text=f"Question {self.current_question + 1} of {len(self.questions)}",
            font_size=38,
            color=(0.1, 0.1, 0.2, 1)
        )

        question = Label(
            text=self.questions[self.current_question],
            font_size=40,
            color=(0.1, 0.1, 0.2, 1)
        )

        self.layout.add_widget(question_number)
        self.layout.add_widget(question)

        for answer_text, score in self.answers:

            answer_button = Button(
                text=answer_text,
                font_size=40,
                size_hint_y=None,
                height=50
            )

            answer_button.bind(
                on_press=lambda instance, value=score:
                self.select_answer(value)
            )

            self.layout.add_widget(answer_button)

    # Select answer
    def select_answer(self, score):

        self.total_score += score
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    # Display result
    def show_result(self):

        self.layout.clear_widgets()

        title = Label(
            text="Your Assessment is Complete!",
            font_size=24,
            bold=True,
            color=(0.1, 0.1, 0.2, 1)
        )

        result = Label(
            text=f"Your total score is: {self.total_score} / 15",
            font_size=22,
            color=(0.1, 0.1, 0.2, 1)
        )

        suggestion = Label(
            text="Take a few moments to relax.\n"
                 "Try deep breathing or a short walk.\n"
                 "go for a short nap.\n"
                 "listen to your favorite music.\n"
                 "Talk to someone you trust if you need support.",
            font_size=50,
            color=(0.2, 0.1, 0.2 , 0.8)
        )

        restart_button = Button(
            text="Start Again",
            font_size=30,
            size_hint_y=None,
            height=60
        )

        restart_button.bind(on_press=self.start_again)

        self.layout.add_widget(title)
        self.layout.add_widget(result)
        self.layout.add_widget(suggestion)
        self.layout.add_widget(restart_button)

    # Restart assessment
    def start_again(self, instance):

        self.current_question = 0
        self.total_score = 0

        self.show_home()


if __name__ == "__main__":
    MindlyApp().run()
