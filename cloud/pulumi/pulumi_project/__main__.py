"""A Google Cloud Python Pulumi program"""

import pulumi 
from pulumi_gcp import storage

pulumi.export("x", "hello")
pulumi.export("o", {'num': 42})

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('marcelo-bucket', location="US")

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
