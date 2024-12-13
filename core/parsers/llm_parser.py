import os
from core.types import Parser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains import LLMChain

__all__ = ["get_llm_file_parser"]


def get_llm_file_parser(
    prompt: str, allowed_root_titles: list[str], openai_model: str = "gpt-4o"
) -> Parser:
    def llm_parser(text: str) -> dict:
        json_parser = JsonOutputParser()

        prompt_template = PromptTemplate(
            template=prompt,
            input_variables=["input_text"],
            partial_variables={
                "format_instructions": json_parser.get_format_instructions(),
            },
        )

        llm = ChatOpenAI(
            temperature=0,
            model=openai_model,
        )

        chain = LLMChain(llm=llm, prompt=prompt_template, output_parser=json_parser)

        result = chain.invoke(
            {"input_text": text, "allowed_titles": allowed_root_titles}
        )
        return result["text"]

    return llm_parser
