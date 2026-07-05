def Tracing():
    from dotenv import load_dotenv
    from langchain.chat_models import init_chat_model
    from langsmith import traceable

    load_dotenv()

    model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")
    response = model.invoke("How many global IT companies are operating from Hyderabad, India?")
    print(response.content)