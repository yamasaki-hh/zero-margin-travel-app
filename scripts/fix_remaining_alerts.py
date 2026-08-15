import json

# Fix berlin b_49
with open("data/cities/berlin.json", "r", encoding="utf-8") as f:
    ber = json.load(f)

for s in ber["spots"]:
    if s["id"] == "b_49":
        s["desc_fr"] = "Jardins du Monde à Marzahn avec jardin japonais, chinois et téléphérique."

with open("data/cities/berlin.json", "w", encoding="utf-8") as f:
    json.dump(ber, f, ensure_ascii=False, indent=2)

# Fix hamburg h_13, h_33
with open("data/cities/hamburg.json", "r", encoding="utf-8") as f:
    ham = json.load(f)

for s in ham["spots"]:
    if s["id"] == "h_13":
        s["desc_fr"] = "Musée des arts et métiers avec collections Art nouveau et orientales."
    elif s["id"] == "h_33":
        s["desc_fr"] = "Expérience sensorielle unique guidée dans l'obscurité totale par des non-voyants."

with open("data/cities/hamburg.json", "w", encoding="utf-8") as f:
    json.dump(ham, f, ensure_ascii=False, indent=2)

print("🎉 Fixed alert fields for Berlin and Hamburg!")
