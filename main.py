import ner

entity = []
for i in range(1, 15):
    file = open("data/" + str(i) + ".txt", "r")
    string = ner.remove_non_ascii(file.read())
    names = ner.extract_names(string)
    names = list(set(names))
    entity.append(names)

graph = []
label = {}
temp = {}
for item in entity:
    for i in item:
        for j in item:
            if i != j:
                val = (i, j)
                if temp.has_key(val):
                    temp[val] = temp[val] + 1
                    if temp[val] > 2:
                        label[val] = temp[val]
                        graph.append(val)
                else:
                    temp[val] = 1

ner.draw_graph(graph, label)