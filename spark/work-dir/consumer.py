from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.avro.functions import from_avro
from pyspark.sql.types import StructType, StructField, TimestampType, FloatType
from pyspark.streaming import StreamingContext

table_schema = StructType([
    StructField('ot', TimestampType()),
    StructField('ct', TimestampType()),
    StructField('o', FloatType()),
    StructField('h', FloatType()),
    StructField('l', FloatType()),
    StructField('c', FloatType()),
    StructField('v', FloatType()),
])

avro_schema = """
{
    "type": "record",
    "name": "kandles",
    "fields": [
        { "name": "ot", "type": { "type": "long", "logicalType": "timestamp-millis" } },
        { "name": "ct", "type": { "type": "long", "logicalType": "timestamp-millis" } },
        { "name": "o", "type": "float" },
        { "name": "h", "type": "float" },
        { "name": "l", "type": "float" },
        { "name": "c", "type": "float" },
        { "name": "v", "type": "float" }
    ]
}
"""

kafka_params = {
    "kafka.bootstrap.servers": "kafka:9092",
    "group.id": "k-connect-cluster",
    "subscribe": "bitcoin_chart_topic",
    "kafkaConsumer.pollTimeoutsMs": '5000',
    "startingOffsets": "earliest"
}

if __name__ == "__main__":

    spark = SparkSession.builder\
        .appName("spark_kafka_consumer")\
        .getOrCreate()

    df = spark.readStream\
        .format('kafka')\
        .options(**kafka_params).load()

    price_kandle = df.select(from_avro(col("value"), avro_schema).alias("data"))\
        .select('data.*')

    price_kandle.writeStream\
        .format("console")\
        .outputMode("append")\
        .option("truncate", False)\
        .start()\
        .awaitTermination()

    print('Loaded Streaming')
