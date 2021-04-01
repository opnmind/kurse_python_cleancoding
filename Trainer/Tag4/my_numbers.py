with open("/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log") as fd:
    for line in fd: # fd als Iterator
        if "127.0.0.1" in line:
            print(line)


def my_numbers(start_value, max_value):
    value = start_value
    while value < max_value:
        print("-->", value)
        yield value #<- hier zeigt es sich als Generator! yield != return vom Verhalten her!
        value += 1



for number in my_numbers(10, 20): # Listenkontext, d.h. der generator gibt elemnt für Elemnt bei jedem Aufruf
    print(number)

print(list(my_numbers(10,20))) # Erzeugt durch mehrfachen internen aufruf die Liste