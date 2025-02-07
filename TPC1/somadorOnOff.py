import sys

def somadorOnOff(l):
    i = 0
    valor = 0
    sinal = 1
    flag_on = True
    
    while i < len(l):
        if l[i] == '-':
            sinal = -1
            i += 1
            continue

        if l[i] == '=':
            print("Resultado após '=': " + str(valor))
            
        if i+2 < len(l):
            off = l[i] + l[i+1] + l[i+2]
            on = l[i] + l[i+1]
            
            if off.lower() == "off":
                flag_on = False
                i += 3
                continue
            elif on.lower() == "on":
                flag_on = True
                i += 2

        if l[i].isdigit() and flag_on:
            num = 0
            while i < len(l) and l[i].isdigit():
                num = num * 10 + int(l[i])
                i += 1
            valor += num * sinal
            sinal = 1
        else:
            i += 1

    return valor

def main():
    print()
    print("===================================================================")
    print(" Bem-vindo ao somadorOnOff! Escreva 'sair' para fechar o programa.")
    print("===================================================================")
    
    while True:
        entrada = sys.stdin.readline()
        if entrada.lower().strip() == "sair":
            print("Fechando programa...")
            break
        print("Resultado final:", somadorOnOff(entrada))

if __name__ == '__main__':
    main()
