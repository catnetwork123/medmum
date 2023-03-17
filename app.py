from flask import Flask, render_template, request
import openai

app = Flask(__name__,template_folder="templates")

# Set OpenAI API key
openai.api_key = "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"

# Define function to generate blog post
def generate_text(prompt, length=1024, temperature=0.7):
    intro = "In this blog post, we'll discuss " + prompt + "."
    conclusion = "In conclusion, " + prompt + " is an important topic that deserves more attention."

    content_length = length - len(intro) - len(conclusion)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=intro,
        max_tokens=content_length,
        n=1,
        stop=None,
        temperature=temperature,
    )

    content = response.choices[0].text.strip()

    generated_text = intro + " " + content + " " + conclusion

    return generated_text

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for generating blog post
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    length = int(request.form['length'])
    temperature = float(request.form['temperature'])

    generated_text = generate_text(prompt, length=length, temperature=temperature)

    return render_template('result.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
