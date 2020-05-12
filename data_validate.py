import boto3
from itertools import groupby
from operator import itemgetter
import pandas as pd

_BUCKET_NAME = ''
_PREFIX = ''

client = boto3.client('s3', aws_access_key_id="****",aws_secret_access_key="****")

content = []

paginator = client.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket=_BUCKET_NAME, Prefix=_PREFIX)

for page in page_iterator:
	for object in page['Contents']:
		key = object['Key']
		size = object['Size']
		date = object ['LastModified']
		content = content + [(key,size,date)]

df = pd.DataFrame(content,columns=['fileName', 'size', 'date'])

# key_mapped = list(map(lambda x:(x[:x.rfind("/")+1],x[x.rfind("/")+1:]), content))
# key_grouped = [(k, list(list(zip(*v))[1])) for k, v in groupby(key_mapped, itemgetter(0))]
# key_filtered = list(filter(lambda x: '_SUCCESS' not in x[1], key_grouped))

# non_success_file_path = list(map(lambda x : x[0],key_filtered))
# success_file_path = list(filter(lambda x: '_SUCCESS' in x[1], key_grouped))[0][0]

# file_name = "_SUCCESS"

# Commenting the line , since it may copy and can be dangerous
# copy_files = map(lambda x : client.copy_object(copy_source,"tivo-session-store","/users/sanni/data/"),non_success_file_path)