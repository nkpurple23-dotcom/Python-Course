student_data={"id1":{"name":"Bob","grade":1,"age":5},
"id2":{"name":"Jack","grade":4,"age":9},
"id3":{"name":"Emily","grade":5,"age":11},
"id4":{"name":"Jack","grade":4,"age":9}}
print(student_data)
student_data.get("id1","Not found")
student_data.get("id5","Not found")
student_data["id5"]={"name":"Katie","grade":6,"age":12}
print(student_data)
student_data.update({"id2":{"name":"George","grade":"4","age":"9"}})
cleaned_data={}
seen_records=[]
for key,value in student_data.items():
    unique_key=(value["name"],value["grade"],value["age"])
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[key]=value
student_data.pop("id4")
len(student_data)
for student_id,details in student_data.items():
    print(student_id,":", details)