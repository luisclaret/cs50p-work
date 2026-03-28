# File name cathegories program

file_extension = input("Filename: ").lower().strip().split(".")

# print(file_extension[-1])

if file_extension[-1] in ["gif", "png"]:
    print(f"image/{file_extension[-1]}")
elif file_extension[-1] in ["jpg", "jpeg"]:
    print(f"image/jpeg")
elif file_extension[-1] in ["pdf", "zip"]:
    print(f"application/{file_extension[-1]}")
elif file_extension[-1] == "txt":
    print("text/plain")
else:
    print("application/octet-stream")
