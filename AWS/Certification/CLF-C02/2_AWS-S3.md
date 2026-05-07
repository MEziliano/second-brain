# [AWS] - CLF-C02 - Cloud Practitioner

# S3 

One of the services provided by AWS in Cloud. Is a HD in cloud. It is able to upload several types of files, such as .docx, .xsls, ... you pay as you go. 
You can think in S3 like a closet and there are many drawer. Like you can create folder in you computer, they decide to put bucket to be different.

When creat a bucket there are two options: 
* General purporse - recommended to most of use cases 
* Directory - recommended for low-latency, such as a game. for example.


```mermaid
graph LR
    subgraph Region ["REGIONS (US-EAST-1)"]
        direction LR

        subgraph AZ1 ["AZ 1"]
            direction TB
            PoP["PoPs"]:::greenBox
            Edge["EDGE
            LOCATIONS"]:::greenBox
        end

        subgraph AZ2 ["AZ 2"]
            direction TB
            Empty2[" "]:::invisible
        end

        subgraph AZ3 ["AZ 3"]
            direction TB
            Empty3[" "]:::invisible
        end
    end

    %% Aplicação de Estilos
    class Region regionStyle
    class AZ1,AZ2,AZ3 azStyle
    classDef invisible display:none;

    %% Forçar alinhamento horizontal conectando invisivelmente
    AZ1 ~~~ AZ2 ~~~ AZ3
```

## S3 Storage Classes

