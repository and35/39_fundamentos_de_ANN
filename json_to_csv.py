import pandas as pd
print("el archivo json debe estar en el actual directorio")
json_file = str(input("dame el nombre del archivo json: "))
df = pd.read_json (json_file)
df.to_csv(f"{json_file.strip('.json')}.csv", index = None)
print("listo!!!")