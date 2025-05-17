from llama_cpp import Llama

# Load the model (happens once)
llm = Llama(
    model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",  # updated path to match actual file
    n_ctx=512,
    n_threads=4
)

def process_input(text):
    prompt = f"Summarize the following system log:\n\n{text}\n\nSummary:"
    
    response = llm(
        prompt,
        max_tokens=256,
        stop=["</s>"]
    )
    
    return response["choices"][0]["text"].strip()