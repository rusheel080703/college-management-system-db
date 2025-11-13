ER Diagram Homework – College Management System
 
Overview

This homework focuses on designing a detailed ER diagram for a small college management system.
The diagram models key entities, their attributes, and relationships to represent the college's academic, administrative, and extracurricular operations.
The system covers student enrollment, courses, professors, classrooms, departments, hostels, libraries, clubs, staff, events, and cafeterias.

We used Llama 3 and Gemma 2:2B via Ollama to generate the ER diagram, but Llama 3 produced the correct final output.

Entities

The system includes core academic entities and additional operational entities:

Core (9): Student, Professor, Class, School, Department, Course, Room, Enroll, Building.

Additional (6): Library, Hostel, Club, Staff, Event, Cafeteria.

Each entity has clearly defined attributes, such as:

Student: student_id, name, dob, email, phone

Course: course_id, name, department_id, credits

Hostel: hostel_id, name, capacity


Relationships

The ER diagram defines cardinality relationships between entities:

Student ENROLLS_IN Enrollment (many-to-many)

Professor TEACHES Course (one-to-many)

Course ENROLLED_IN Enrollment (many-to-many)

Professor WORKS_AT Department (many-to-one)

Classroom HOLDS Schedule (one-to-many)

Schedule DEALS_WITH Assignment (one-to-many)

Student TAKES Exam (many-to-many)

Club HOSTS Event (one-to-many)

Staff MANAGES Cafeteria & Library (many-to-one)

Hostel HOUSES Student (one-to-many)

These relationships reflect real-world college operations, showing how students, staff, courses, and facilities interact.


Tools & Workflow

Llama 3 (primary) and Gemma 2:2B (secondary) via Ollama

Mermaid.js for visual ER diagram rendering

VS Code for writing and testing Mermaid syntax

Markdown for documentation and README

Note: While both LLMs were tested, Llama 3 provided the accurate and usable ER diagram syntax, including proper entity attributes and relationships.

Outcome

The final ER diagram was generated using Llama 3, as it provided a more accurate structure than Gemma 2:2B.
It models the college database effectively and can serve as a blueprint for implementation.