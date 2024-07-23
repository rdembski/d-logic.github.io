import gradio as gr
from image_generator import image_generator_demo2
from image_analyzer import image_analyzer_demo
from pdf_chatbot import pdf_chatbot_demo
from smart_search import smart_search_demo
from remove_background import remove_background_demo
from magic_eraser import magic_eraser_demo
from img_prompts import img_prompts_demo

# Original content
content = {
    "en": """
![logo](https://huggingface.co/spaces/rafaldembski/D-LOGIC_beta/resolve/main/logodlogic.png)

# Welcome to D-LOGIC - Intelligent Assistant

D-LOGIC is a state-of-the-art, multi-functional application designed to enhance your daily life through the integration of various language models. Created by hobbyist and artificial intelligence enthusiast Rafał Dembski, this research project aims to bring innovative solutions and cutting-edge AI functionalities right to your fingertips.

## 📖 About the Project  
D-LOGIC is a versatile tool built to provide a wide range of functionalities, leveraging the power of advanced machine learning and natural language processing technologies. Currently in its development phase, this application is a testament to the passion and dedication of its creator, Rafał Dembski.

### Key Features:
- 🤖 **Chat Bot**: An intelligent assistant ready to help with your queries.
- 🔍 **Smart Search**: A powerful search tool to find information quickly and efficiently.
- 🖼️ **Image Tools**: Comprehensive tools for image generation, background removal, and more.
- 📄 **Document Tools**: Tools designed to handle PDFs and other documents seamlessly.

### Supported Languages:
- 🇺🇸 English
- 🇵🇱 Polish (Polski)
- 🇩🇪 German (Deutsch)

## 📚 Learn More
- 📘 **Tutorials**: Find detailed guides and tutorials to help you get the most out of D-LOGIC. [Read more...](#about#tutorials)
- ❓ **FAQ**: Frequently Asked Questions to address common queries and issues. [Read more...](#about#faq)
- 👤 **About Me**: Learn more about the creator of D-LOGIC, Rafał Dembski, his journey, and his passion for programming and AI. [Read more...](#about#about-me)
- 📞 **Contact**: Get in touch with the team behind D-LOGIC for any queries or support. [Read more...](#about#contact)
- 📜 **Documentation**: Detailed documentation about the functionalities and usage of D-LOGIC. [Read more...](#about#documentation)

<span style="color: red; font-weight: bold;">As this project is still evolving, feedback and suggestions are highly appreciated. Join us on this journey of innovation and discovery.</span>
    """,
    "pl": """
![logo](https://huggingface.co/spaces/rafaldembski/D-LOGIC_beta/resolve/main/logodlogic.png)

# Witamy w D-LOGIC - Inteligentny Asystent

D-LOGIC to zaawansowana, wielofunkcyjna aplikacja zaprojektowana, aby ułatwić codzienne życie dzięki integracji różnych modeli językowych. Stworzona przez hobbystę i entuzjastę sztucznej inteligencji Rafała Dembskiego, ten projekt badawczy ma na celu dostarczenie innowacyjnych rozwiązań i najnowszych funkcji AI na wyciągnięcie ręki.

## 📖 O Projekcie  
D-LOGIC to wszechstronne narzędzie zbudowane, aby zapewnić szeroki wachlarz funkcjonalności, wykorzystując moc zaawansowanego uczenia maszynowego i technologii przetwarzania języka naturalnego. Obecnie w fazie rozwoju, ta aplikacja jest świadectwem pasji i poświęcenia jej twórcy, Rafała Dembskiego.

### Kluczowe funkcje:
- 🤖 **Chat Bot**: Inteligentny asystent gotowy do pomocy w zapytaniach.
- 🔍 **Smart Search**: Potężne narzędzie do wyszukiwania informacji szybko i efektywnie.
- 🖼️ **Image Tools**: Kompleksowe narzędzia do generowania obrazów, usuwania tła i innych.
- 📄 **Document Tools**: Narzędzia zaprojektowane do obsługi PDF-ów i innych dokumentów bezproblemowo.

### Obsługiwane języki:
- 🇺🇸 English
- 🇵🇱 Polish (Polski)
- 🇩🇪 German (Deutsch)

## 📚 Dowiedz się więcej
- 📘 **Tutoriale**: Znajdź szczegółowe przewodniki i samouczki, aby w pełni wykorzystać możliwości D-LOGIC. [Czytaj więcej...](#about#tutorials)
- ❓ **FAQ**: Najczęściej zadawane pytania, aby odpowiedzieć na typowe wątpliwości i problemy. [Czytaj więcej...](#about#faq)
- 👤 **O mnie**: Dowiedz się więcej o twórcy D-LOGIC, Rafale Dembskim, jego drodze i pasji do programowania i AI. [Czytaj więcej...](#about#about-me)
- 📞 **Kontakt**: Skontaktuj się z zespołem stojącym za D-LOGIC w przypadku jakichkolwiek pytań lub wsparcia. [Czytaj więcej...](#about#contact)
- 📜 **Dokumentacja**: Szczegółowa dokumentacja dotycząca funkcjonalności i użycia D-LOGIC. [Czytaj więcej...](#about#documentation)

<span style="color: red; font-weight: bold;">Ponieważ ten projekt wciąż się rozwija, opinie i sugestie są bardzo mile widziane. Dołącz do nas w tej podróży innowacji i odkryć.</span>
    """,
    "de": """
![logo](https://huggingface.co/spaces/rafaldembski/D-LOGIC_beta/resolve/main/logodlogic.png)

# Willkommen bei D-LOGIC - Intelligenter Assistent

D-LOGIC ist eine hochmoderne, multifunktionale Anwendung, die entwickelt wurde, um Ihr tägliches Leben durch die Integration verschiedener Sprachmodelle zu verbessern. Erstellt von dem Hobbyisten und KI-Enthusiasten Rafał Dembski, zielt dieses Forschungsprojekt darauf ab, innovative Lösungen und modernste KI-Funktionalitäten direkt an Ihre Fingerspitzen zu bringen.

## 📖 Über das Projekt  
D-LOGIC ist ein vielseitiges Werkzeug, das entwickelt wurde, um eine breite Palette von Funktionen bereitzustellen, indem die Leistung fortschrittlicher maschineller Lern- und Sprachverarbeitungstechnologien genutzt wird. Derzeit in der Entwicklungsphase ist diese Anwendung ein Zeugnis für die Leidenschaft und das Engagement ihres Schöpfers, Rafał Dembski.

### Hauptmerkmale:
- 🤖 **Chat Bot**: Ein intelligenter Assistent, der bereit ist, bei Ihren Anfragen zu helfen.
- 🔍 **Smart Search**: Ein leistungsstarkes Suchwerkzeug, um Informationen schnell und effizient zu finden.
- 🖼️ **Bildwerkzeuge**: Umfassende Werkzeuge zur Bildgenerierung, Hintergrundentfernung und mehr.
- 📄 **Dokumentenwerkzeuge**: Werkzeuge, die entwickelt wurden, um PDFs und andere Dokumente nahtlos zu bearbeiten.

### Unterstützte Sprachen:
- 🇺🇸 English
- 🇵🇱 Polish (Polski)
- 🇩🇪 German (Deutsch)

## 📚 Erfahren Sie mehr
- 📘 **Tutorials**: Finden Sie detaillierte Anleitungen und Tutorials, um das Beste aus D-LOGIC herauszuholen. [Mehr lesen...](#about#tutorials)
- ❓ **FAQ**: Häufig gestellte Fragen, um häufige Anfragen und Probleme zu klären. [Mehr lesen...](#about#faq)
- 👤 **Über mich**: Erfahren Sie mehr über den Schöpfer von D-LOGIC, Rafał Dembski, seinen Werdegang und seine Leidenschaft für Programmierung und KI. [Mehr lesen...](#about#about-me)
- 📞 **Kontakt**: Kontaktieren Sie das Team hinter D-LOGIC bei Fragen oder Unterstützung. [Mehr lesen...](#about#contact)
- 📜 **Dokumentation**: Detaillierte Dokumentation über die Funktionen und die Nutzung von D-LOGIC. [Mehr lesen...](#about#documentation)

<span style="color: red; font-weight: bold;">Da sich dieses Projekt noch in der Entwicklung befindet, werden Feedback und Vorschläge sehr geschätzt. Begleiten Sie uns auf dieser Reise der Innovation und Entdeckung.</span>
    """
}

