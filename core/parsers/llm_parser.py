import os
from core.types import Parser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains import LLMChain

__all__ = ["get_llm_file_parser"]


def get_llm_file_parser(prompt: str) -> Parser:
    def llm_parser(text: str) -> dict:
        json_parser = JsonOutputParser()

        prompt_template = PromptTemplate(
            template=prompt,
            input_variables=["input_text"],
            partial_variables={
                "format_instructions": json_parser.get_format_instructions()
            },
        )

        llm = ChatOpenAI(
            temperature=0,
            model="gpt-4o",
            openai_api_key=os.environ.get("OPENAI_API_KEY"),  # otherwise CI fails?
        )

        chain = LLMChain(llm=llm, prompt=prompt_template, output_parser=json_parser)

        result = chain.invoke({"input_text": text})
        return result["text"]

    return llm_parser
