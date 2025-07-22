import streamlit as st
import fitz
from PIL import Image
import os
import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM



def load_models():
    st.info("🔁 Loading models (BLIP + T5 QGen)...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    blip = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Use "slow" tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        "mrm8488/t5-base-finetuned-question-generation-ap", use_fast=False
    )
    model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")

    # Create QGen pipeline manually
    qgen = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    return processor, blip, qgen

def extract_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    structured = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        images = []

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            path = f"extracted_images/page{page_num+1}_img{img_index+1}.{ext}"
            with open(path, "wb") as f:
                f.write(image_bytes)
            images.append(path)

        structured.append({
            "page": page_num + 1,
            "text": text.strip(),
            "images": images
        })

    with open("output/structured_output.json", "w") as f:
        json.dump(structured, f, indent=4)

    return structured

def generate_questions(structured, processor, blip, qgen):
    results = []
    for page in structured:
        for image_path in page["images"]:
            img = Image.open(image_path).convert("RGB")
            inputs = processor(img, return_tensors="pt")
            out = blip.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)
            question = qgen(f"generate question: {caption}")[0]['generated_text']

            results.append({
                "image": image_path,
                "caption": caption,
                "question": question
            })

    with open("output/generated_questions.json", "w") as f:
        json.dump(results, f, indent=4)

    return results

# Streamlit App UI
st.title("AI PDF Visual Question Generator")
st.markdown("Upload an educational PDF and generate image-based questions using AI!")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting content..."):
        structured_data = extract_pdf(uploaded_file)
        st.success("PDF content extracted!")

        processor, blip, qgen = load_models()
        with st.spinner(" Generating questions..."):
            question_data = generate_questions(structured_data, processor, blip, qgen)
            st.success("Questions generated!")

        st.subheader("Results")

        for item in question_data:
            st.image(item["image"], width=300)
            st.markdown(f"**Caption:** {item['caption']}")
            st.markdown(f"**Question:** {item['question']}")
            st.markdown("---")

        st.download_button(
            "Download Questions JSON",
            data=json.dumps(question_data, indent=4),
            file_name="generated_questions.json",
            mime="application/json"
        )
