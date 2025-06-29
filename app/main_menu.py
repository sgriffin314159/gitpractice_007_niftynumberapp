import gradio as gr
#from app.number_guessing_game import number_game_ui
from app.number_of_the_day import get_number_of_day_ui
#from app.number_facts import number_facts_ui

def launch_app():
    def handle_selection(choice):
        if choice == "Play Number Guessing Game":
            return number_game_ui()
        elif choice == "Get Number of the Day":
            return get_number_of_day_ui()
        elif choice == "Get Number Facts":
            return number_facts_ui()
        else:
            return gr.update(visible=True)

    with gr.Blocks() as demo:
        gr.Markdown("## Welcome to the Number Fun App")
        with gr.Row():
            menu = gr.Radio(
                [
                    "Play Number Guessing Game",
                    "Get Number of the Day",
                    "Get Number Facts",
                    "Reset to Main Menu"
                ],
                label="Select an option",
            )
        output = gr.Column()

        menu.change(fn=handle_selection, inputs=menu, outputs=output)

    demo.launch()

