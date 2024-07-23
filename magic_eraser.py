import gradio as gr

def magic_eraser_demo():
    with gr.Blocks() as demo:
        gr.HTML("""
            <style>
                .iframe-container {
                    width: 100%;
                    height: 100%;
                    overflow: hidden;
                }
                iframe {
                    width: 100%;
                    height: 100%;
                    border: none;
                    display: block;
                    margin: 0 auto;
                }
            </style>
            <div class="iframe-container">
                <iframe
                    src="https://rafaldembski-magic-eraser.hf.space"
                    frameborder="0"
                ></iframe>
            </div>
        """)
    return demo
    