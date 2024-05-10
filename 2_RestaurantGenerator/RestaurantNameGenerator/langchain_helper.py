# from langchain.llms import OpenAI # deprecated
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

# Import the OpenAI API key
from secret_key import openapi_key
import os
os.environ['OPENAI_API_KEY'] = openapi_key

# Create an instance of the OpenAI class
llm = OpenAI(temperature=0.7)

# Function to generate restaurant name and menu items
def generate_restaurant_name_and_menu_items(cusine):
    
    
    
    llm = OpenAI(temperature=0.6)

    # chain 1 - Generate restaurant name. 
    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a restaurant for {cuisine}. Suggest one fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name') # added output_key

    # chain 2 - Generate food menu items based on restaurant name
    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest 5 menu items (only name, no description) for {restaurant_name}. Return it as a comma separated list"
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items') # added output_key
    
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
        )
    # response = chain({'cuisine': cusine})

    response = chain.invoke({'cuisine': cusine})
    # print(response)

    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_menu_items('Italian'))
    # Expected output: 
    # {
    # 'restaurant_name': 'Pasta Palace', 
    # 'menu_items': 'Spaghetti, Lasagna, Ravioli, Fettuccine Alfredo, Carbonara'
    # }