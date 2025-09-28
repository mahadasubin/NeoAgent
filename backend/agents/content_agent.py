import openai

def generate_content(topic, product, audience):
    prompt = f"Create a LinkedIn marketing post for {product}. Topic: {topic}. Audience: {audience}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
