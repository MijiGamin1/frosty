import sys
def cleanup():
    global key
    global val
    global new
    global num
    key = ""
    val = ""
    new = ""
    num = 0
    
def varcheck(val):
    vkey = ""
    vval = ""
    j = 0
    if val[0] == "*": #+0/*0/0*:
        val = val[1:]
        while val[j] != "-":
            vkey += val[j]
            j += 1
        j += 1
        while val[j] != "*":
            vval += val[j]
            j += 1
        return vars[vkey][int(vval)]
    else:
        return val
    
vars = {}
loops = {}
cmd = ""

key = ""
val = ""
new = ""
num = 0

vkey = ""
vval = ""
j = 0

rid = "" #id of loop
rval = "" #amount of times loop repeats
rp = 0 #place loop starts


text = input("File: ")

with open(text, 'r') as file:
    for line in file:
        for i in range(len(line)):
            cmd = line[i]
            if cmd == "+":
                i += 1
                while line[i] != "/":
                    key += line[i]
                    i += 1
                    if not key in vars:
                        vars[key] = []
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                i += 1
                vars[key].append(int(val))
                cleanup()
                i += 2
            if cmd == "~": #~0/1/0/
                i += 1
                while line[i] != "/":
                    key += line[i]
                    i += 1
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                i += 1
                while line[i] != "/":
                    new += line[i]
                    i += 1
                new = varcheck(new)
                i += 1
                vars[key][int(val)] = int(new)
                cleanup()
                i += 2
            if cmd == "." or cmd == ",":
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                i += 1
                if cmd == ".":
                    print(val)
                elif cmd == ",":
                    print(chr(int(val)))
                cleanup()
                i += 2
            if cmd == "@":
                i += 1
                while line[i] != "/":
                    key += line[i]
                    i += 1
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                i += 1
                num = int(input("Enter number:"))
                vars[key][int(val)] = num
                cleanup()
                i += 2
            if cmd == ":": #this is for repeat, make it like :0/5:, where it repeats 5 times with an ID (rid) of zero, then the end of the loop is ::0::
                i += 1
                while line[i] != "/":
                    rid += line[i]
                    i += 1
                if rid not in loops:
                    loops[rid] = []
                i += 1
                while line[i] != "/":
                    rval += line[i]
                    i += 1
                rval = varcheck(rval)
                loops[rid].append(int(rval))
                i += 2
                if rp == 0:
                    rp = i
                    loops[rid].append(int(rp))
                rid = ""
                rval = ""
                rp = 0
                cleanup()
            if cmd == "#": 
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                if loops[val][0] != 0:
                    loops[val][0] -= 1
                    i = loops[val][1] 
                else:
                    i += 2
                cleanup()
            print(i)
            print(loops)
            print(vars)
