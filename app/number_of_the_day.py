# Menu option 2 - Learn about the Number of the Day
# Utilizes API at https://math.tools/numbers/number-of-the-day/

import requests
import gradio as gr

def get_number_of_day():
    response = requests.get("http://math.tools/api/numbers/nod?json")
    if response.status_code == 200:
        return response.json().get("contents", "No data available.")
    return "API Get Request failed to retrieve the number of the day."

def get_number_of_day_ui():
    with gr.Blocks() as ui:
        gr.Markdown("### Number of the Day ")
        output = gr.Textbox(label="Did you know?", value=get_number_of_day(), interactive=False)
        gr.Button("Return to Main Menu")
    return ui
