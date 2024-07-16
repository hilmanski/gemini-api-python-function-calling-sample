import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Sample custom function
def score_checker(score):
    if score > 0.5:
        return "Student passed the test"
    else:
        return "Student failed the test"
    
score_checker_declaration = {
    'name': "score_checker",
    'description': "Check if a score is a pass or fail",
    'parameters': {
        "type": "object",
        "properties": {
            "score": {
                "type": "number",
                "description": "The score to check"
            }
        },
        "required": [
            "score"
        ]
    },
}

prompt = "I saw my test score was 0.4. Did I pass?"

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(
    prompt,
    tools=[{
        'function_declarations': [score_checker_declaration],
    }],
)

function_call = response.candidates[0].content.parts[0].function_call
args = function_call.args
function_name = function_call.name

if function_name == 'score_checker':
    result = score_checker(args['score'])


response = model.generate_content(
    "Based on this information `" + result + "` respond to the student in a friendly manner.",
)
print(response.text)

