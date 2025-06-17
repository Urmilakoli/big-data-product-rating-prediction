from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline

# Assuming data is already loaded and preprocessed
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
rf = RandomForestClassifier(labelCol="rating", featuresCol="features")
pipeline = Pipeline(stages=[assembler, rf])

model = pipeline.fit(training_data)
predictions = model.transform(test_data)
predictions.select("prediction", "rating").show()
