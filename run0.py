import vertexai
from flask import Flask
from vertexai.language_models import TextGenerationModel

vertexai.init(project="amiable-elf-396321", location="us-central1")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison")
response = model.predict(
    """what is the immune system?""",
    **parameters
)
print(f"Response from Model: {response.text}")

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = model.predict(
        """what is the immune system?""",
        **parameters
    )
    return response.text 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

    
