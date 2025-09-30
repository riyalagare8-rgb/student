# Define student details using a dictionary
student = {
    "Name": "riya lagare",
    "Age": 20,
    "Roll Number": "022",
    "Branch": "bca",
    "College": "kle tech",
    "phone no": "1234567890",
    "grade": "a"
}

# Print student details
print("📘 Student Details:")
print("-------------------")
for key, value in student.items():
    print(f"{key}: {value}")