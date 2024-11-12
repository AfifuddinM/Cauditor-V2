from langchain_community.llms import Ollama 
import streamlit as st
import ollama
llm = Ollama(model="cauditor")

st.title("Chatbot using Llama3")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write_stream(llm.stream(prompt, stop=['<|eot_id|>']))


    # with open(link,'rb') as file:
    #     content = file.read()

    prompts = f'Review this code, Rate the code "bad","mediocre","decent","good" alert any security vulnerabilities first such as sql injection and risks of attacks, provide suggestions for improvement, coding best practices, improve readability, and maintainability. Provide code examples for your suggestion." {content}'

    response = ollama.generate(model='codellama:7b',prompt=prompts)
    aResponse = response['response']

    # file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')

    # with open(file_path, 'w') as file:
    #     file.write(f"Response: {aResponse}\n\n")
    #     print(f"Response saved to {file_path}")
    
    with open(link,'rb') as file:
    content = file.read()
    prompts = f'Review this code, Rate the code "bad","mediocre","decent","good" alert any security vulnerabilities first such as sql injection and risks of attacks, provide suggestions for improvement, coding best practices, improve readability, and maintainability. Provide code examples for your suggestion."'
    response = ollama.generate(model='codellama:7b',prompt=prompts)
    aResponse = response['response']
    print('response')
