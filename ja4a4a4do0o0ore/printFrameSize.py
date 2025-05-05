import os
import json
from collections import defaultdict

def extract_sections(directory):
    results = []

    sizeRow  = ""

    # Parcourir tous les fichiers dans le répertoire
    for filename in os.listdir(directory):
        if filename.startswith("parsedbyshark172"):
            sizeRow = filename 
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
                
                for i, line in enumerate(lines):                                            

                    if "Packet Length" in line:
                        sizeRow += line[line.find(":")+1:-1]

                    if "Padding Length" in line:
                        sizeRow += " P:" + line[line.find(":")+1:-1]

                    if "Frame Length:" in line:
                        sizeRow += " FE:" + line[line.find(":")+1:line.find("bytes")-1]
                   
        print(sizeRow)

    return results



# Exemple d'utilisation
directory = "."  # Remplacez par le chemin de votre répertoire
output_file = "sections.json"
extract_sections(directory)
