import gradio as gr
gr.close_all()

def greet (name):
  return "hello, " + name + "!"

demo = gr.InterFace(
  fn=greet,
  inputs=[gr.textbox(label="Name:")],
  outputs=[gr.textbox()],
)
demo.launch()

import gradio as gr
gr.close_all()

def getDetails(mame, age, preference, hobbies):
return f"Name:(name)\nAge:{age)\nSubject Preference: {preference)\m Hobbies: {[h for h in hobbies]}"

demo = gr.Interface(
fn=getDetails,
inputs = [gr.Textbox(label-"Name: "),
gr.Slider(label="Age: "),
gr.Radio(label="Subject Preference: ", choices-['c', 'c#', 'Java', 'Python"]),
gr.Checkboxgroup(label='Hobbies:', choices=['Painting", 'Singing', 'Reading', "Gaming'])

outputs=[gr.Textbox()]

demo. launch()
