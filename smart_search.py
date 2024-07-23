import gradio as gr

def smart_search_demo():
    with gr.Blocks() as demo:
        gr.HTML("""
            <style>
                .iframe-container {
                    width: 100%;
                    height: 100%;
                    border: none;
                    overflow: hidden;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                iframe {
                    width: 100%;
                    height: 100%;
                    border: none;
                    display: block;
                    background-color: #000000;
                }
                @media (max-width: 768px) {
                    .iframe-container {
                        height: 450px;
                    }
                    iframe {
                        height: 450px;
                    }
                }
            </style>
            <div class="iframe-container">
                <iframe src="https://rafaldembski-smart-search.hf.space" frameborder="0" allowfullscreen></iframe>
            </div>
        """)
    return demo
