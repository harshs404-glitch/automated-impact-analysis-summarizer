import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
import httpx
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

tiktoken_cache_dir = os.path.join(os.path.dirname(__file__), "token")
os.environ["TIKTOKEN_CACHE_DIR"] = tiktoken_cache_dir
os.makedirs(tiktoken_cache_dir, exist_ok=True)

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://genailab.tcs.in")
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY missing — copy .env.example to .env and fill it in")

_http_client = httpx.Client(verify=False)

LLM = ChatOpenAI(
    base_url=BASE_URL,
    model="azure_ai/genailab-maas-DeepSeek-V3-0324",
    api_key=API_KEY,
    http_client=_http_client,
    temperature=0,
)

EMBEDDING_MODEL = OpenAIEmbeddings(
    base_url=BASE_URL,
    model="azure/genailab-maas-text-embedding-3-large",
    api_key=API_KEY,
    http_client=_http_client,
)

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
RETRIEVER_K = 8