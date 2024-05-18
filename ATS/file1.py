#Poppler Path = C:\Program Files\poppler-24.02.0\Library\bin



# import streamlit as st
# import os
# import io
# from PIL import Image
# import pdf2image
# import google.generativeai as genai
# import base64

# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input,pdf_content,prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input,pdf_content[0],prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         #convert pdf to image
#         images = pdf2image.convert_from_bytes(uploaded_file.read())

#         first_page = images[0]

#         # convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts=[
#             {
#                 "mime_type" : "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
    

# # Streamlit AP

# st.set_page_config(page_title="ATS Resume Expert")
# st.header("ATS Tracking system")
# input_text = st.text_area("Job Description : ",key="input")
# uploaded_file = st.file_uploader("Upload your resume (PDF....)",type = ["pdf"])


# if uploaded_file is not None:
#     st.write("PDF uploaded Succeessfully")

# submit1 = st.button("Tell Me about the Resume") 

# # submit2 = st.button("How can i Improvise my Skills") 

# # submit3 = st.button("What are the key words that are Missing") 

# submit3 = st.button("Percentage Match") 

# input_prompt1 = """
# You are an experienced Human Resource Manager with Tech Experience in the field of Data Science , 
# Full stack Web Development , Big Data Engineering , Devops ,Data Analyst ,
#  your task is to review the provided resume against the job description for these profiles.
# Please share your proffessional evaluation on whether the candidate's profile  align with the role.
#  Highlight the strengths and weakness of the applicant in relation to the specified job requirements 
# """

# # input_prompt2 = """
# # You are an Technical Human Resource Manager with expertise in datascience ,Full stack Web Development ,
# #  Big Data Engineering , Devops ,Data Analyst ,
# # your role is to scruntinize the resume in light of the job descrioption provided.
# # Share your insights on the candidate's suitability for the role from an HR perspective,
# # Additionally , offer advice on enhancing the candidate's  skills and identify areas

# # """

# input_prompt3="""
# You are an skilled ATS(Aplicant Rracking System) scanner with a deep understanding of data science,
#  Full stack Web Development , Big Data Engineering , Devops ,Data Analyst , and deep ATS functlionality,
# your task is to evaluate the resume against the provided job descrioption .
# give me the percentage of match if the resume matches
# job description . First the output should come as percentage and then keywords missing and last final thoughts. 
# """
  
# if submit1:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt1,pdf_content,input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt3,pdf_content,input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")  

# import streamlit as st
# import os
# import io
# from PIL import Image
# import pdf2image
# import google.generativeai as genai
# import base64

# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input, pdf_content[0], prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         # Convert PDF to image
#         images = pdf2image.convert_from_bytes(uploaded_file.read())

#         first_page = images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# # Streamlit App

# st.set_page_config(page_title="ATS Resume Expert")
# st.header("ATS Tracking System")
# input_text = st.text_area("Job Description:", key="input")
# uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])  # Corrected typo here

# if uploaded_file is not None:
#     st.write("PDF uploaded successfully")

# submit1 = st.button("Tell Me about the Resume")
# submit3 = st.button("Percentage Match")

# input_prompt1 = """
# You are an experienced Human Resource Manager with Tech Experience in the field of Data Science, 
# Full stack Web Development, Big Data Engineering, Devops, Data Analyst,
# your task is to review the provided resume against the job description for these profiles.
# Please share your professional evaluation on whether the candidate's profile aligns with the role.
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science,
# Full stack Web Development, Big Data Engineering, Devops, Data Analyst, and deep ATS functionality,
# your task is to evaluate the resume against the provided job description.
# Give me the percentage of match if the resume matches the job description. First, the output should come as percentage and then keywords missing and last final thoughts.
# """

# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")


from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
from pdf2image import convert_from_path
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        image = convert_from_path('uploaded_file',500,poppler_path='C:\Program Files\poppler-24.02.0\Library\bin')
        for i in range(len(image)):
            image[i].save('page'+str(i)+'.jpg','JPEG')
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

#submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
  Please share your professional evaluation of whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant about the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage then keywords missing, and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

