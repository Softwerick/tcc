import json

json_obj = {}
json_obj['data'] = []

for x in range(1000):
    json_obj['data'].append({
        'name': 'teste' + str(x),
        'age': x,
        'occupation': 'developer' + str(x),
        'id': '12345678910',
        'telNumber': '47999999999'
    })
      

# Directly from dictionary
with open('data.json', 'w') as outfile:
    json.dump(json_obj, outfile)
  
# # Using a JSON string
# with open('data.json', 'w') as outfile:
#     outfile.write(json_string)prom