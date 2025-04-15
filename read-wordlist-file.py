

# FUNCTION
def read_list(file_path):
    content = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cont = line.strip()
                if cont:
                    content.append(cont)
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
    except Exception as e:
        print(f"[!] Error reading the file: {e}")
    return content

# ARRAY (treat the function as an array)
contents = read_list("content_list.txt")

# USE
for cont in contents:
  # code here......
