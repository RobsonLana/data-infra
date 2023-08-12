# Data engineering ETL infrastructure

This is a experimentation project, targeting the learning of the recurrent technologies used on data consumption and pipeline development.

## Technologies used

- Docker / compose
- Zookeeper
- Cassandra
- Kafka / Connect
- Spark

The main goal of this project is to make available a template of a local ETL infrastructure to be used in any possible way and exercise the usage of such tools.

The first draft of this project used Bitnami images to realize the tasks of data consumption, but since there was too many roadblocks to make the shcema registry work, I've decided to change to Confluent images, which has a easier setup since the schema registry is also available by them.

## Future Goals of the project

The main branch of the repository will come with a simple ETL designed for a dataset available at [Kaggle: Bitcoin History Kandle Lines](https://www.kaggle.com/datasets/jesusgraterol/bitcoin-hist-klines-all-intervals-2017-2023?resource=download). But other branches / versions of the same project for other kinds of datasets will be available to demonstrate more possibilites and business rules to be used.

For now, some tweaks involving directory writting permissions to the containers is necessary, and the automatic connection publishing is also pending. But the basic functionality is reached, and more quality of life improvements wil be implemented.

## To be done

- Spark consumer
- Ideas for further datalake layers
- Reduce the project's structure and management
