# Google Cloud Associate Data Practitioner Study Guide

**Goal:** Pass the Google Cloud Certified Associate Data Practitioner exam.

**Background:** Data Scientist focused on supervised learning / Total beginner in GCP Data Infrastructure.

**Schedule:** 4 hours per day, Monday through Saturday (24 hours/week).

---

## 1. Territory Map (Overview)

We divide your journey into **4 Sequential Modules**, designed to take you from foundational cloud concepts to final exam readiness.

| Module | Module Name | Learning Objective | Interdependence |
| --- | --- | --- | --- |
| **Module 1** | **Cloud Fundamentals & Data Ingestion** | Understand the GCP cloud model, basic IAM, and how to bring structured and unstructured data from external sources into GCP (Cloud Storage and BigQuery). | *Mandatory foundation for everything else.* |
| **Module 2** | **Storage, Modeling, and Governance** | Design efficient schemas, manage partitions/clusters in BigQuery, apply data governance (Dataplex), and ensure data security/quality. | *Requires Module 1 (data already ingested into GCP).* |
| **Module 3** | **Processing, Pipelines, and Basic AI/ML** | Build data pipelines (Dataflow/Dataproc) and apply Machine Learning in a native, simplified way within the GCP ecosystem (BigQuery ML and Vertex AI Workbench). | *Requires Modules 1 and 2 to be mastered.* |
| **Module 4** | **Operations, Optimization, and Exam Simulation** | Monitor costs, optimize queries, troubleshoot pipeline failures, and complete official practice tests under time pressure. | *Requires Modules 1, 2, and 3.* |

---

## 2. Curated Resources (Where to Learn)

### **Module 1: Fundamentals & Ingestion**

* **Official/Technical Source:** Official Google Cloud Documentation: *Google Cloud Fundamentals: Core Infrastructure* and the overview sections for *Cloud Storage* and *BigQuery Loading Data*.
* **Conceptual/Educational Source:** Official learning path on *Google Cloud Skills Boost* tailored for the Associate Data Practitioner.
* **Practical Source:** Qwiklabs Hands-on Labs: *Google Cloud Essentials* and *BigQuery: Qwik Start - Console*.

### **Module 2: Storage, Modeling & Governance**

* **Official/Technical Source:** BigQuery Query Optimization and Data Modeling Guide (Official GCP Documentation).
* **Conceptual/Educational Source:** Google Cloud Architecture Center articles on *Data Warehousing* and partitioning/clustering.
* **Practical Source:** Example GitHub Repository: Google Cloud's public repository with BigQuery modeling code samples (`googlecloudplatform/training-data-analyst`).

### **Module 3: Processing & AI/ML**

* **Official/Technical Source:** Official documentation for *BigQuery ML (BQML)* and introduction to *Vertex AI Workbench*.
* **Conceptual/Educational Source:** Videos from the *Cloud Bytes* series or *Google Cloud Tech* YouTube talks focused on Dataflow vs. Dataproc and BQML.
* **Practical Source:** Qwiklabs Hands-on Lab: *Predict Movie Ratings with BigQuery ML*.

### **Module 4: Operations & Simulation**

* **Official/Technical Source:** Official *Associate Data Practitioner Exam Guide* and sample practice questions.
* **Conceptual/Educational Source:** Google Cloud Blog posts on data cost management (*Cost Optimization Best Practices*).
* **Practical Source:** Market practice exams on platforms like *Udemy* (specifically updated for the Associate Data Practitioner).

---

## 3. ⚡ Weekly Active Roadmap (4-Week Schedule)

Your commitment is **4 hours per day (24 hours/week)**. Here is how we break down the month:

```
WEEK 1 ──────► WEEK 2 ──────► WEEK 3 ──────► WEEK 4
Fundamentals   Storage,       Processing,    Operations,
& Ingestion    Modeling &     Pipelines &    Optimization &
               Governance     AI/ML          Simulations

```

---

### **Week 1: Module 1 (Fundamentals & Ingestion)**

