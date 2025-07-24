import sys

def cleanup():
    global key
    global val
    global new
    global num
    global fff
    key = ""
    val = ""
    new = ""
    fff = ""
    num = 0
    
def varcheck(val):
    vkey = ""
    vval = ""
    j = 0
    if "*" in val: #+0/*0-0*:
        val = val[val.index("*")+1:]
        while val[j] != "-":
            vkey += val[j]
            j += 1
        j += 1
        while val[j] != "*":
            vval += val[j]
            j += 1
        if vkey == "i": #trying to make iterator with varcheck, *i-0* means iteration of loop with id zero, good luck soldier
            return loops[vval][0] #nice job soldier
        elif vkey == "_":
            return len(vars[vval])
        return vars[vkey][int(vval)]
    else:
        return val
    
def ifcheck(line, iid):
    idc = ""
    for j in range(len(line)):
        if line[j] == "}":
            j += 1
            while line[j] != "/":
                idc += line[j]
                j += 1
            if idc == iid:
                return j
                
vars = {}
cmd = ""
i = 0

key = ""
val = ""
new = ""
fff = ""
num = 0

vkey = ""
vval = ""
j = 0

loops = {}
rid = "" #id of loop
rval = "" #amount of times loop repeats
rp = 0 #place loop starts

prstr = "" #printed string

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
                if not val.isdigit(): #add numeric values of string to integer if val is a string
                    for n in range(len(val)):
                        vars[key].append(ord(val[n]))
                else:
                    vars[key].append(int(val))
                cleanup()
                
            if cmd == "~": #~0/1/0/
                i += 1
                while line[i] != "/":
                    key += line[i]
                    i += 1
                key = varcheck(key)
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
                
            if cmd == "." or cmd == "," or cmd == "!" or cmd == "\\": #printing
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                if cmd == ".":
                    print(val, end="")
                elif cmd == ",":
                    print(chr(int(val)), end="")
                elif cmd == "\\":
                    print(vars[val], end="")
                elif cmd == "!":
                    for x in range(len(vars[val])):
                        prstr += chr(int(vars[val][x]))
                    print(prstr, end="")
                    prstr = ""
                cleanup()
                
            if cmd == "@":
                i += 1
                while line[i] != "/":
                    key += line[i]
                    i += 1
                key = varcheck(key)
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                num = int(input("Enter number:"))
                vars[key][int(val)] = num
                cleanup()
                
            if cmd == ":":
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
                    
            if cmd == "a" or cmd == "s" or cmd == "d" or cmd == "x" or cmd == "m": #a[key]/[index]/[num1]/[num2]/ Add Subtract Divide multiply (X) Modulo
                i += 1
                while line[i] != "/": 
                    key += line[i]
                    i += 1
                key = varcheck(key)
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
                while line[i] != "/":
                    fff += line[i]
                    i += 1
                fff = varcheck(fff)
                if cmd == "a":
                    vars[key][int(val)] = int(new) + int(fff)
                if cmd == "s":
                    vars[key][int(val)] = int(new) - int(fff)
                if cmd == "d":
                    vars[key][int(val)] = round(int(new) / int(fff)) #decimals? in MY integer-based esolang?
                if cmd == "x":
                    vars[key][int(val)] = int(new) * int(fff)
                if cmd == "m":
                    vars[key][int(val)] = int(new) % int(fff)
                cleanup()
                
            if cmd == ">" or cmd == "<" or cmd == "=": #>*0-0*/5/[id]: if key 0 index 0 is larger than 5, continue. if else, go to the } block at the id specified. can also be used as an odd goto/break
                i += 1
                while line[i] != "/": 
                    key += line[i]
                    i += 1
                key = varcheck(key)
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                i += 1
                while line[i] != "/":
                    new += line[i]
                    i += 1
                if cmd == ">" and int(key) > int(val):
                    cleanup()
                elif cmd == "<" and int(key) < int(val):
                    cleanup()
                elif cmd == "=" and int(key) == int(val):
                    cleanup()
                else:
                    i = ifcheck(line, new)
                    cleanup()
                    
            if cmd == "$":
                i += 1
                while line[i] != "/":
                    key += line[i]
                    i += 1
                key = varcheck(key)
                i += 1
                while line[i] != "/":
                    val += line[i]
                    i += 1
                val = varcheck(val)
                vars[key].pop(int(val))
                cleanup()
                
            if cmd == "n":
                i += 1
                print("")
                
            if cmd == "[":
                i += 1
                while line[i] != "/": 
                    key += line[i]
                    i += 1
                key = varcheck(key)
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
                while line[i] != "/":
                    fff += line[i]
                    i += 1
                fff = varcheck(fff)
                for h in range(len(vars[key][int(new):int(fff)])): #add the new items one at a time, rather than in their own list
                    vars[val].append(vars[key][int(new)+h])
                cleanup()
                
            else:
                i += 1
