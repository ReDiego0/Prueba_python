'''
Los tratamientos serán descontados por planilla mensualmente por un periodo de 12 meses. Todos los tratamientos incluyen:  
✓ Limpieza y detartraje 
✓ Aplicación de sellante   
✓ Aplicación de flúor.  

Los tratamientos ofrecidos son:   
Tratamientos 	         Valor  
Carillas Porcelana  	$250.000  
Implantes Dentales 	    $475.000  
Ortodoncia Brackets  	$800.000  

✓ Trabajador Auxiliar, se aplicará un descuesto del 15%  
✓ Trabajador Administrativo, se aplica un descuento del 10%  
✓ Trabajador Docente, 5% descuento

Las condiciones generales del programa son:   
  
✓	Presentar un menú con las siguientes opciones:   
 
1.	Cotización:   o Debe ofrecer los tratamientos disponibles. 
o	Debe calcular el total de la cotización, además debe consultar si tiene descuento y aplicarlo si corresponde.  
o	Desplegar el total de la cotización e indicar el valor de las cuotas mensuales  
  
2.	Renunciar:  o Debe permitir eliminar la cotización echa anteriormente, volver al menú y permitir realizar una nueva cotización. 
 
3.	Salir del programa sin considerar la cotización que se pueda haber ingresado

Ejemplo de cotización:  
1	tratamiento Carillas Porcelana 
2	tratamientos Ortodoncia Brackets 
  
Aplicando descuento de trabajador docente, en este caso, los datos serían:  ($250.000 + 2 * $800.000) – 5% (descuento) = $1.757.500 
'''

SUMA = 1
r_a = 0
r_r = 0
r_m = 0
r_t = 0

carillas = 0
implantes = 0
ortodoncia = 0
d_auxiliar = 0
d_trabajador_a = 0
d_trabajador_d = 0

C = 250000
I = 475000
O = 800000
# -----------------------------------------
MENSAJE_COTIZACION = ("----------------------------------\n            COTIZACIÓN            \n----------------------------------")
FLECHA = ("-->")
GUION = ("----------------------------------")
# ------------------------------------------

AUXILIAR_D = 0.15
TRABAJADOR_A = 0.10
TRABAJADOR_D = 0.05

while True:
    try:
        print("Elegir cargo\n1. Trabajador Auxiliar\n2. Trabajador Administrativo\n3. Trabajador Docente")
        r_c = int(input("Escribir opción:\n"))
        if r_c > 3 or r_c < 1:
            raise ValueError()
        break
    except ValueError:
        print("Ingreso inválido")
if r_c == 1:
    d_auxiliar += 1
elif r_c == 2:
    d_trabajador_a += 1
else:
    d_trabajador_d += 1


total_descuento = d_auxiliar + d_trabajador_d + d_trabajador_a

while r_m != 4:
    try:
        r_m = int(input("Eliga la opción que desee:\n1. Cotización\n2. Renunciar\n3. Calcular total\n4. Salir del programa\n"))
        if r_m > 4 or r_m < 1:
            raise ValueError()
    except ValueError:
        print("Ingreso inválido")
    if r_m == 1:
        while r_t != 5 or r_t != 4:
            try:
                print("Elegir tratamiento")
                print("[1] Carillas Porcelana")
                print("[2] Implantes Dentales")
                print("[3] Ortodoncia Brackets")
                print("[4] Volver atras")
                print(f"Tratamientos seleccionados actualmente: \nCarillas: {carillas}\nImplantes: {implantes}\nOrtodoncia: {ortodoncia}")
                r_t = int(input("Escribir opción:\n"))
                if r_t < 1 or r_t > 4:
                    raise ValueError()
                break
            except ValueError:
                print("Ingreso inválido")
        if r_t == 1:
            carillas = carillas + SUMA
            print(f"Ha elegido {carillas} de [1] Carillas Porcelana")
        elif r_t == 2:
            implantes = implantes + SUMA
            print(f"Ha elegido {implantes} de [2] Implantes Dentales") 
        elif r_t == 3:
            ortodoncia = ortodoncia + SUMA
            print(f"Ha elegido {ortodoncia} de [3] Ortodoncia Brackets")  
        else:
            print("Volviendo al menú principal...")
    if r_m == 2:
         while r_r != 3:
            try:  
                r_r = int(input("Ha elegido eliminar la cotización hecha anteriormente:\n[1] Eliminar todas las cotizaciones hechas.\n[2] Eliminar una cotización en especifico.\n[3] Volver al menú principal."))
                if r_r > 2 or r_r < 1:
                    raise ValueError()
            except ValueError:
                print("Ingreso inválido")       
            if r_r == 1:
                carillas = carillas - carillas
                ortodoncia = ortodoncia - ortodoncia
                implantes = implantes - implantes
                print("Todas las cotizaciones hechas han sido eliminadas")
                break
            if r_r == 2:
                while r_a != 4:
                    try:
                        print("¿Cual cotización desea eliminar?")
                        print(f"[1] Carillas Porcelana {carillas}")
                        print(f"[2] Implantes Dentales {ortodoncia}")
                        print(f"[3] Ortodoncia Brackets {implantes}")
                        print("[4] Salir sin eliminar nada")
                        r_a = int(input())
                        if r_a > 3 or r_a < 1:
                            raise ValueError()
                        break
                    except ValueError:
                            print("Ingreso inválido")
                    if r_a == 1:
                        carillas = carillas - SUMA
                    elif r_a == 2:
                        ortodoncia = ortodoncia - SUMA
                    elif r_a == 3:
                        implantes = implantes - SUMA
                    else:
                        print("Volviendo atras...")
    if r_m == 3:
        calculo = (carillas * C) + (ortodoncia * O) + (implantes * I)
        descuento = total_descuento / calculo / 100
        if d_auxiliar > d_trabajador_a and d_auxiliar > d_trabajador_d:
            print(f"{MENSAJE_COTIZACION}")
            print(f"{FLECHA} {carillas} Tratamiento (s) {carillas * C}")
            print(f"{FLECHA} {ortodoncia} Tratamiento (s) {ortodoncia * O}")
            print(f"{FLECHA} {implantes} Tratamiento (s) {implantes * I}")
            print(f"{GUION}")
            print(f"Subtotal     {calculo}")
            print(f"Descuento {descuento}")
        elif d_trabajador_d > d_auxiliar and d_trabajador_d > d_trabajador_a:
            print(MENSAJE_COTIZACION)
            print(f"{FLECHA} {carillas} Tratamiento (s) {carillas * C}")
            print(f"{FLECHA} {ortodoncia} Tratamiento (s) {ortodoncia * O}")
            print(f"{FLECHA} {implantes} Tratamiento (s) {implantes * I}")
            print(f"{GUION}")
            print(f"Subtotal     {calculo}")
            print(f"Descuento {descuento}")
        elif d_trabajador_a > d_auxiliar and d_trabajador_a > d_trabajador_d:
            print(MENSAJE_COTIZACION)
            print(f"{FLECHA} {carillas} Tratamiento (s) {carillas * C}")
            print(f"{FLECHA} {ortodoncia} Tratamiento (s) {ortodoncia * O}")
            print(f"{FLECHA} {implantes} Tratamiento (s) {implantes * I}")
            print(f"{GUION}")
            print(f"Subtotal     {calculo}")
            print(f"Descuento {descuento}")
    if r_m == 4:
        print("Ha seleccionado salir del programa, adios.")
        break
# --------------------------------------------------------------------------------



