student_data={"id1": {"name":"John", "age":12, "gender":"male"},
"id2": {"name":"Jane", "age":13, "gender":"female"},
"id3": {"name":"Jane", "age":13, "gender":"female"},
"id4": {"name":"Mary", "age":11, "gender":"female"}}
result={}
seen_keys=[]
for key,value in student_data.items():
    unique_key=(value["name"],value["age"],value["gender"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[key]=value
print(result)