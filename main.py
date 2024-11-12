import streamlit as st
import ollama

client = ollama.Client()

def review_code(content):
    prompts = (
        f'Review this code. Rate the code as "bad", "mediocre", "decent", or "good"; alert any security vulnerabilities first such as SQL injection and risks of attacks. '
        f'Provide suggestions for improvement, coding best practices, and improving readability and maintainability. Provide code examples for your suggestion.\n\n{content}'
    )

    response = client.generate(model='codellama:7b', prompt=prompts)
    
    if 'response' in response:
        return response['response']
    else:
        st.error("Unexpected response format from Cauditor")
        st.write(response) 
        return "Review generation failed. Please try again."

st.title("Code Review with Cauditor")

uploaded_file = st.file_uploader("Upload your script file", type=["py", "js", "java", "cpp", "ts", "rb", "php", "html"])
code_input = st.text_area("Or write your code here")

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
else:
    code = code_input

if st.button("Review Code"):
    if code:
        with st.spinner("Cauditor is reviewing your code..."):
            review = review_code(code)
        
        st.subheader("Code Review")
        st.write(review)

        review_bytes = review.encode("utf-8")
        st.download_button(
            label="Download Review as .txt",
            data=review_bytes,
            file_name="code_review.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please enter code or upload a file.")
