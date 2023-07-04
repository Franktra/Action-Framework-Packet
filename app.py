# Action Framework

## Introduction
The Action Framework is a strategic methodology designed to optimize interaction with AI language models. It provides a structured approach to formulate prompts for better AI outputs. 

## Three-Step Iterative Process
The framework revolves around a three-step iterative process:
1. Goal specification - Clearly stating what you want the AI to generate.
2. Action set-up - Framing the AI's role and providing contextual instructions.
3. Evaluation & refinement - Evaluating the AI’s output and iteratively refining the prompts to get the desired output.

## Benefits
- Improves effectiveness and accuracy of AI outputs
- Encourages iterative refinement, leading to better results over time
- Provides a systematic approach to prompt engineering

# Python Script for Interaction with AI
```python
import openai

openai.api_key = 'your-api-key'

def generate_ai_response(prompt, temperature=0.5, max_tokens=100):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=temperature,
      max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def interact_with_ai(goal, action_setup, refinement_steps):
    output = None
    for i in range(refinement_steps):
        prompt = f"{action_setup}\n{goal}"
        output = generate_ai_response(prompt)
        if output is satisfactory:    # User-defined evaluation condition
            break
        else:
            goal, action_setup = refine_prompt(goal, action_setup)  # User-defined function to refine prompt based on feedback
    return output