[Docs](https://aws.amazon.com/s3/storage-classes/)

| Storage Class                 | Use Case                     | Durability    | Availability | Retrieval Time | Price |
| ----------------------------- | ---------------------------- | ------------- | ------------ | -------------- | ----- |
| S3 Standard                   | General purpose              | 99.999999999% | 99.99%       | Milliseconds   | $$    |
| S3 Intelligent-Tiering        | Variable access patterns     | 99.999999999% | 99.9%        | Milliseconds   | $$    |
| S3 Standard-IA                | Infrequent access            | 99.999999999% | 99.9%        | Milliseconds   | $     |
| S3 One Zone-IA                | Infrequent access, single AZ | 99.999999999% | 99.5%        | Milliseconds   | $     |
| S3 Glacier Instant Retrieval  | Archival, infrequent access  | 99.999999999% | 99.9%        | Milliseconds   | $     |
| S3 Glacier Flexible Retrieval | Archival, flexible retrieval | 99.999999999% | 99.9%        | Minutes        | $     |
| S3 Glacier Deep Archive       | Archival, long-term          | 99.999999999% | 99.9%        | Hours          | $     |

> Amazon S3 offers several storage classes designed for different data access patterns, performance needs, and cost-optimization goals. Key classes include S3 Standard (frequent access), S3 Intelligent-Tiering (automatic savings), S3 Standard-IA/One Zone-IA (infrequent access), and S3 Glacier (archive) options, all offering high durability.

### Key Amazon S3 Storage Classes:
* **S3 Standard**: Designed for frequently accessed data, providing high throughput and low latency. Ideal for cloud apps, websites, and content distribution.
* **S3 Intelligent-Tiering**: Automatically optimizes costs by moving data between frequent and infrequent access tiers based on changing patterns without operational overhead.
* **S3 Standard-Infrequent Access (S3 Standard-IA)**: Suitable for data accessed less frequently but requiring rapid access when needed, at a lower storage price than S3 Standard.
* **S3 One Zone-Infrequent Access (S3 One Zone-IA)**: Similar to S3 Standard-IA, but stores data in a single Availability Zone, making it 20% lower cost, ideal for re-creatable, non-critical data.
* **S3 Glacier Instant Retrieval**: Archive storage for data accessed rarely, yet requiring millisecond retrieval.
* **S3 Glacier Flexible Retrieval**: Replaced S3 Glacier, supporting data archiving with retrieval times from minutes to hours.
* **S3 Glacier Deep Archive**: Lowest-cost storage class, designed for data that is rarely accessed, with retrieval times within hours.
* **S3 Express One Zone** : High-performance storage class for frequently accessed data, providing the lowest latency.

### Key Considerations
* **Durability**: All S3 storage classes (except S3 One Zone-IA) store data across multiple, geographically separated Availability Zones to ensure 99.999999999% durability.
* **Minimum Storage Duration**: IA and Glacier classes have minimum storage duration charges (e.g., 30 days for IA, 90-180 days for Glacier).
* **Lifecycle Policies**: You can use Lifecycle rules to automatically transition objects between storage classes to reduce costs as data ages

---
| **Key Words**      |    **Content**        | 
| ------------------ |                  ---------- | 
| Data access patterns <br> Performance needs <br> Cost-optimization|  **Classes:** <br> S3 Standard <br> S3 Intelligent-Tiering <br> Standard IA <br> S3 Glacier                  | 
|                                                                    |                            | 

> 

<h3><details><summary> Diagram view</summary>



```mermaid
graph LR
    root[<b>Amazon S3 Storage Classes</b>]

    %% Main Categories
    subgraph Frequent_Access [<b>Frequent Access / High Performance</b>]
        direction LR
        Standard[<b>S3 Standard</b><br/>General purpose, apps, websites]
        Express[<b>S3 Express One Zone</b><br/>Lowest latency<br/>Single AZ]
    end

    subgraph Intelligent [<b>Automatic Optimization</b>]
        IntelligentTiering[<b>S3 Intelligent-Tiering</b><br/>Automatically moves data<br/>No operational overhead]
    end

    subgraph Infrequent_Access [<b>Infrequent Access IA</b>]
        direction LR
        StandardIA[<b>S3 Standard-IA</b><br/>Rapid access when needed<br/>Multi-AZ]
        OneZoneIA[<b>S3 One Zone-IA</b><br/>cheaper<br/>Single AZ<br/>Recreatable data]
    end

    subgraph Archive [<b>Glacier Archiving</b>]
        direction LR
        GlacierInstant[<b>Glacier Instant Retrieval</b><br/>Millisecond retrieval]
        GlacierFlexible[<b>Glacier Flexible Retrieval</b><br/>Minutes to hours<br/>Replaced standard S3 Glacier]
        GlacierDeep[<b>Glacier Deep Archive</b><br/>Lowest cost<br/>Hours to retrieve]
    end

    %% Connections
    root --> Frequent_Access
    root --> Intelligent
    root --> Infrequent_Access
    root --> Archive

    Standard 
    Express 
    IntelligentTiering 
    OneZoneIA 
    GlacierInstant 
    GlacierFlexible 
    GlacierDeep 

    %% Key Considerations (Floating notes or connected)
    note1["<b>⚠️ Durability</b><br/>99.999999999%<br/>Except One Zone-IA"]
    note2["<b>⏳ Min Duration</b><br/>IA: 30 days<br/>Glacier: 90-180 days"]
    note3["<b>🔄 Lifecycle</b><br/>Auto transition<br/>to reduce costs"]

    root -.-> note1
    note1 -.-> note2
    note2 -.-> note3

    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef frequent fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef intelligent fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef infrequent fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef archive fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef notes fill:#ffebee,stroke:#c62828,stroke-width:2px,stroke-dasharray: 5 5;

    class note1,note2,note3 notes;
    class Standard,Express frequent;
    class IntelligentTiering intelligent;
    class StandardIA,OneZoneIA infrequent;
    class GlacierInstant,GlacierFlexible,GlacierDeep archive;
``` 
<details></h3>

```mermaid
flowchart LR


    A[Amazon S3 Storage Classes]  --> B[Standard] 
    A --> C[Express]
    A --> D[IntelligentTiering]
    A --> E[StandardIA]
    A --> F[OneZoneIA]
    A --> G[Glacier Instant]
    

    G --> H[GlacierInstant]
    G --> I[GlacierFelixble]
    G --> J[Glacier Deep]
``` 