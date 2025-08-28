
import streamlit as st
from input_agent import extract_cobol_from_docx
from semantic_agent import convert_to_structured_format
from rule_extractor_agent import extract_business_rules
from validator_agent import validate_rules
from output_agent import write_rules_to_docx

st.title("COBOL Business Rule Extractor")

uploaded_file = st.file_uploader("Upload COBOL DOCX File", type=["docx"])

if uploaded_file:
    with open("temp_input.docx", "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully.")

    cobol_code = extract_cobol_from_docx("temp_input.docx")
    st.subheader("Extracted COBOL Code")
    st.text(cobol_code)

    structured_logic = convert_to_structured_format(cobol_code)
    st.subheader("Structured Logic")
    st.text(structured_logic)

    business_rules = extract_business_rules(structured_logic)
    st.subheader("Extracted Business Rules")
    st.write(business_rules)

    validated_rules = validate_rules(business_rules)
    st.subheader("Validated Rules")
    st.write(validated_rules)

    output_path = "business_rules_output.docx"
    write_rules_to_docx(validated_rules, output_path)

    with open(output_path, "rb") as f:
        st.download_button("Download Business Rules DOCX", f, file_name=output_path)
