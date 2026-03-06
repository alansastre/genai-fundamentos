
Proyecto chatbot CLI básico con LangChain v1.x moderno utilizando langchain-ollama.

El chatbot se invoca por cli, y permite mantener una conversación en memoria, sin base de datos.

Se utilizará por defecto el modelo gemma3:1b, pudiendo cambiar a otro modelo como deepseek-r1:1.5b o qwen3:1.7b.

El foco no será la arquitectura, tan solo ilustrar el uso de langchain-ollama para interactuar con LLMs open source mediante ollama, por lo que la aplicación se desarrollará entera en un archivo main.py.

El entorno y dependencias ya está configurado con uv.

NO uses agentes, invoca directamente los LLM usando chat models.