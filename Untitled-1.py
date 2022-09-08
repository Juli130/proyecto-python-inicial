
from csv import DictReader
import csv
from pickle import TRUE


def un_jugador():
    with open("trivia.csv", "r") as csvfile:
    
        data = list(csv.DictReader(csvfile))
    resp_cor = []
    lis_resp = []
    num = 1
    
    for i in data:  
        print(i['pregunta'])
        print(i["respuesta 1"])
        print(i["respuesta 2"])
        print(i["respuesta 3"])
        print(i["respuesta 4"])
        reco = i["respuesta_correcta"]
        respu = str(input("coloque su respuesta:").lower())
        if respu == i["respuesta 1"] or respu == i["respuesta 2"] or respu == i["respuesta 3"] or respu == i["respuesta 4"]: 
            
            if respu == reco:
                resp = ("pregunta", num, "correcta")
                lis_resp.append(resp)
                num += 1
            else:
                resp = ("pregunta", num, "incorrecta")
                lis_resp.append(resp)
                num += 1
        else:
            print("respuesta invalida")
            resp = ("respuesta", num, "invalida")
            lis_resp.append(resp)
            continue
    print(lis_resp)
    
def dos_jugadores():
    with open("trivia.csv", "r") as csvfile:
    
        data = list(csv.DictReader(csvfile))
    resp_cor = []
    lis_resp = []
    lis_resp2 = []
    num_2 = 1
    num = 1
    for i in data:  
        print(i['pregunta'])
        print(i["respuesta 1"])
        print(i["respuesta 2"])
        print(i["respuesta 3"])
        print(i["respuesta 4"])
        reco = i["respuesta_correcta"]
        respu = str(input("jugador 1 coloque su respuesta:").lower())
        respu_2 = str(input("jugador 2 coloque su respuesta:").lower())
        if respu == i["respuesta 1"] or respu == i["respuesta 2"] or respu == i["respuesta 3"] or respu == i["respuesta 4"]: 
            
            if respu == reco:
                resp = ("pregunta", num, "correcta")
                lis_resp.append(resp)
                num += 1
            else:
                resp = ("pregunta", num, "incorrecta")
                lis_resp.append(resp)
                num += 1
        else:
            print("respuesta invalida")
            resp = ("respuesta", num, "invalida")
            lis_resp.append(resp)
            continue
        if respu_2 == i["respuesta 1"] or respu_2 == i["respuesta 2"] or respu_2 == i["respuesta 3"] or respu_2 == i["respuesta 4"]: 
            
            if respu_2== reco:
                resp_2 = ("pregunta", num, "correcta")
                lis_resp2.append(resp_2)
                num_2 += 1
            else:
                resp_2 = ("pregunta", num, "incorrecta")
                lis_resp2.append(resp_2)
                num_2 += 1
        else:
            print("respuesta invalida")
            resp = ("respuesta", num, "invalida")
            lis_resp2.append(resp_2)
            continue
    print('jugador 1', lis_resp)
    print('jugador 2', lis_resp2)




if __name__ == '__main__':
    
    print('''hola, bienbenido a la trivia de videojuegos. seleccione la cantidad de jugadores(maximo 2)''')

    cant_jug = int(input())

    while TRUE:
        if cant_jug == 1:
            un_jugador()
            break

        elif cant_jug == 2:
            dos_jugadores()
            break
        else:
            print("introduce una opcion correcta")
