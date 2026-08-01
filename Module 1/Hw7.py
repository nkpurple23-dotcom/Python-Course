CAMERA=1   # 0001
MICROPHONE=2   # 0010
STORAGE=3  # 0011
LOCATION=4  # 0100
approved_apps = ["history app","english app","science app","math app"]
restricted_apps=["gaming app","shopping app","social media app"]
name = input("Enter your name: ")
wanted_app = input("Enter the app you want to access from the available apps: ").lower()
if type(name) is str:
    print("Is string")
if type(wanted_app) is not int:
    print("Not a number")
if wanted_app in approved_apps:
    print(f"{wanted_app} is an approved app.")
elif wanted_app in restricted_apps:
    print(f"{wanted_app} is an restricted app.")
else:
    print(f"{wanted_app} is not part of the available apps list.")
if wanted_app not in restricted_apps:
    print("This app is not in the restricted list.")
else:
    print("This app is restricted.")
permissions = CAMERA|MICROPHONE|STORAGE
print(f"Permission bits: {bin(permissions)}")
if permissions&CAMERA:
    print("Camera enabled")
else:
    print("Camera disabled")
if permissions&MICROPHONE:
    print("Microphone enabled")
else:
    print("Microphone disabled")
if permissions&STORAGE:
    print("Storage enabled")
else:
    print("Storage disabled")
if permissions&LOCATION:
    print("Location enabled")
else:
    print("Location disabled")
print(f"Camera bit: {bin(CAMERA)}")
print(f"After left shift: {bin(CAMERA<<1)}")
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(STORAGE>>1))
if wanted_app in approved_apps and wanted_app not in restricted_apps:
    print(f"Access granted to {wanted_app}")
else:
    print(f"Access denied to {wanted_app}")
