l1=["bhindi","aloo","chowmien"]
# i=1
# for item in 11:
#     if i%2 is not 0:
#         print(f"jarvis please buy {item}")
#         i+=1

for index, item in enumerate(l1):
    if index%2==0:
        print(f"jarvis buy{item}")