import re

def open_file(path):
    with open(path, 'r') as file:
        header = file.readline()  # skip header
        content = file.read()
    return content

def parser():
    compositores = set()
    obras_por_periodo = {}
    periodo_titulos = {}
    
    content = open_file('obras.csv')
    
    records = re.split(r'\n(?=(?:[^"]*"[^"]*")*[^"]*$)', content)
    
    for record in records:
        fields = re.findall(r'(?:[^;"]|"(?:[^"]|"")*")+', record)
        fields = [f.strip() for f in fields]
        
        if len(fields) >= 5:
            titulo = fields[0]
            periodo = fields[3]
            compositor = fields[4]
            
            if titulo and periodo and compositor:
                compositores.add(compositor)
                obras_por_periodo[periodo] = obras_por_periodo.get(periodo, 0) + 1
                
                if periodo not in periodo_titulos:
                    periodo_titulos[periodo] = set()
                periodo_titulos[periodo].add(titulo)

    compositores_sorted = sorted(list(compositores))
    
    for periodo in periodo_titulos:
        periodo_titulos[periodo] = sorted(list(periodo_titulos[periodo]))
    
    return compositores_sorted, obras_por_periodo, periodo_titulos



def print_results(compositores, obras_por_periodo, periodo_titulos):
    with open('compositores.txt', 'w') as f:
        f.write("Lista ordenada de compositores:\n")
        for compositor in compositores:
            f.write(f"- {compositor}\n")
        print("Arquivo 'compositores.txt' criado com sucesso!")
    
    with open('obras_por_periodo.txt', 'w') as f:
        f.write("Distribuição de obras por período:\n")
        for periodo, quantidade in sorted(obras_por_periodo.items()):
            f.write(f"- {periodo}: {quantidade} obras\n")
        print("Arquivo 'obras_por_periodo.txt' criado com sucesso!")
    
    with open('titulos_por_periodo.txt', 'w') as f:
        f.write("Títulos por período:\n")
        for periodo in sorted(periodo_titulos.keys()):
            f.write(f"\n{periodo}:\n")
            for titulo in periodo_titulos[periodo]:
                f.write(f"- {titulo}\n")
        print("Arquivo 'titulos_por_periodo.txt' criado com sucesso!")



def main():
    compositores, obras_por_periodo, periodo_titulos = parser()
    print_results(compositores, obras_por_periodo, periodo_titulos)

if __name__ == '__main__':
    main()