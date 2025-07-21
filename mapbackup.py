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
    if "*" in val: #+0/*0/0*:
        print(val)
        val = val[val.index("*")+1:]
        while val[j] != "-":
            vkey += val[j]
            j += 1
        j += 1
        while val[j] != "*":
            vval += val[j]
            j += 1
        if vkey == "i": #trying to make iterator with varcheck, *i-0* means iteration of loop with id zero, good luck soldier
            return loops[vval][0]
        return vars[vkey][int(vval)]
    else:
        return val
    
vars = {}
loops = {}
cmd = ""
i = 0

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
        while i < len(line):
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
                vars[key].append(int(val))
                cleanup()
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
                vars[key][int(val)] = int(new)
                cleanup()
            if cmd == "." or cmd == ",":
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                if cmd == ".":
                    print(val)
                elif cmd == ",":
                    print(chr(int(val)))
                cleanup()
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
                num = int(input("Enter number:"))
                vars[key][int(val)] = num
                cleanup()
            if cmd == ":": #this is for repeat, make it like :0/5/, where it repeats 5 times with an ID (rid) of zero, then the end of the loop is ::0::
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
                    cleanup()
            else:
                i += 1
            print(loops)
            print(vars)
