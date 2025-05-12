import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])



print(sys.version)
print(sys.version_info)

print(sys.path) #Specfies the search path for modules

print(sys.platform) #Platform identifier

sys.stdout.write("This is stdout\n")
sys.stderr.write("This is stderr\n")

print(sys.maxsize) #Maximum size of a list



print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
sys.exit(0)  # Clean exit
