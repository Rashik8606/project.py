f=open('rashik2.txt','w')
f.write('hello rashik you fine ')
f.close()

def readable(list_path):
    read = []
    f=open('rashik2.txt','r')
    for i in f:
        read.append(i.strip())
        return read
list_path = 'rashik2.txt'
data_path = readable(list_path)
print(data_path)
