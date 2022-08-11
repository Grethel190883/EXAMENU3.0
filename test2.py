from sre_constants import AT_UNI_NON_BOUNDARY


ciudad = str(input("Introduce tu ciudad de nacimiento: "))
ano= int (input("Introduce tu edad:  "))

if(ano >= 18):
    
    print(f'Esta persona tiene la edad de {ano} puede votar en la ciudad de {ciudad}')
else:
    print("Esta persona no tiene edad suficiente para votar")