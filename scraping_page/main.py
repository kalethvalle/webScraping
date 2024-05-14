import scraping as s
import json
import os

def main():
    actors = ["0992339411001", "0968599020001"]
    demandados = ["1791251237001", "0968599020001"]

    pages = s.Scraping()

    for actor in actors:
        pages.getPage()
        lista_causas = pages.serachCausas(nro_actor=actor)
        
        json_object = json.dumps(lista_causas, indent=4)
        file_path = os.path.join(os.path.dirname(__file__), f'../src/collections/actors/{actor}.json')
        with open(file_path, "w") as outfile:
            outfile.write(json_object)


if __name__ == '__main__':
    main()