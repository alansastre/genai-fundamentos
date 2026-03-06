# Fundamentos de IA Generativa para Developers

[![Python](https://img.shields.io/badge/Python-3.13.5-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1.2.6-1C3C3C?logo=langchain&logoColor=white)](https://langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-latest-000000?logo=ollama&logoColor=white)](https://ollama.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)](https://openai.com/)
[![Anthropic](https://img.shields.io/badge/Anthropic-Claude-D4A27F?logo=anthropic&logoColor=white)](https://anthropic.com/)
[![Google AI](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white)](https://ai.google.dev/)
[![uv](https://img.shields.io/badge/uv-package_manager-DE5FE9?logo=astral&logoColor=white)](https://docs.astral.sh/uv/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

Curso práctico de **IA Generativa** orientado a desarrolladores. Aprende los fundamentos teóricos y prácticos para integrar LLMs en tus aplicaciones usando LangChain con modelos locales (Ollama) y APIs comerciales (OpenAI, Anthropic, Google).

**Autor:** Alan Sastre

## Contenido del Curso

### 01 - Fundamentos Teóricos
| Notebook | Descripción |
|----------|-------------|
| `01-genai-que-es-ia-generativa` | Introducción a la IA Generativa |
| `02-genai-que-puede-hacer` | Casos de uso y aplicaciones |
| `03-genai-historia-y-evolucion` | Historia y evolución de los LLMs |
| `04-genai-llm-arquitectura-alto-nivel` | Arquitectura de los modelos de lenguaje |
| `05-genai-llm-limitaciones-y-alucinaciones` | Limitaciones y alucinaciones |
| `06-genai-roles-disciplinas-profesionales` | Roles profesionales en IA |

### 02 - Iniciación Práctica
| Notebook | Descripción |
|----------|-------------|
| `01-genai-setup-entorno-python-ollama-langchain` | Configuración del entorno de desarrollo |
| `02-genai-langchain-modelos-ollama` | Uso de modelos locales con Ollama |
| `03-genai-langchain-message-types` | Tipos de mensajes en LangChain |
| `04-genai-langchain-generation-parameters` | Parámetros de generación |

### 03 - Proveedores de LLMs
| Notebook | Descripción |
|----------|-------------|
| `01-genai-ecosistema-proveedores` | Panorama de proveedores |
| `02-genai-langchain-openai` | Integración con OpenAI |
| `03-genai-langchain-anthropic` | Integración con Anthropic (Claude) |
| `04-genai-langchain-google` | Integración con Google (Gemini) |

### 04 - Proyecto: Chatbot CLI
Aplicación de consola que implementa un chatbot conversacional usando LangChain y Ollama. Incluye:
- Memoria de conversación
- Cambio dinámico de modelos
- Comandos interactivos (`/help`, `/model`, `/clear`, `/info`)

> **Nota:** Los notebooks incluyen diagramas Mermaid que no se visualizan en GitHub. Para verlos correctamente, abre los notebooks en VS Code con la extensión [Quarto](https://quarto.org/).

## Requisitos Previos

- **Python 3.13+**
- **Ollama** instalado y en ejecución (para modelos locales)
- **API Keys** (opcionales, para proveedores comerciales):
  - `OPENAI_API_KEY`
  - `ANTHROPIC_API_KEY`
  - `GOOGLE_API_KEY`

## Instalación

### 1. Instalar Ollama

Descarga e instala Ollama desde [ollama.com](https://ollama.com/) y descarga un modelo:

```bash
ollama pull gemma3:1b
```

### 2. Instalar uv (gestor de proyectos Python)

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Clonar y configurar el proyecto

```bash
git clone https://github.com/TU_USUARIO/genai-fundamentos.git
cd genai-fundamentos

# Crear entorno virtual e instalar dependencias
uv venv --python 3.13.5
uv add -r requirements.txt
```

### 4. Activar el entorno virtual

**Windows:**
```powershell
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 5. Configurar API Keys (opcional)

Crea un archivo `.env` en la raíz del proyecto:

```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
```

## Uso

### Ejecutar los Notebooks

Abre los notebooks con VS Code (extensión Jupyter) o ejecuta:

```bash
jupyter notebook
```

### Ejecutar el Chatbot CLI

```bash
python 04-proyecto/main.py
```

**Comandos disponibles:**
- `/help` - Muestra la ayuda
- `/model <nombre>` - Cambia el modelo (ej: `gemma3:1b`, `deepseek-r1:1.5b`)
- `/clear` - Limpia el historial
- `/info` - Muestra información del chatbot
- `/exit` - Salir

## Dependencias Principales

| Paquete | Versión | Descripción |
|---------|---------|-------------|
| `langchain` | 1.2.6 | Framework para aplicaciones LLM |
| `langchain-ollama` | 1.0.1 | Integración con Ollama |
| `langchain-openai` | 1.1.7 | Integración con OpenAI |
| `langchain-anthropic` | 1.3.1 | Integración con Anthropic |
| `langchain-google-genai` | 4.2.0 | Integración con Google AI |
| `jupyter` | 1.1.1 | Notebooks interactivos |

## Estructura del Proyecto

```
genai-fundamentos/
├── 01-fundamentos/          # Notebooks de teoría
├── 02-iniciacion/           # Notebooks de iniciación práctica
├── 03-proveedores/          # Notebooks de integración con APIs
├── 04-proyecto/             # Chatbot CLI
│   └── main.py
├── .env                     # Variables de entorno (no incluido)
├── pyproject.toml           # Configuración del proyecto
├── requirements.txt         # Dependencias alternativas (pip)
└── README.md
```

## Licencia

Este proyecto está bajo la licencia MIT.

