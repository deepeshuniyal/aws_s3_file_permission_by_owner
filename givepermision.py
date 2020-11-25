import boto3
buckettocheck=''
client = boto3.client('s3')
file = open("otheraccountDel_prod.txt", "r")
i=0
skipped=0
for line in file:
    try:
      i+=1
      print(str(i))
      #print('line ::'+str(line))
      key=str(line)
      #key=line.encode('utf-8') #if you don't do this you can have erros for some type of chars
      key=key[:-1] #this is to remove the cariage return char to the string
      print('key ::'+str(key))
      response = client.put_object_acl(
          ACL='bucket-owner-full-control',
          Bucket=buckettocheck,
          Key=key,
      )
    except Exception as ex:
      print(ex)
      skipped+=1
      print(str('skipped:'+str(skipped)))
print(str('total file analized ' +str(i)))
print(str('total file skipped ' +str(skipped)))
file.close()

