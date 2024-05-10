from langflow.load import run_flow_from_json

# Will just use default settings, don't need to pass in any tweaks
# TWEAKS = {
#   "OpenAIModel-Ahy84": {},
#   "ChatOutput-oSzrr": {},
#   "ChatInput-B82J9": {},
#   "Prompt-kyIF3": {},
#   "AstraDBSearch-XQL1Y": {},
#   "OpenAIEmbeddings-gN6D6": {}
# }

question = input("Ask a question: ")

result = run_flow_from_json(
    flow="Langflow_v1_project.json",
    input_value=question,
    # tweaks=TWEAKS
    )

print(">", result[0].outputs[0].results)
