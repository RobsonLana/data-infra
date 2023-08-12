from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.streaming import StreamingContext

def process(message):
    print('Message Received')
    print(message)
    return message

if __name__ == "__main__":
    kafka_params = {
        "kafka.bootstrap.servers": "kafka:9092",
        "group.id": "k-connect-cluster",
        "subscribe": "bitcoin_chart_topic",
        "kafkaConsumer.pollTimeoutsMs": '5000'
    }

    spark = SparkSession.builder.appName("spark_kafka_consumer")\
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2")\
        .getOrCreate()

    df = spark.readStream.format('kafka').options(**kafka_params).load()
    print(df)

    processed = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")\
        .select(col('key').cast('string'), col('value').cast('string'))

    query = processed.writeStream\
        .outputMode('append').format('console').start()

    query.awaitTermination()
