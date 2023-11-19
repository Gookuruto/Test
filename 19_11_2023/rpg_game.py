import obiektowe

print(obiektowe.orc_monster["Attack power"])

monster_list = [{
    "Name": "Orc",
    "Hp": 100,
    "Attack power": 50,
    "Armor": 20
}]
for i in range(10):
    monster_list.append({
        "Name": "Orc",
        "Hp": 100,
        "Attack power": 50,
        "Armor": 20
    })
monster_list[0]["Name"] = "Orc Warrior"
print(monster_list)
obiektowe.orc_monster["attack"]()
