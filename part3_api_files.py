import requests
from datetime import datetime

print("===== TASK 1 : FILE READ & WRITE =====")

notes = [
"Topic 1: Variables store data. Python is dynamically typed.",
"Topic 2: Lists are ordered and mutable.",
"Topic 3: Dictionaries store key-value pairs.",
"Topic 4: Loops automate repetitive tasks.",
"Topic 5: Exception handling prevents crashes."
]

# Write to file
with open("python_notes.txt","w",encoding="utf-8") as f:
    for line in notes:
        f.write(line+"\n")

print("File written successfully.")

# Append lines
with open("python_notes.txt","a",encoding="utf-8") as f:
    f.write("Topic 6: Functions organize reusable code.\n")
    f.write("Topic 7: APIs allow programs to communicate.\n")

print("Lines appended.")

print("\nReading file content:\n")

with open("python_notes.txt","r",encoding="utf-8") as f:
    lines = f.readlines()

for i,line in enumerate(lines,1):
    print(f"{i}. {line.strip()}")

print("Total lines:",len(lines))

keyword = input("Enter a keyword to search: ")

found=False
for line in lines:
    if keyword.lower() in line.lower():
        print(line.strip())
        found=True

if not found:
    print("No matching lines found.")



print("\n===== TASK 2 : API INTEGRATION =====")

try:
    url="https://dummyjson.com/products?limit=20"
    response=requests.get(url,timeout=5)
    data=response.json()
    products=data["products"]

    print("\nID | Title | Category | Price | Rating")
    print("----------------------------------------")

    for p in products:
        print(p["id"],"|",p["title"],"|",p["category"],"|",p["price"],"|",p["rating"])

    print("\nHigh rated products (rating >=4.5)\n")

    filtered=[p for p in products if p["rating"]>=4.5]
    filtered=sorted(filtered,key=lambda x:x["price"],reverse=True)

    for p in filtered:
        print(p["title"],"-",p["price"],"- rating:",p["rating"])

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out.")
except Exception as e:
    print("Error:",e)


print("\nSearch laptops category\n")

try:
    url="https://dummyjson.com/products/category/laptops"
    res=requests.get(url,timeout=5)
    data=res.json()

    for p in data["products"]:
        print(p["title"],"- $",p["price"])

except Exception as e:
    print("Error fetching laptops:",e)


print("\nPOST request simulation\n")

try:
    url="https://dummyjson.com/products/add"

    body={
    "title":"My Custom Product",
    "price":999,
    "category":"electronics",
    "description":"A product I created via API"
    }

    res=requests.post(url,json=body,timeout=5)
    print(res.json())

except Exception as e:
    print("POST error:",e)



print("\n===== TASK 3 : EXCEPTION HANDLING =====")

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print(safe_divide(10,2))
print(safe_divide(10,0))
print(safe_divide("ten",2))


def read_file_safe(filename):
    try:
        with open(filename,"r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))



print("\n===== TASK 4 : LOGGING =====")

def log_error(function,error):
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("error_log.txt","a") as f:
        f.write(f"[{time}] ERROR in {function}: {error}\n")


# Trigger connection error
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api",timeout=5)
except Exception as e:
    log_error("fetch_products",str(e))


# Trigger HTTP error
try:
    r=requests.get("https://dummyjson.com/products/999",timeout=5)
    if r.status_code!=200:
        log_error("lookup_product","HTTPError - 404 Not Found")
except Exception as e:
    log_error("lookup_product",str(e))


print("\nError log contents:\n")

try:
    with open("error_log.txt","r") as f:
        print(f.read())
except:
    print("Log file not found.")