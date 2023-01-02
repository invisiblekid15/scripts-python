import json
import sys

if __name__ == "__main__":
    out = open('out.txt', 'w')
    out.write("<MaterialTableComponent\n")
    out.write("title=\""+sys.argv[1]+"\"\n")
    out.write("columns={[\n")
    with open('./rawData.json', "r") as f:
        data = json.loads(f.read())
        for key in data:
            out.write("{ title : \""+key+"\", field : \""+key+"\"},\n")

    out.write("]}\n");
    out.write("data={[]}\n")
    out.write("/>")

    out.close();





