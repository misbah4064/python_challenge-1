import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
# while True:
# 	print kernel.respond(raw_input("Enter your message >> "))
print("Say: Hello ")
while True:
    input_text = input("> ")
    response = kernel.respond(input_text)
    print(response)