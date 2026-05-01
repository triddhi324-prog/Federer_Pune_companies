import pandas as pd
data = [
    {"Company":"Rossari Biotech","City":"Pune","Segment":"Specialty Chemicals","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Moderate","C5":"Strong","C6":"Strong"},
    {"Company":"Fine Organic Industries","City":"Pune","Segment":"Performance Chemicals","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Privi Speciality Chemicals","City":"Pune","Segment":"Specialty Chemicals","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Aether Industries","City":"Pune","Segment":"Custom Synthesis","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Deepak Fertilisers","City":"Pune","Segment":"Performance Chemicals","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Chemetall India","City":"Pune","Segment":"Specialty Chemicals","Revenue":"100-300Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Dorf Ketal Chemicals","City":"Pune","Segment":"Specialty Chemicals","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Emcure Pharmaceuticals","City":"Pune","Segment":"Complex Pharma","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"BVG Life Sciences","City":"Pune","Segment":"Biotech","Revenue":"<300Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Gennova Biopharma","City":"Pune","Segment":"Biotech","Revenue":"<300Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Praxis Life Sciences","City":"Pune","Segment":"Pharma Chemicals","Revenue":"<100Cr","C1":"Strong","C2":"Strong","C3":"Moderate","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Anshul Life Sciences","City":"Pune","Segment":"Pharma","Revenue":"<300Cr","C1":"Strong","C2":"Strong","C3":"Moderate","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Enzene Biosciences","City":"Pune","Segment":"Biotech","Revenue":"<300Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Kan Biosys","City":"Pune","Segment":"Agri Biotech","Revenue":"<100Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Micro Inks","City":"Pune","Segment":"Performance Chemicals","Revenue":"<300Cr","C1":"Strong","C2":"Strong","C3":"Moderate","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Hikal","City":"Pune","Segment":"Custom Synthesis","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Kusumgar Corporates","City":"Pune","Segment":"Specialty Chemicals","Revenue":"<100Cr","C1":"Strong","C2":"Strong","C3":"Moderate","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Garware Technical Fibres","City":"Pune","Segment":"Specialty Materials","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Endress+Hauser India","City":"Pune","Segment":"Instrumentation","Revenue":"100-300Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Forbes Marshall","City":"Pune","Segment":"Instrumentation","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Strong","C5":"Strong","C6":"Strong"},
    {"Company":"Unichem Laboratories","City":"Pune","Segment":"Pharma","Revenue":"<300Cr","C1":"Strong","C2":"Strong","C3":"Moderate","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Ajinkya Chemtech","City":"Pune","Segment":"Specialty Chemicals","Revenue":"<50Cr","C1":"Strong","C2":"Strong","C3":"Moderate","C4":"Moderate","C5":"Strong","C6":"Moderate"},
    {"Company":"NGL Fine-Chem","City":"Pune","Segment":"Pharma Chemicals","Revenue":"100-300Cr","C1":"Strong","C2":"Strong","C3":"Moderate","C4":"Strong","C5":"Strong","C6":"Moderate"},
    {"Company":"Mapro Industries","City":"Pune","Segment":"Food Ingredients","Revenue":"<300Cr","C1":"Strong","C2":"Strong","C3":"Moderate","C4":"Moderate","C5":"Strong","C6":"Strong"},
    {"Company":"EPL Limited","City":"Pune","Segment":"Specialty Materials","Revenue":"300-500Cr","C1":"Strong","C2":"Strong","C3":"Strong","C4":"Moderate","C5":"Strong","C6":"Strong"},
]

df = pd.DataFrame(data)
score_map = {"Strong":1, "Moderate":0.5, "Weak":0}

weights = {
    "C1":10,
    "C2":5,
    "C3":25,
    "C4":20,
    "C5":20,
    "C6":20
}

def calculate_score(row):
    total = 0
    for c in weights:
        total += score_map[row[c]] * weights[c]
    return total

df["Total Score"] = df.apply(calculate_score, axis=1)

df["Band"] = df["Total Score"].apply(lambda x: "A" if x >= 80 else "B")

df = df.sort_values(by="Total Score", ascending=False)

df.to_csv("federer_pune_companies.csv", index=False)

print(" CSV file created: federer_pune_companies.csv")
print(df)