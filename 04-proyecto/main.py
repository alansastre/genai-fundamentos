#!/usr/bin/env python3
"""
Chatbot CLI básico con LangChain v1.x moderno utilizando langchain-ollama.
Mantiene conversación en memoria sin base de datos.
"""

import sys
from typing import List
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage, AIMessage, SystemMessage


class ChatbotCLI:
    """Chatbot CLI simple con memoria de conversación."""
    
    def __init__(self, model_name: str = "gemma3:1b"):
        """
        Inicializa el chatbot con el modelo especificado.
        
        Args:
            model_name: Nombre del modelo de Ollama a usar
        """
        self.model_name = model_name
        self.llm = ChatOllama(model=model_name, temperature=0.7)
        self.conversation_history: List = []
        
    def change_model(self, new_model: str):
        """Cambia el modelo de Ollama."""
        self.model_name = new_model
        self.llm = ChatOllama(model=new_model, temperature=0.7)
        print(f"✓ Modelo cambiado a: {new_model}")
        
    def add_system_message(self, content: str):
        """Añade un mensaje del sistema al historial."""
        self.conversation_history.append(SystemMessage(content=content))
        
    def chat(self, user_input: str) -> str:
        """
        Procesa el mensaje del usuario y devuelve la respuesta del modelo.
        
        Args:
            user_input: Mensaje del usuario
            
        Returns:
            Respuesta del modelo
        """
        # Añadir mensaje del usuario al historial
        self.conversation_history.append(HumanMessage(content=user_input))
        
        # Invocar el modelo con el historial completo
        response = self.llm.invoke(self.conversation_history)
        
        # Extraer el contenido de la respuesta
        ai_response = response.content
        
        # Añadir respuesta del modelo al historial
        self.conversation_history.append(AIMessage(content=ai_response))
        
        return ai_response
    
    def clear_history(self):
        """Limpia el historial de conversación."""
        self.conversation_history = []
        print("✓ Historial de conversación limpiado")
        
    def show_info(self):
        """Muestra información sobre el chatbot."""
        print(f"\n{'='*60}")
        print(f"Modelo actual: {self.model_name}")
        print(f"Mensajes en historial: {len(self.conversation_history)}")
        print(f"{'='*60}\n")


def print_help():
    """Muestra la ayuda de comandos."""
    help_text = """
Comandos disponibles:
  /help          - Muestra esta ayuda
  /model <name>  - Cambia el modelo (ej: gemma3:1b, deepseek-r1:1.5b, qwen3:1.7b)
  /clear         - Limpia el historial de conversación
  /info          - Muestra información del chatbot
  /exit o /quit  - Sale del programa
  
Para chatear, simplemente escribe tu mensaje y presiona Enter.
"""
    print(help_text)


def main():
    """Función principal del chatbot CLI."""
    print("="*60)
    print("🤖 Chatbot CLI con Ollama y LangChain")
    print("="*60)
    print("\nEscribe '/help' para ver los comandos disponibles")
    print("Escribe '/exit' o '/quit' para salir\n")
    
    # Inicializar chatbot con modelo por defecto
    chatbot = ChatbotCLI(model_name="gemma3:1b")
    
    # Mensaje de bienvenida del sistema (opcional)
    chatbot.add_system_message("Eres un asistente útil y amigable.")
    
    try:
        while True:
            # Leer entrada del usuario
            user_input = input("Tú: ").strip()
            
            # Comandos especiales
            if not user_input:
                continue
                
            if user_input.startswith("/"):
                command = user_input.split()[0].lower()
                
                if command in ["/exit", "/quit"]:
                    print("\n¡Hasta luego! 👋")
                    break
                    
                elif command == "/help":
                    print_help()
                    
                elif command == "/clear":
                    chatbot.clear_history()
                    
                elif command == "/info":
                    chatbot.show_info()
                    
                elif command == "/model":
                    if len(user_input.split()) > 1:
                        new_model = user_input.split()[1]
                        chatbot.change_model(new_model)
                    else:
                        print("❌ Error: Especifica un modelo. Ejemplo: /model deepseek-r1:1.5b")
                        
                else:
                    print(f"❌ Comando desconocido: {command}. Escribe '/help' para ver los comandos disponibles.")
                    
            else:
                # Procesar mensaje del usuario
                try:
                    print("🤖 Pensando...", end="\r")
                    response = chatbot.chat(user_input)
                    print("🤖 Bot: " + response)
                    print()  # Línea en blanco para mejor legibilidad
                except Exception as e:
                    print(f"\n❌ Error al procesar el mensaje: {e}")
                    print("Verifica que Ollama esté corriendo y que el modelo esté disponible.\n")
                    
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
