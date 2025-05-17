from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import UnstructuredWordDocumentLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
import warnings
warnings.filterwarnings('ignore')

# List of Word documents
# path="./common_solutions_and_problems/"
path=""
files = [
    # path+"Well_Planning_Problems_and_Solutions.docx",
    # path+"Rig_Contracting_Problems_and_Solutions.docx",
    # path+"Expat_Employment_Problems_and_Solutions.docx",
    # path+"Upstream_Manual_System_Problems_and_Solutions.docx",
    # path+"Well_Target_Days_Calculation_Problems_and_Solutions.docx",
    # path+"Realtime_Monitoring_Problems_and_Solutions.docx",

    path+"Upstream_Manual_System_Problems_and_Solutions.docx",
    path+"Well_Attachments_Common_Issues_and_Solutions.docx",
    path+"Rig_Contracting_Problems_and_Solutions.docx",
    path+"Adhoc_Reporting_Common_Issues_and_Solutions.docx",
    path+"Expat_Employment_Problems_and_Solutions.docx",
    path+"Rig_Scheduling_Common_Problems.docx",
    path+"Well_Planning_Problems_and_Solutions.docx",
    path+"Best_Practices_Issues_and_Solutions.docx",
    path+"Realtime_Monitoring_Problems_and_Solutions.docx",
    path+"Well_Target_Days_Calculation_Problems_and_Solutions.docx"
]
print(files)
# Load all documents
all_docs = []
for file in files:
    loader = UnstructuredWordDocumentLoader(file)
    all_docs.extend(loader.load())

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(all_docs)

# Store in ChromaDB
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="./vectorstore")
# vectorstore.persist()

print("Vectorstore setup complete.")