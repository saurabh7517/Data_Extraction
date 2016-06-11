from bs4 import BeautifulSoup
from collections import defaultdict



#Extracting data from first Line(store name, street address)
def first_line(f_line):
    first_line_list = list()
    left_strip = f_line.strip().lstrip('"')
    soup = BeautifulSoup(left_strip, "lxml")
    tag1 = soup.h5
    # print tag1.string
    first_line_list.append(tag1.string)
    for tag2 in soup.find_all("span"):
        first_line_list.append(tag2.string)
        # print tag2.string
    return first_line_list

#Extracting data from second line(state,country)
def second_line(s_line):
    second_line_list = list()
    soup = BeautifulSoup(s_line,"lxml")
    tag = soup.span
    second_line_list.append(tag.string)
    # print tag.string
    return second_line_list

#Extracting data from third line(pin code, phone)
def third_line(t_line):
    third_line_list = list()
    soup = BeautifulSoup(t_line,"lxml")
    tag = soup.span
    third_line_list.append(tag.string)
    # print tag.string
    for tag2 in soup.find_all("br"):
        third_line_list.append(tag2.next_sibling.string)
        # print tag2.next_sibling.string
    # print third_line_list
    return third_line_list

#Writing data to file and using defaultdict as input parameter
def writeDoc(key_val_dict):
    try:
        fname = open("C:\Users\saurabh\Desktop\_temp.txt", "a")
        for k in key_val_dict:
            print k
            print "\n" + "\n"
            fname.write(k)
            for v in key_val_dict[k]:
                fname.write("\n")
                try:
                    fname.write(v[0] + "\n")
                except:
                    print "0 missing"
                try:
                    fname.write(v[1] + "\n")
                except:
                    print "1 missing"
                try:
                    fname.write(v[2])
                except:
                    print "2 Missing"
                fname.write(",")
                try:
                    fname.write(v[3])
                except:
                    print "3 missing"
                fname.write(",")
                try:
                    fname.write(v[4])
                except:
                    print "4 missing"
                fname.write("\n")
                try:
                    fname.write(v[5] + "\n")
                except:
                    print "5 missing"
                try:
                    fname.write(v[6] + "\n")
                except:
                    print "6 Missing"
                fname.write("\n")
    except IOError as e:
        print e
        print "File cannot be opened"
        fname.close()



#Adding every address into defaultdict and then returning it
def createDict(address_list,defdict):
    defdict[address_list[3]].append(address_list)
    return defdict



#Just for checking the data at Console
def display_items(key_val_dict):
    for k in key_val_dict:
        print k
        for v in key_val_dict[k]:
            print v

            # print v[0]
            # print v[1]
            # print v[2]
            # try:
            #     print v[3]
            # except:
            #     print "3 missing"
            # try:
            #     print v[4]
            # except:
            #     print "4 missing"
            # try :
            #     print v[5]
            # except:
            #     print "5 missing"
            #
            #
            #
            # try:
            #     print v[6]
            # except:
            #     print "6 Missing"









count = 0
inserts = 0
try:
    fname = open('.\store.txt', 'r')
    address = list()
    key_val = defaultdict(list)
    for line in fname:
        new_line = line.lstrip("\t")
        if (new_line.startswith('marker_' + str(count) + '.set')):
            search_us = new_line.find(">US<")
            if(search_us > 0):
                filter_text = new_line.split(",")
                address.extend(first_line(filter_text[1]))
                address.extend(second_line(filter_text[2]))
                stripped_third_string = filter_text[3].strip().rstrip('<br>");')
                address.extend(third_line(stripped_third_string))
                # print address
                key_val = createDict(address,key_val)

                address = []
                inserts = inserts + 1
            count = count + 1
            # print count
    # writeDoc(key_val)       #Writing data to file
    # display_items(key_val)
    print inserts #Counting the number of US entries entered into defaultdict

except IOError as e:
    print e
