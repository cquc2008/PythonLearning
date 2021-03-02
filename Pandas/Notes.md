# Words
  + scenario -- a discription of possible actions or events in the future
  + ingestion -- *[noun.]* the process of taking food, drugs,etc. into your body, usually by swallowing
    - ingest -- *[verb.]* to taking food, drugs, etc. into your body, usually by swallowing.
  + architecture -- the design and structure of a computer system,which controls what equipment can be connected to it and what software can operate on it
  + category -- (in a system for dividing things according to appearance, quality, etc.) a type, or a group of things having some features that are the same
  + accommodate -- *verb.* to provide with a place to live or to be stored in
  + anomaly -- *noun.* a person or thing that is different from what is usual, or not in agreement with something else and therefore not satisfactory
  + batch -- *noun.* a group of things or people dealt with at the same time or considered similar in type
  + spark -- *noun.* a very small piece of fire that flies out from something that is burning, or one that is made by rubbing two hard things together, or a flash or light made by electricity; 
  + distinct -- *adj.* clearly separate and different

# ingest
ingestion is a set of software engineering techniques to adapt high volumes of data that arrive rapidly (often via streaming)
  + Kafka
  + RabbitMQ
  + Fluentd
  + Sqoop
  + Kinesis(AWS)
# Model
Modelling is a set of data architecture techniques to create data storage that is appropriate for a particular domain.
  + Relational
    - MySQL
    - Postgres
    - RDS(AWS)
  + Key Value
    - Redis
    - Riak
    - DynamoDB(AWS)
  + Columnar
    - Casandra
    - HBase
    - RedShift(AWS)
  + Document
    - MongoDB
    - ElasticSearch
    - CouchBase
  + Graph
    - Neo4J
    - OrientDB
    - ArangoDB
# Query
Query refers to extracting data(from storage) and modifying that data to accommodate anomalies such as missing data.
  + Batch
     - MapReduce
     - Spark
     - Elastic MapReduce(AWS)
  + Batch SQL
     - Hive
     - Presto
     - Drill
    + Streaming
     - Storm
     - Spark Streaming
     - Samza
