import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = 'ls__85291a99f2ab490bab7da20a3f9b254e'
os.environ['LANGCHAIN_PROJECT'] = 'no-phish-ai'
os.environ['OPENAI_API_KEY'] = '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'


from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage

llm = ChatOpenAI()
#llm.invoke("Hello, world!")


chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are a security assistant that tells users about phishy sites."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

llm = ChatOpenAI()
llm(chat_template.format_messages(text="google.com"))