import boto3
buckettocheck=''
client = boto3.client('s3')
response = client.list_buckets()
#bucketid=response['Owner']['ID']
bucketid="" ##get the owner ID of the old account.
print(bucketid)
f=open("otheraccountDel_predev.txt","w+")
response = client.list_objects_v2(
    Bucket=buckettocheck,
    MaxKeys=3,
    Delimiter='giuseppe',
    FetchOwner=True
    
)
i=0
witherrors=0
while response['IsTruncated']:
    #print ('response' + str(response))
    for obj in response['Contents']:
        i+=1
        #print('bucketid' +bucketid)
        #print(obj['Owner']['ID'])
        if bucketid == obj['Owner']['ID']:
            #print ('response' + str(response))
            #print obj['Key']
            witherrors+=1
            f.write(obj['Key']+'\n')
    print ('total objects checked ' + str(i))
    print ('total objects with errors ' + str(witherrors))
    #print ('Key ' + str(obj['Key']+'\n'))
    response = client.list_objects_v2(
        Bucket=buckettocheck,
        MaxKeys=1000,
        Delimiter='giuseppe',
        ContinuationToken=response['NextContinuationToken'],
        FetchOwner=True
        #ExpectedBucketOwner='651425144378'
        #ExpectedBucketOwner='207709854481'
    )
f.close()
