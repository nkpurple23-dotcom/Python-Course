student_data={"id1":{"name":"Jane","score":69},
"id2":{"name":"Mary","score":90},
"id3":{"name":"June","score":87},
"id4":{"name":"John","score":50},
"id5":{"name":"Bob","score":26}}
for key,value in student_data.items():
    sum+=value["score"]
avg=sum/5
print(max(student_data)
student_data.get("id1","Not Found")