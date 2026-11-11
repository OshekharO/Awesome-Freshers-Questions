# 🧠 Prompt Library & AI Engineering Cheat Sheet

*A curated collection of effective AI prompts, architectural templates, and technical interview questions for AI and Prompt Engineering freshers (Updated November 2026).*

![Prompt Library](https://img.shields.io/badge/Prompts-Collection-blue)
![Categories](https://img.shields.io/badge/Categories-5+-green)
![Status](https://img.shields.io/badge/Maintenance-Active-brightgreen)

## 📚 Overview

This directory contains my personal collection of AI prompts that have been tested and refined across different AI tools and platforms. Each prompt is designed to produce high-quality, consistent results for specific use cases.

---

## 🗂️ Categories

### 🤖 AI Development
Prompts for coding assistance, debugging, code review, and development workflows.
- **Code Generation** - Templates for generating specific code patterns
- **Debugging** - Systematic approaches to identifying and fixing issues
- **Code Review** - Structured analysis templates
- **Architecture** - System design and planning prompts

### 🎨 UI/UX Design
Prompts for creating interfaces, design systems, and user experiences.
- **Component Design** - UI element specifications
- **Design Systems** - Consistent styling and theming
- **User Flows** - Interaction and navigation patterns
- **Responsive Design** - Cross-device compatibility

### 🔧 Code Generation
Language-specific prompts for various programming tasks.
- **Python** - Data science, web development, automation
- **Java** - Enterprise patterns, Spring framework
- **JavaScript/TypeScript** - Frontend and Node.js development
- **SQL** - Database queries and optimization
- **Shell Scripting** - Automation and system tasks

### 📝 Documentation
Prompts for creating comprehensive technical documentation.
- **API Documentation** - RESTful services and endpoints
- **Code Comments** - Inline documentation standards
- **Technical Guides** - Tutorials and how-tos
- **README Templates** - Project documentation structure

---

## 🎯 Part 2: AI & Prompt Engineering Technical Interview Questions (Freshers 2026)

### Question 1: What are the core Prompt Engineering techniques, and when should you choose each?

#### Logic & Background:
Prompt engineering guides Large Language Models (LLMs) toward accurate, structured, and deterministic outputs without retraining or weight updates.

#### Method 1: Zero-Shot Prompting (Direct Task Instruction)
- **Logic**: Present task directly to the LLM without demonstrations or prior examples.
- **When to use**: Standard tasks (translation, summarization, sentiment analysis) where the LLM has strong pre-trained knowledge.
- **Limitation**: Inconsistent formatting or unpredictable edge-case handling for complex business logic.

#### Method 2: Few-Shot Prompting (In-Context Learning)
- **Logic**: Provide 2 to 5 input-output demonstration pairs within the prompt before giving the final target input.
- **When to use**: When strict output format (e.g. JSON schema, custom classification tags) or domain-specific tone is required.
- **Why it works**: Directs model attention weights toward the demonstrated syntactic pattern without parameter fine-tuning.

#### Method 3: Chain-of-Thought (CoT) & Zero-Shot CoT
- **Logic**: Instruct the model to break down complex reasoning step-by-step before producing the final answer ("Think step-by-step").
- **When to use**: Multi-step arithmetic, logic puzzles, algorithmic debugging, and root-cause analysis.
- **Why it works**: Allows the autoregressive decoder to generate intermediate tokens, expanding the working memory context before committing to an answer.

#### Method 4: ReAct (Reasoning + Acting) / Agentic Tool-Use Pattern
- **Logic**: Combines Chain-of-Thought reasoning with external environment actions (Observation -> Thought -> Action -> Observation).
- **When to use**: AI agents searching the web, querying databases, running code, or calling APIs.

---

### Question 2: RAG (Retrieval-Augmented Generation) vs Fine-Tuning vs System Prompts: How do you choose the right approach?

#### Logic & Background:
A common architectural interview question for AI engineers designing enterprise LLM applications.

| Criterion | System Prompt Engineering | Retrieval-Augmented Generation (RAG) | Model Fine-Tuning |
|---|---|---|---|
| **Primary Goal** | Steer tone, personality, format, and simple rules | Connect LLM to external, dynamic, private, or real-time data | Teach new specialized styles, specific vocabulary, or task formats |
| **Data Freshness** | Static (per conversation) | Dynamic (real-time vector DB queries) | Static (frozen at training time) |
| **Hallucination Risk** | High | Low (grounded in retrieved context) | Moderate |
| **Cost & Latency** | Lowest (prompt tokens only) | Low to Medium (retrieval + prompt overhead) | High upfront compute cost; low per-token inference |
| **Setup Complexity** | Minutes | Days / Weeks (Embeddings, Vector DB, Chunking) | Weeks / Months (Dataset curation, GPU training) |

#### Recommendation Rule:
1. Always start with **Prompt Engineering**.
2. If the model needs proprietary knowledge, enterprise documents, or up-to-date facts -> Implement **RAG**.
3. Only use **Fine-Tuning** if tone, syntax, or task efficiency cannot be achieved via RAG/prompting, or to distill a large model into a smaller, cheaper local model.

---

### Question 3: How do you prevent and mitigate Hallucinations in LLM applications?

#### Logic & Background:
Hallucinations occur when an LLM generates factually false or unverifiable statements with high confidence.

#### Method 1: Grounded Retrieval with Explicit Negative Constraints
- Inject verified domain documents into the context window.
- Add strict system constraints: *"Answer strictly using only the provided context. If the answer cannot be found in the context, explicitly state 'I do not have enough information to answer this question' without guessing."*

#### Method 2: Temperature & Top-p Hyperparameter Tuning
- **Temperature (0.0 to 0.2)**: Reduces randomness; forces greedy decoding of top-probability tokens. Essential for factual Q&A, math, and code generation.
- **Top-p (Nucleus Sampling)**: Limits token selection to cumulative probability distribution threshold (e.g. 0.9).

#### Method 3: Self-Consistency & Citation Verification
- Prompt the model to cite exact source sentences or document IDs for every assertion.
- Run a secondary verification step (LLM-as-a-judge or regex checker) comparing claims against cited context.

#### Method 4: Guardrails & Schema Validation
- Use structured output tools (JSON mode, Pydantic, Zod, NeMo Guardrails) to enforce schema integrity and filter out of bounds responses.

---

### Question 4: How does Function Calling / Tool Use work in LLMs, and what is the Model Context Protocol (MCP)?

#### Logic & Background:
Modern AI systems interact with tools, databases, and APIs via structured schemas.

#### Execution Lifecycle (Step-by-Step):
1. **Tool Definition**: The client application sends the user prompt along with a list of available tools described in JSON Schema format (function name, description, required parameters).
2. **Model Decision**: The LLM analyzes the user request. If a tool is needed, it stops generating text and outputs a structured `tool_calls` JSON object with the function name and extracted arguments.
3. **Client Execution**: The client backend parses the JSON, executes the real function (e.g. database query, weather API, calculator), and receives the result.
4. **Final Response**: The client appends the function result back into the message history as a `role: tool` message. The LLM reads the result and produces a natural language summary to the user.

#### What is Model Context Protocol (MCP)?
- An open, standardized protocol developed by Anthropic (November 2024+) providing a universal client-server architecture for AI models to connect securely to local files, external APIs, developer tools, and cloud databases (like Neon, Render, GitHub) without writing bespoke integrations for every model provider.

---

*Created By Shekher Saksham Shashi (AMPICS)*
