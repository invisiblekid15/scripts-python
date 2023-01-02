import json
import sys

if __name__ == "__main__":
    out = open('out.txt', 'w')
    out.write("<MaterialTableComponent\n")
    out.write("title=\""+sys.argv[1]+"\"\n")
    out.write("columns={[\n")
    with open('./rawData.txt', "r") as f:
        data = f.readlines()
        for key in data:
            out.write("{ title : \""+str(key).split()[0]+"\", field : \""+str(key).split()[0]+"\"},\n")

    out.write("]}\n");
    out.write("data={[]}\n")
    out.write("/>")

    out.close();