* **Main Focus:** Cloud concepts, IAM, Cloud Storage (storage classes), and initial data loading into BigQuery (CSV, JSON, Avro).
* **Mandatory Practical Task (GitHub):** Write a Python script (using the GCP API) to generate synthetic sales data, automatically upload it to a Cloud Storage bucket, and create a routine that loads it into a partitioned table in BigQuery. Document the step-by-step process in your `README.md`.
* **Completion Signal:** Can you explain the differences between Cloud Storage classes (Standard, Nearline, Coldline, Archive) and load data via the Console and CLI without looking at the documentation?

---

### **Week 2: Module 2 (Storage, Modeling & Governance)**

* **Main Focus:** Dimensional modeling in Data Warehouses, partitioning vs. clustering in BigQuery, views, materialized views, and Dataplex fundamentals.
* **Mandatory Practical Task (GitHub):** Take a public dataset in BigQuery (e.g., `bigquery-public-data.austin_311`), create an optimized denormalized table using date partitioning and category clustering. Write an optimized query comparing processed byte costs before and after optimization.
* **Completion Signal:** Can you mathematically or architecturally justify when to use partitioning versus clustering in a BigQuery table?

---

### **Week 3: Module 3 (Processing, Pipelines & AI/ML)**

* **Main Focus:** ETL/ELT concepts, introduction to Apache Beam / Dataflow, and applying Machine Learning directly inside the warehouse using BigQuery ML (regression, classification).
* **Mandatory Practical Task (GitHub):** In BigQuery ML, train a linear or logistic regression model using real public data. Extract evaluation metrics (ROC, RMSE) via SQL and save the documented script in your portfolio repository.
* **Completion Signal:** Can you explain the data flow in a Dataflow pipeline and train a basic predictive model using only SQL commands in BigQuery?

---

### **Week 4: Module 4 (Operations, Optimization & Simulation)**

* **Main Focus:** Cost management, monitoring BigQuery jobs, troubleshooting common IAM permission errors, and taking practice exams.
* **Mandatory Practical Task (GitHub):** Create a Markdown pocket guide in your GitHub repo summarizing major BigQuery cost pitfalls, alongside a troubleshooting flowchart for IAM errors in data projects.
* **Completion Signal:** Can you score over 80% on an official 50-question practice exam under timed conditions without consulting any materials?

---

## 4. Retention Strategy (How Not to Forget)

### **1. Spaced Repetition Techniques:**

* **Cornell Notes:** Organize your notes by dividing the page into Cues/Questions, Summary, and Detailed Notes. Review them after 1 day, 7 days, and 15 days.
* **Mind Maps:** Build a weekly mind map connecting GCP services (e.g., how Cloud Storage connects to BigQuery, which in turn connects to BigQuery ML).
* **Teach-Back Method:** At the end of each study block, record a 3-minute audio explaining the core concept to yourself as if teaching a layperson.

### **2. Flashcards vs. Projects:**

* **Flashcards (Anki):** Storage file size limits in Cloud Storage, BigQuery-specific SQL syntax (`QUALIFY`, `ARRAY_AGG`, `STRUCT`), partition types, and service quotas.
* **Projects (GitHub):** The 3 hands-on micro-projects outlined in the weekly schedule (Ingestion Automation, Table/Cost Optimization, and BQML Model).

### **3. Fire Tests (Unassisted Practical Assessments):**

* **Fire Test 1 (End of Week 2):** Solve a simulated case study on data modeling and storage costs in 30 minutes without consulting notes.
* **Fire Test 2 (End of Week 4):** Take a full 50-question Associate Data Practitioner practice exam under real exam conditions (90-minute time limit).

---

## 5. Common Beginner Pitfalls

1. **Studying Passive Video Content Only:**
* *How to avoid:* Golden Rule — for every 1 hour of video or reading, spend 2 hours executing in the GCP Console or writing code/queries.


2. **Ignoring BigQuery Cost Management and Quotas:**
* *How to avoid:* Remember that BigQuery charges based on the volume of data scanned. Always use the `LIMIT` clause carefully (it doesn't reduce scan cost by itself!) and check the byte estimator before running queries on large datasets during study sessions.


3. **Over-focusing on Complex ML Code:**
* *How to avoid:* The *Associate Data Practitioner* exam focuses on data engineering, architecture, governance, and utilizing native tools (like BQML), rather than building complex algorithms from scratch. Keep your primary focus on infrastructure and data flows within GCP.

---
