
from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("mergecheck") \
    .getOrCreate()

# Read a CSV file into a DataFrame
#df1 = spark.read.csv("/Users/prabhakarbalaram/Downloads/xfly analysis(NEW CHANGES ).csv", header=True, inferSchema=True)

# Show the DataFrame
#df1.show()

# Read a CSV file into a DataFrame
df2 = spark.read.csv("/Users/prabhakarbalaram/Downloads/xfly analysis(NEW CHANGES ).csv", header=True, inferSchema=True)

# Show the DataFrame
df2.show()

#dicl= df1.to_dict()
#print(dicl)

df3=df2.apply(' '.join).str.replace('[^A-Za-z\s]+', '') \
           .str.split(expand=False)
df3.count()