# Function to update home content based on selected language
def update_home_content(lang):
    return content[lang]

def build_demo():
    with gr.Blocks() as demo:
        gr.HTML("""
            <style>
                body {
                    background-color: #000000;
                    color: #ffffff;
                    margin: 0;
                    padding: 0;
                    height: 100vh;
                    overflow: hidden;
                }
                .gradio-container {
                    background-color: #000000;
                    color: #ffffff;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between; /* Ensure content is spread out with space between */
                }
                .header {
                    flex-shrink: 0;
                }
                .iframe-container {
                    width: 100%;
                    height: 100%;
                    border: none;
                    flex-grow: 1;
                }
                .tab-content {
                    height: 100%;
                    overflow: auto;
                    flex-grow: 1; /* Ensure tab-content takes up available space */
                }
                footer {
                    flex-shrink: 0;
                    padding: 10px 0;
                    text-align: center;
                }
            </style>
        """)

        lang_choice = gr.Dropdown(label="Choose Language", choices=[
            ("🇺🇸 English", "en"),
            ("🇵🇱 Polish (Polski)", "pl"),
            ("🇩🇪 German (Deutsch)", "de"),
        ], value="en")

        with gr.Tabs() as main_tabs:
            with gr.Tab("🏠 Home"):
                home_content = gr.Markdown(content["en"])

            with gr.Tab("🤖 Chat Bot"):
                gr.Markdown("## D-LOGIC - Intelligent Assistant")
                gr.HTML("""
                    <iframe src="https://hf.co/chat/assistant/662961816a8a9e052973f42d" width="100%" height="600"></iframe>
                """)

            with gr.Tab("🔍 Smart Search"):
                smart_search_demo()

            with gr.Tab("🖼️ Image Tools"):
                with gr.Tabs() as image_tools_tabs:
                    with gr.Tab("🖼️ Image Generator"):
                        image_generator_demo2()
                    with gr.Tab("🗑️ Remove Background"):
                        remove_background_demo()
                    with gr.Tab("🖍️ Magic Eraser"):
                        magic_eraser_demo()
                    with gr.Tab("✨ Image Prompts Collection"):
                        img_prompts_demo()

            with gr.Tab("🛠️ Tools"):
                with gr.Tabs() as tools_tabs:
                    with gr.Tab("👁️ Image Analyzer"):
                        image_analyzer_demo()
                    with gr.Tab("📄 PDF ChatBot"):
                        pdf_chatbot_demo()

            with gr.Tab("📚 About"):
                with gr.Tabs() as about_tabs:
                    with gr.Tab("📘 Tutorials"):
                        gr.Markdown("""
                            **Tutorials**
                            Find detailed guides and tutorials to help you get the most out of D-LOGIC.
                            [Read more...](#about#tutorials)
                        """)
                    with gr.Tab("❓ FAQ"):
                        gr.Markdown("""
                            **FAQ**
                            Frequently Asked Questions to address common queries and issues.
                            [Read more...](#about#faq)
                        """)
                    with gr.Tab("👤 About Me"):
                        gr.Markdown("""
                            **About Me**
                            Learn more about the creator of D-LOGIC, Rafał Dembski, his journey, and his passion for programming and AI.
                            [Read more...](#about#about-me)
                        """)
                    with gr.Tab("📞 Contact"):
                        gr.Markdown("""
                            **Contact**
                            Get in touch with the team behind D-LOGIC for any queries or support.
                            [Read more...](#about#contact)
                        """)
                    with gr.Tab("📜 Documentation"):
                        gr.Markdown("""
                            **Documentation**
                            Detailed documentation about the functionalities and usage of D-LOGIC.
                            [Read more...](#about#documentation)
                        """)

        lang_choice.change(
            fn=update_home_content,
            inputs=lang_choice,
            outputs=home_content
        )

        footer = gr.HTML("""
            <footer>
                <p>&copy; 2024 D-LOGIC. All rights reserved. Created by Rafał Dembski. This is a research project.</p>
                <p>Use via API 🔧  ·  utworzone z gradio 🧡</p>
            </footer>
        """)

    return demo

if __name__ == "__main__":
    demo = build_demo()
    demo.launch()
    