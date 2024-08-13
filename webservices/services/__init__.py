import os
import weaviate
# from langchain import PromptTemplate
from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
# from langchain.vectorstores import Weaviate
from langchain_community.vectorstores import Weaviate
from huggingface_hub import hf_hub_download
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
# from langchain.llms import HuggingFacePipeline
from langchain_community.llms import HuggingFacePipeline
from etl.get_best_model_path import latest_folds_dir, best_model_path
from transformers import (
    AutoTokenizer, 
    GPT2LMHeadModel,
)
from dotenv import load_dotenv
load_dotenv()

client = weaviate.Client("http://localhost:8080")
classname = os.getenv('WEAVIATE_CLASS')

custom_prompt_template = """
Use the following pieces of information to answer the user's question. Ignore everything from the previous conversation.

{context}
In the provided context, you will find paragraphs of documents offering solutions to specific questions. 
Each solution is linked to a respective page. As a Japanese expert, your task is to extract the relevant page IDs based on the given question, using the provided context.
Please present the extracted page IDs in a comma-separated format exclusively, without additional information.
The extracted page IDs must be present in the context.
Extract information exclusively related to the mentioned identifier from the question.

Example Question:
識別子 'naniwa' の場合、モジュール 'Apache/スコアボード/Waiting for connection' とエージェント 'prod_highschool' と障害状態 '障害状態' であればページ取得してください。
識別子 'naniwa' の場合、モジュール 'Apache/スコアボード/Waiting for connection' とエージェント 'prod_highschool' であればページ取得してください。
識別子 'naniwa' の場合、モジュール 'Apache/スコアボード/Waiting for connection' であればページ取得してください。

Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer (comma-separated format):
"""

prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])

# model 1
model_name_or_path = "TheBloke/Llama-2-7B-Chat-GGML"
model_basename = "llama-2-7b-chat.ggmlv3.q4_1.bin"
model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)

# Create LLM object
if torch.cuda.is_available():
    config = {'context_length': 4096, 'gpu_layers':150, 'threads':0, 'batch_size': 300}
else:
    config = {'context_length': 4096}

llm = CTransformers(
        model = model_path,
        model_type="llama",
        max_new_tokens = 512,
        config = config,
        temperature = 0
    )
print('------------------------------init called-------------------------------')

# model 2: rinna/llama-3-youko-8b
# model_id = "rinna/llama-3-youko-8b"
# pipeline = transformers.pipeline(
#     "text-generation",
#     model=model_id,
#     model_kwargs={"torch_dtype": torch.bfloat16,
#                   "cache_dir": "/mnt/data1/hf_cache"
# },
#     device_map="auto",
#     # device_map={"": "cuda:0"},
#     max_new_tokens=256
# )

# llm = HuggingFacePipeline(pipeline=pipeline)
# llm.model_id = model_id

# model 3
# from huggingface_hub import login

# model_path = "Fugaku-LLM/Fugaku-LLM-13B-instruct"
# cache_directory = "/mnt/data1/hf_cache"

# tokenizer = AutoTokenizer.from_pretrained(model_path, cache_dir=cache_directory,  use_auth_token=huggingface_token)
# model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map="auto", cache_dir=cache_directory,  use_auth_token=huggingface_token)
# import pdb; pdb.set_trace()
# print(model)
# # pipeline = transformers.pipeline("text-generation", model=model, tokenizer=tokenizer)
# pipeline = transformers.pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=1000)
# print(pipeline)
# llm = HuggingFacePipeline(pipeline=pipeline)
# llm.model_id = model_path

# import pdb; pdb.set_trace()

# model 3 load method 2
# pipeline = transformers.pipeline(
#     "text-generation",
#     model=model_path,
#     model_kwargs={"torch_dtype": torch.bfloat16,
#                   "cache_dir": "/mnt/data1/hf_cache"
# },
#     device_map="auto",
#     # device_map={"": "cuda:0"},
#     max_new_tokens=128
# )

# llm = HuggingFacePipeline(pipeline=pipeline)
# llm.model_id = model_path



vectorstore = Weaviate(client, classname, "final_document")
initial_retriever = vectorstore.as_retriever(search_kwargs={'k': 4})

qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                    #    retriever=vectorstore.as_retriever(search_kwargs={'k': 4}),
                                       retriever=initial_retriever,
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt': prompt}
                                       )

def update_retriever(qa_chain, retriever):
    qa_chain.retriever = retriever


# Load Trained Model
class GetModelTokenizer:
    def __init__(self):
        # self.model_path = self.get_model_path()
        # self.model_path = '/mnt/data1/imai_phase3_genAI_copy_for_phase4/fold_output_dir12jul/4/checkpoint-801'
        # self.model_path = '/mnt/data1/imai_phase3_genAI_copy_for_phase4/fold_output_dir19jul/4/checkpoint-801'
        # self.model_path = '/mnt/data1/imai_phase_4new/model_files/20240725_123433/5/checkpoint-950'
        # newly trained model
        # self.model_path = '/mnt/data1/imai_phase_4new/model_files/20240726_100822/5/checkpoint-570'
        # without pause resume model
        # self.model_path = "/mnt/data1/imai_phase_4new/testresume/without pause resume"
        # with pause and resume
        # self.model_path = "/mnt/data1/imai_phase_4new/testresume/withpauseresume"
        # newly 12 aug model without pause and resume
        self.model_path = "/mnt/data1/imai_phase_4new/testresume/withoutresume12aug"
        print(self.model_path, '================')


    def get_model_path(self):
        # trained_model_files_base_dir = os.path.join(os.getcwd(), 'model_files')
        # new path added as below
        trained_model_files_base_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')), 'model_files')

        model_path = latest_folds_dir(trained_model_files_base_dir)
        print('model_path:', model_path)
        return model_path

    def load_model(self):
        model = GPT2LMHeadModel.from_pretrained(self.model_path)
        return model

    def load_tokenizer(self):
        tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        return tokenizer
