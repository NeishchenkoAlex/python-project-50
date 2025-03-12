# data={
#   "common": {
#     "setting1": "Value 1",
#     "setting2": 200,
#     "setting3": True,
#     "setting6": {
#       "key": "value",
#       "doge": {
#         "wow": ""
#       }
#     }
#   },
#   "group1": {
#     "baz": "bas",
#     "foo": "bar",
#     "nest": {
#       "key": "value"
#     }
#   },
#   "group2": {
#     "abc": 12345,
#     "deep": {
#       "id": 45
#     }
#   }
# }


# def obxod(data,target,depht=1):
    
#     result=[]
    
#     for key,item in data.items():
#         if isinstance(item, dict):
#             result.append(f'директория{depht} не содержит значение{target}')
#             result.append(obxod(item, target,depht+1))
#         elif item==target:
#             result.append(f"{key} имеет уровень{depht}")
#     return result
    

# print(obxod(data,45))









