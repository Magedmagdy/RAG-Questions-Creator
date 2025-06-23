import streamlit as st
from src.helper import (
    get_pdf_text, 
    get_text_chunks, 
    get_vector_store, 
    user_query,
    save_text_to_pdf
)

def main():
    st.set_page_config(page_title="AI Exam Generator System", page_icon="💬")
    
    # Session state
    if "history" not in st.session_state:
        st.session_state.history = []
    if "response" not in st.session_state:
        st.session_state.response = ""
    if "response_no_answers" not in st.session_state:
        st.session_state.response_no_answers = ""

    st.header("AI Exam Questions Generator🧾")
    st.caption("Hi, I'm Your AI Agent. I will help you to prepare for your exam..☺")

    # Sidebar with logo and file upload
    with st.sidebar:
        st.image("RAG-Questions-Creator-main/Images/logo.png", width=350)



        doc_files = st.file_uploader(label="Upload your PDF files", accept_multiple_files=True)
        if st.button("Process"):
            if doc_files is not None:
                with st.spinner("Processing...."):
                    raw_text = get_pdf_text(doc_files)
                    if not raw_text.strip():
                        st.error("❌ Couldn't extract any text from the PDF. Please upload a suitable one.")
                    else:
                        text_chunks = get_text_chunks(raw_text)
                        if not text_chunks:
                            st.error("❌ Failed to split text into chunks.")
                        else:
                            get_vector_store(text_chunks)
                            st.success("✅ Done.")
        
        st.markdown("---")
        st.markdown(
            """
            <div style='text-align: center; font-size: 14px;'>
                Created by <strong>Eng.Maged Magdy</strong>  
                <br>
                <a href="https://www.linkedin.com/in/maged-magdy-48515a11a/" target="_blank">
                    🔗 LinkedIn Profile
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Input fields for generating questions
    Exam_name = st.text_input("Enter Exam Name")
    question = st.text_input("What do you want me to do?")
    num_questions = st.number_input("Choose the number of questions", min_value=10, max_value=100)
    difficulty_level = st.selectbox("Difficulty Level", options=["easy", "medium", "hard"])
    question_types = st.selectbox("Questions Type", options=["multiple choice", "true/false", "short answer", "essay"])

    # ======== Generate Questions WITHOUT Answers ========
    if st.button("Generate Questions Only (No Answers)"):
        with st.spinner("Generating questions without answers..."):
            response_no_answers = user_query(
                question=question,
                num_questions=num_questions,
                difficulty_level=difficulty_level,
                question_types=question_types,
                include_answers="No"
            )
            st.session_state.response_no_answers = response_no_answers

    if st.session_state.response_no_answers:
        st.subheader("Generated Questions (No Answers):")
        st.write(st.session_state.response_no_answers)

        file_name_no_answers = st.text_input("**File name for version WITHOUT answers (e.g., questions_only.pdf)**", value="questions_only.pdf")

        if st.button("Save To PDF (No Answers)"):
            if file_name_no_answers:
                file_path_no_answers = save_text_to_pdf(st.session_state.response_no_answers, filename=file_name_no_answers,Exam_name=Exam_name)
                st.success("✅ PDF (no answers) saved successfully!")

                with open(file_path_no_answers, "rb") as pdf_file:
                    st.download_button(
                        label="Download PDF (No Answers)",
                        data=pdf_file,
                        file_name=file_name_no_answers,
                        mime="application/pdf"
                    )
            else:
                st.warning("⚠️ Please write a file name for the version without answers.")

    # ======== Generate Questions WITH Answers ========
    if st.button("Generate Questions (With Answers)"):
        with st.spinner("Generating questions with answers..."):
            response = user_query(
                question=question,
                num_questions=num_questions,
                difficulty_level=difficulty_level,
                question_types=question_types,
                include_answers="Yes"
            )
            st.session_state.response = response

    if st.session_state.response:
        st.subheader("Generated Questions (With Answers):")
        st.write(st.session_state.response)

        file_name = st.text_input("**File name for version WITH answers (e.g., questions_with_answers.pdf)**", value="questions_with_answers.pdf")

        if st.button("Save To PDF (With Answers)"):
            if file_name:  
                file_path = save_text_to_pdf(st.session_state.response, filename=file_name,Exam_name=Exam_name)
                st.success("✅ PDF (with answers) saved successfully!")

                with open(file_path, "rb") as pdf_file:
                    st.download_button(
                        label="Download PDF (With Answers)",
                        data=pdf_file,
                        file_name=file_name,
                        mime="application/pdf"
                    )
            else:
                st.warning("⚠️ Please write a file name for the version with answers.")

if __name__ == "__main__":
    main()
