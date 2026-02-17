# def arg(name,greet):
#     print("Good day ," + name )
#     print(greet)

# arg("Aryan" ,"Thank YOU ")
# arg("Ankit" ,"Thank YOU ")
# arg("Aman" ,"Thanks")



#default argument
def arg(name,ending="Thank You"):  #here we set ending as default
    print(f"Good day , {name}")
    print(ending)

arg("Aryan" )