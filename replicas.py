f = open("roles.txt", encoding="utf-8")

actors = []
for li in f:
    if "textlines" not in li.lower():
        actors.append(li.rstrip("\n").replace(".", ""))
    else:
        break
del(actors[0])

actors_and_texts = {a: [] for a in actors}

current_actor = ""
first_line = f.readline()
first_line = first_line.rstrip()
if ":" in first_line:
    current_actor = first_line[:first_line.index(":")]
    actors_and_texts[current_actor].append([first_line.replace(first_line[:first_line.index(":") + 2], "")])

role_text = []
for j in f:
    j = j.rstrip("\n")
    if ":" in j:
        if j[:j.index(":")] in actors and j[:j.index(":")] != current_actor:
            actors_and_texts[current_actor].append(role_text)
            new_actor = j[:j.index(":")]
            current_actor = new_actor
            role_text = [j.replace(j[:j.index(":") + 2], "")]
        else:
            role_text.append(j)
    else:
        role_text.append(j)

for val in actors_and_texts.values():
    for i in val:
        if not any(i):
            val.remove(i)

for k, v in actors_and_texts.items():
    print(f"{k}")
    for num, el in enumerate(v):
        print(f"{num + 1}) {"\n".join(el)}")