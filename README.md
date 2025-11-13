# 🎓 College Management System Database Blueprint

**Designing a robust relational schema for a college using a Multi-LLM Workflow and Mermaid.js.**

This repository presents the detailed **Entity-Relationship (ER) Diagram** and data model for a comprehensive **College Management System (CMS)**. The system models key aspects of academic, administrative, and extracurricular college operations.

![ER Diagram](ER%20Diagram.png)

---

## 📋 Table of Contents

1.  [🧠 Methodology: LLM-Assisted Design](#-methodology-llm-assisted-design)
2.  [🛠 Tech Stack](#-tech-stack)
3.  [📊 Data Model Summary](#-data-model-summary)
4.  [💻 Setup & Execution](#-setup--execution)
5.  [📁 Repository Contents](#-repository-contents)
6.  [🧑‍💻 Author](#-author)

---

## 🧠 Methodology: LLM-Assisted Design

The ER diagram was generated using an innovative **multi-LLM workflow** to ensure accuracy and comprehensive coverage of the database requirements. This process showcases advanced prompt engineering and model evaluation techniques.

### LLM Workflow Tools

The database schema was generated using a Streamlit application (`invokeMultipleLLMs.py`) that leverages **LiteLLM** to compare outputs from multiple Large Language Models (LLMs) running via **Ollama**.

| Tool | Purpose | Status |
| :--- | :--- | :--- |
| **LLMs** | **Llama 3** (Primary) & **Gemma 2:2B** (Secondary) | Tested/Compared |
| **Orchestration** | LiteLLM (for unified API calls) | Implemented |
| **Interface** | Streamlit (for side-by-side comparison UI) | Implemented |
| **Visualization** | Mermaid.js ER Diagram Syntax | Final Output |

> **Result:** **Llama 3** provided the most accurate and usable ER diagram syntax, which forms the final blueprint.

### The Prompt Text

The detailed instructions provided to the LLMs are available in `Prompt Text.txt`. The prompt explicitly required:
* A total of **15 entities** (9 core academic, 6 operational).
* Detailed **attributes** for each entity.
* Clearly defined **relationships** with cardinality (e.g., Many-to-One).
* Output **only in Mermaid syntax**.

---

## 🛠 Tech Stack

### 🔹 Database & Design
- **Data Modeling:** 15 Entity Schema Blueprint
- **Visualization:** Mermaid.js ER Diagram Syntax

### 🔹 LLM Integration
- **LLM Orchestration:** Python with LiteLLM
- **Models:** Ollama (Llama 3, Gemma 2:2B)
- **UI/App:** Streamlit
- **Optimization:** PyTorch (for optional GPU support in LLM inference)

---

## 📊 Data Model Summary

The final database blueprint comprises **15 core entities** to comprehensively manage all college operations.

### Core Entities & Key Attributes (Examples)

| Category | Entity | Key Attributes (Example) |
| :--- | :--- | :--- |
| **Core Academic** | **Student** | `student_id`, `name`, `dob`, `email`, `phone` |
| | **Professor** | `prof_id`, `name`, `department_id`, `email` |
| | **Course** | `course_id`, `name`, `department_id`, `credits` |
| **Operational** | **Hostel** | `hostel_id`, `name`, `capacity` |
| | **Staff** | `staff_id`, `name`, `role`, `department_id` |

### Key Relationships

| Relationship | Cardinality (Mermaid) | Description |
| :--- | :--- | :--- |
| **Student ENROLLS\_IN Enrollment** | One-to-Many (`||--o{`) | Models student registration for courses. |
| **Professor TEACHES Course** | One-to-Many (`||--o{`) | Links professors to the courses they instruct. |
| **Staff MANAGES Cafeteria/Library** | One-to-Many (`||--o{`) | Defines administrative oversight for facilities. |

### Raw Mermaid Code Snippet

The schema for the database is entirely defined in the Mermaid syntax (full code in `Output Text.txt`):

```text
erDiagram
    Student {
        string student_id
        string name
        ...
    }
    Professor {
        string prof_id
        string name
        ...
    }
    // ... (All entities defined)
    
    Student ||--o{ Enrollment : "enrolls in"
    Professor ||--o{ Course : "TEACHES"
    // ... (All relationships defined)
````

-----

## 💻 Setup & Execution

These instructions are for setting up and running the multi-LLM prompting tool (`invokeMultipleLLMs.py`) locally.

### 1️⃣ Prerequisites

1.  **Install Ollama** and pull the required models:
    ```bash
    ollama run llama3
    ollama run gemma2:2b
    ```
2.  **Install Python Dependencies**:
    ```bash
    pip install streamlit litellm torch
    ```

### 2️⃣ Execution

Run the Streamlit application from your terminal:

```bash
streamlit run invokeMultipleLLMs.py
```

**Output:** The application will start and open in your browser (e.g., `http://localhost:8501`), allowing you to compare LLM outputs in real-time.

-----

## 📁 Repository Contents

| File | Description |
| :--- | :--- |
| `ER Diagram.png` | **The final, visual ER Diagram.** |
| `Output Text.txt` | The raw **Mermaid ER code** used to generate the diagram. |
| `Prompt Text.txt` | The detailed instructions provided to the LLMs. |
| `invokeMultipleLLMs.py` | The Streamlit/LiteLLM Python script for the multi-LLM workflow. |
| `Prompt Screenshot.png` | Screenshot of the Streamlit application's input interface. |
| `Output Screenshot.png` | Screenshot of the Mermaid rendering in the app. |

-----

## 🧑‍💻 Author

**Rusheel Vijay Sable**

  * **Role:** Full Stack & AI Developer | Data Science Enthusiast
  * **Motto:** "Building scalable solutions using generative AI and robust database design principles."

<!-- end list -->

```
```
