inimigos = [
    {"nome": "Darth", "HP": 100, "poder": 150},
    {"nome": "Luke", "HP": 80, "poder": 160},
    {"nome": "Ran", "HP": 50, "poder": 75}
]
'''
print("Nome:", inimigos[0]["nome"], "HP:", inimigos[0]["HP"], "Poder:", inimigos[0]["poder"])
print("Nome:", inimigos[1]["nome"], "HP:", inimigos[1]["HP"], "Poder:", inimigos[1]["poder"])
print("Nome:", inimigos[2]["nome"], "HP:", inimigos[2]["HP"], "Poder:", inimigos[2]["poder"])
'''

# OU

for i in inimigos:
    print(f"Nome: {i['nome']}, HP: {i['HP']}, Poder: {i['poder']}")
