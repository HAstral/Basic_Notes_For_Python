# x=dict();
# x["key"]="value";
# print(x);
# x["name"]="spaon";
# print(x["name"]);
# y={"name":"Aye",
#    "age":21};
# print(y);
# print(y.values())
# z=x.copy();

# x.clear();
# print(x);
# print(z);
# print(z.get("key"));
# print(y.items());
# print(y.keys());
# x.pop("key");
# # print(x);
# x.update("gender":"male")
# print(x)
capital={"India":"New Delhi",
         "USA":"Washington D.C.",
         "UK":"London",
         "France":"Paris"}
#print(dir(capital))
#print(help(capital))
# print(capital.get("UK"))

# if capital.get("UK"):
#     print("That country exists")
# else:
#     print("That country does not exist")
capital.update({"Germany":"Berlin"})
capital.update({"China":"Beijing"})
# key=capital.keys()
# print(key)
# for key in capital.keys():
#     print(key,end=" | ")
values=capital.values()
print(values)