
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(label="Enter your name"),
        gr.Slider(minimum=1, maximum=5, step=1, label="Intensity")
    ],
    outputs=gr.Textbox(label="Output"),
    api_name="predict"
)

demo.launch()




import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
