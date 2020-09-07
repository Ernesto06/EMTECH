#IMPORTACIÓN DE lISTAS:

from listas import lifestore_products
from listas import lifestore_sales
from listas import lifestore_searches

#INICIO DE SESIÓN:

print("Bienvenido al portal de información de LifeStore.")
usuario = input(
    '\nFavor de ingresar su puesto en la empresa: \na)Gerente\nb)Vendedor\nc)Otro\n'
)

if usuario != 'a':
    print(
        '\nLo siento, sólo los usuarios con calidad de administrador pueden acceder a la base de datos. \nFavor de ponerse en contacto con su supervisor.'
    )

else:
    i = 0
    decis = 0
    for i in range(0, 3):
        password = input(
            '\nIngrese su contraseña de administrador. Máximo 3 intentos\n')
        if password == 'ls4ever':
            print(
                '\nContrasena correcta, ahora puede acceder a la base de datos.'
            )
            admin = input("Ingrese su nombre, por favor\n")
            print("\nHola gerente", admin)
            decis = 1
            break

        else:
            i += 1
            print("Contraseña incorrecta, intento número", i)

#MENÚ PRINCIPAL:

    while decis == 1:
        print("\nMenú principal, ¿qué desea consultar?")
        opcion = input(
            "\na)Menú de ventas \nb)Menú de búsquedas \nc)Menú de reseñas y devoluciones \nd)Nada, deseo salir\n"
        )

        ventas = []
        for producto in lifestore_products:
            contador = 0
            for venta in lifestore_sales:
                if producto[0] == venta[1]:
                    contador += 1
            ventas_formato = [
                producto[0], producto[1], producto[3], producto[4], contador,
                producto[2]
            ]
            ventas.append(ventas_formato)

        busquedas = []
        for producto in ventas:
            contador = 0
            for busca in lifestore_searches:
                if producto[0] == busca[1]:
                    contador += 1
            busca_formato = [
                producto[0], producto[1], producto[2], producto[3],
                producto[4], contador
            ]
            busquedas.append(busca_formato)

        categorias = []
        for producto in busquedas:
            if producto[2] not in categorias:
                categorias.append(producto[2])

        procesadores = []
        for producto in busquedas:
            if producto[2] == categorias[0]:
                procesadores_formato = [
                    producto[0], producto[1], producto[4], producto[5]
                ]
                procesadores.append(procesadores_formato)

        tarjetas_video = []
        for producto in busquedas:
            if producto[2] == categorias[1]:
                video_formato = [
                    producto[0], producto[1], producto[4], producto[5]
                ]
                tarjetas_video.append(video_formato)

        tarjetas_madre = []
        for producto in busquedas:
            if producto[2] == categorias[2]:
                madre_formato = [
                    producto[0], producto[1], producto[4], producto[5]
                ]
                tarjetas_madre.append(madre_formato)

        discos = []
        for producto in busquedas:
            if producto[2] == categorias[3]:
                discos_formato = [
                    producto[0], producto[1], producto[4], producto[5]
                ]
                discos.append(discos_formato)

        usb = []
        for producto in busquedas:
            if producto[2] == categorias[4]:
                usb_formato = [
                    producto[0], producto[1], producto[4], producto[5]
                ]
                usb.append(usb_formato)

        pantallas = []
        for producto in busquedas:
            if producto[2] == categorias[5]:
                pantallas_formato = [
                    producto[0], producto[1], producto[4], producto[5]
                ]
                pantallas.append(pantallas_formato)

        bocinas = []
        for producto in busquedas:
            if producto[2] == categorias[6]:
                bocinas_formato = [
                    producto[0], producto[1], producto[4], producto[5]
                ]
                bocinas.append(bocinas_formato)

        audifonos = []
        for producto in busquedas:
            if producto[2] == categorias[7]:
                audifonos_formato = [
                    producto[0], producto[1], producto[4], producto[5]
                ]
                audifonos.append(audifonos_formato)

        resenas = []
        for producto in busquedas:
            contador = 0
            suma = 0
            for resena in lifestore_sales:
                if producto[0] == resena[1]:
                    suma += resena[2]
                    contador += 1
            if contador == 0:
                resena_formato = [producto[0], producto[1], contador, 0]
                resenas.append(resena_formato)
            else:
                resena_formato = [
                    producto[0],
                    producto[1],
                    contador,
                    suma / contador,
                ]
                resenas.append(resena_formato)

        devueltos = []
        for producto in resenas:
            i = 0
            suma = 0
            for devolucion in lifestore_sales:
                if producto[0] == devolucion[1] and devolucion[4] == 1:
                    i += 1
                    suma += devolucion[2]
                else:
                    continue
            if i > 0:
                devueltos_formato = [
                    producto[0], producto[1], producto[3], i, suma / i
                ]
                devueltos.append(devueltos_formato)

        if opcion == "d":
            print("\nVuelva pronto gerente", admin,
                  "fue un placer atenderle.\n")
            decis = 0

        elif opcion != 'a' and opcion != 'b' and opcion != 'c':
            print(
                '\nNo ha seleccionado alguna opción válida, intente de nuevo')
            decis = 1
#INGRESO FORMAL A A
        elif opcion == 'a':

            print('\nEste es el menú de ventas, elija una opcion:')
            op_ventas = input(
                '\na1)Productos más vendidos globales \na2)Productos menos vendidos globales\na3)Ventas por categoría\na4)Ingresos y ventas\n'
            )

            if op_ventas != 'a1' and op_ventas != 'a2' and op_ventas != 'a3' and op_ventas != 'a4' and op_ventas != 'a5':
                print(
                    '\nNo ha seleccionado alguna opción válida, volverá al menú principal'
                )
                decis = 1

            elif op_ventas == 'a1':

                ventas_ordenadas_1 = []
                while ventas:
                    maximo = ventas[0][4]
                    valor_actual = ventas[0]
                    for venta in ventas:
                        if venta[4] > maximo:
                            maximo = venta[4]
                            valor_actual = venta
                    ventas_ordenadas_1.append(valor_actual)
                    ventas.remove(valor_actual)

                print(
                    '\nFormato de presentación de datos: id, Producto, Stock, Ventas\n'
                )

                mayores_ventas = []
                i = 1
                for venta in ventas_ordenadas_1:
                    if venta[4] == 0:
                        continue
                    else:
                        mayores_ventas.append(venta)
                        print(i, '.-', venta[0], ',', venta[1], ',', venta[3],
                              ',', venta[4], '\n')
                        i += 1

                print(
                    'Estos son los', i - 1,
                    'productos con mayores ventas globales.\nLos demás no registraron ninguna.\n'
                )

            elif op_ventas == 'a2':

                ventas_ordenadas_2 = []
                while ventas:
                    minimo = ventas[0][4]
                    valor_actual = ventas[0]
                    for venta in ventas:
                        if venta[4] < minimo:
                            minimo = venta[4]
                            valor_actual = venta
                    ventas_ordenadas_2.append(valor_actual)
                    ventas.remove(valor_actual)
                print(
                    '\nFormato de presentación de datos: id, Producto, Stock, Ventas\n'
                )

                menores_ventas = []
                i = 1
                for venta in ventas_ordenadas_2:
                    if venta[4] == 0:
                        menores_ventas.append(venta)
                        print(i, '.-', venta[0], ',', venta[1], ',', venta[3],
                              ',', venta[4], '\n')
                        i += 1

                print(
                    'Estos son los', i - 1,
                    'productos con menores ventas globales:\nno presentaron ninguna venta.\n'
                )

            elif op_ventas == 'a3':
                choice = input(
                    "\n¿Qué categoría quieres consultar?\n1)Procesadores \n2)Tarjetas de video \n3)Tarjetas madre \n4)Discos duros \n5)USB \n6)Pantallas \n7)Bocinas \n8)Audífonos"
                )

                if choice == '1':
                    procesadores_ordenadas = []
                    while procesadores:
                        minimo = procesadores[0][2]
                        valor_actual = procesadores[0]
                        for proceso in procesadores:
                            if proceso[2] < minimo:
                                minimo = proceso[2]
                                valor_actual = proceso
                        procesadores_ordenadas.append(valor_actual)
                        procesadores.remove(valor_actual)

                    print(
                        '\nVentas ascendentes de procesadores.\nFormato de presentación de datos: id, Producto, Ventas\n'
                    )
                    for proceso in procesadores_ordenadas:
                        print(proceso[0], ',', proceso[1], ',', proceso[2],
                              '\n')

                elif choice == '2':
                    tarjetas_video_ordenadas = []
                    while tarjetas_video:
                        minimo = tarjetas_video[0][2]
                        valor_actual = tarjetas_video[0]
                        for tarjeta in tarjetas_video:
                            if tarjeta[2] < minimo:
                                minimo = tarjeta[2]
                                valor_actual = tarjeta
                        tarjetas_video_ordenadas.append(valor_actual)
                        tarjetas_video.remove(valor_actual)

                    print(
                        '\nVentas en ascendente de Tarjetas de video.\nFormato de presentación de datos: id, Producto, Ventas\n'
                    )
                    for tarjeta in tarjetas_video_ordenadas:
                        print(tarjeta[0], ',', tarjeta[1], ',', tarjeta[2],
                              '\n')

                elif choice == '3':
                    tarjetas_madre_ordenadas = []
                    while tarjetas_madre:
                        minimo = tarjetas_madre[0][2]
                        valor_actual = tarjetas_madre[0]
                        for tarjeta in tarjetas_madre:
                            if tarjeta[2] < minimo:
                                minimo = tarjeta[2]
                                valor_actual = tarjeta
                        tarjetas_madre_ordenadas.append(valor_actual)
                        tarjetas_madre.remove(valor_actual)

                    print(
                        '\nVentas en ascendente de Trajetas madre.\nFormato de presentación de datos: id, Producto, Ventas\n'
                    )
                    for tarjeta in tarjetas_madre_ordenadas:
                        print(tarjeta[0], ',', tarjeta[1], ',', tarjeta[2],
                              '\n')

                elif choice == '4':
                    discos_ordenadas = []
                    while discos:
                        minimo = discos[0][2]
                        valor_actual = discos[0]
                        for disco in discos:
                            if disco[2] < minimo:
                                minimo = disco[2]
                                valor_actual = disco
                        discos_ordenadas.append(valor_actual)
                        discos.remove(valor_actual)

                    print(
                        '\nVentas en ascendente de Discos duros.\nFormato de presentación de datos: id, Producto, Ventas\n'
                    )
                    for disco in discos_ordenadas:
                        print(disco[0], ',', disco[1], ',', disco[2], '\n')

                elif choice == '5':
                    usb_ordenadas = []
                    while usb:
                        minimo = usb[0][2]
                        valor_actual = usb[0]
                        for us in usb:
                            if us[2] < minimo:
                                minimo = us[2]
                                valor_actual = us
                        usb_ordenadas.append(valor_actual)
                        usb.remove(valor_actual)

                    print(
                        '\nVentas en ascendente de USB.\nFormato de presentación de datos: id, Producto, Ventas\n'
                    )
                    for us in usb_ordenadas:
                        print(us[0], ',', us[1], ',', us[2], '\n')

                elif choice == '6':
                    pantallas_ordenadas = []
                    while pantallas:
                        minimo = pantallas[0][2]
                        valor_actual = pantallas[0]
                        for pantalla in pantallas:
                            if pantalla[2] < minimo:
                                minimo = pantalla[2]
                                valor_actual = pantalla
                        pantallas_ordenadas.append(valor_actual)
                        pantallas.remove(valor_actual)

                    print(
                        '\nVentas en ascendente de Pantallas.\nFormato de presentación de datos: id, Producto, Ventas\n'
                    )
                    for pantalla in pantallas_ordenadas:
                        print(pantalla[0], ',', pantalla[1], ',', pantalla[2],
                              '\n')

                elif choice == '7':
                    bocinas_ordenadas = []
                    while bocinas:
                        minimo = bocinas[0][2]
                        valor_actual = bocinas[0]
                        for bocina in bocinas:
                            if bocina[2] < minimo:
                                minimo = bocina[2]
                                valor_actual = bocina
                        bocinas_ordenadas.append(valor_actual)
                        bocinas.remove(valor_actual)

                    print(
                        '\nVentas en ascendente de Bocinas.\nFormato de presentación de datos: id, Producto, Ventas\n'
                    )
                    for bocina in bocinas_ordenadas:
                        print(bocina[0], ',', bocina[1], ',', bocina[2], '\n')

                elif choice == '8':
                    audifonos_ordenadas = []
                    while audifonos:
                        minimo = audifonos[0][2]
                        valor_actual = audifonos[0]
                        for audifono in audifonos:
                            if audifono[2] < minimo:
                                minimo = audifono[2]
                                valor_actual = audifono
                        audifonos_ordenadas.append(valor_actual)
                        audifonos.remove(valor_actual)

                    print(
                        '\nVentas en ascendente de Audífonos.\nFormato de presentación de datos: id, Producto, Ventas\n'
                    )
                    for audifono in audifonos_ordenadas:
                        print(audifono[0], ',', audifono[1], ',', audifono[2],
                              '\n')

            elif op_ventas == 'a4':
                choice = input(
                    "\nElija una opcion:\n1)Enero \n2)Febrero \n3)Marzo \n4)Abril \n5)Mayo \n6)Junio \n7)Julio \n8)Agosto\n9)Septiembre\n10)Octubre\n11)Noviembre\n12)Diciembre\n13)Ingresos y ventas mensuales y totales\n"
                )

                enero = []
                for producto in ventas:
                    i = 0
                    for venta in lifestore_sales:
                        if producto[0] == venta[1] and venta[3][
                                3:5] == '01' and venta[4] == 0:
                            i += 1
                    if i > 0:
                        enero_formato = [
                            producto[0], producto[1], i, producto[5],
                            i * producto[5]
                        ]
                        enero.append(enero_formato)

                enero_ventas = 0
                enero_ingresos = 0
                for venta in enero:
                    enero_ventas += venta[2]
                    enero_ingresos += venta[4]

                febrero = []
                for producto in ventas:
                    i = 0
                    for venta in lifestore_sales:
                        if producto[0] == venta[1] and venta[3][
                                3:5] == '02' and venta[4] == 0:
                            i += 1
                    if i > 0:
                        febrero_formato = [
                            producto[0], producto[1], i, producto[5],
                            i * producto[5]
                        ]
                        febrero.append(febrero_formato)

                febrero_ventas = 0
                febrero_ingresos = 0
                for venta in febrero:
                    febrero_ventas += venta[2]
                    febrero_ingresos += venta[4]

                marzo = []
                for producto in ventas:
                    i = 0
                    for venta in lifestore_sales:
                        if producto[0] == venta[1] and venta[3][
                                3:5] == '03' and venta[4] == 0:
                            i += 1
                    if i > 0:
                        marzo_formato = [
                            producto[0], producto[1], i, producto[5],
                            i * producto[5]
                        ]
                        marzo.append(marzo_formato)

                marzo_ventas = 0
                marzo_ingresos = 0
                for venta in marzo:
                    marzo_ventas += venta[2]
                    marzo_ingresos += venta[4]

                abril = []
                for producto in ventas:
                    i = 0
                    for venta in lifestore_sales:
                        if producto[0] == venta[1] and venta[3][
                                3:5] == '04' and venta[4] == 0:
                            i += 1
                    if i > 0:
                        abril_formato = [
                            producto[0], producto[1], i, producto[5],
                            i * producto[5]
                        ]
                        abril.append(abril_formato)

                abril_ventas = 0
                abril_ingresos = 0
                for venta in abril:
                    abril_ventas += venta[2]
                    abril_ingresos += venta[4]

                mayo = []
                for producto in ventas:
                    i = 0
                    for venta in lifestore_sales:
                        if producto[0] == venta[1] and venta[3][
                                3:5] == '05' and venta[4] == 0:
                            i += 1
                    if i > 0:
                        mayo_formato = [
                            producto[0], producto[1], i, producto[5],
                            i * producto[5]
                        ]
                        mayo.append(mayo_formato)

                mayo_ventas = 0
                mayo_ingresos = 0
                for venta in mayo:
                    mayo_ventas += venta[2]
                    mayo_ingresos += venta[4]

                junio = []
                for producto in ventas:
                    i = 0
                    for venta in lifestore_sales:
                        if producto[0] == venta[1] and venta[3][
                                3:5] == '06' and venta[4] == 0:
                            i += 1
                    if i > 0:
                        junio_formato = [
                            producto[0], producto[1], i, producto[5],
                            i * producto[5]
                        ]
                        junio.append(junio_formato)

                junio_ventas = 0
                junio_ingresos = 0
                for venta in junio:
                    junio_ventas += venta[2]
                    junio_ingresos += venta[4]

                julio = []
                for producto in ventas:
                    i = 0
                    for venta in lifestore_sales:
                        if producto[0] == venta[1] and venta[3][
                                3:5] == '07' and venta[4] == 0:
                            i += 1
                    if i > 0:
                        julio_formato = [
                            producto[0], producto[1], i, producto[5],
                            i * producto[5]
                        ]
                        julio.append(julio_formato)

                julio_ventas = 0
                julio_ingresos = 0
                for venta in julio:
                    julio_ventas += venta[2]
                    julio_ingresos += venta[4]

                agosto = []
                for producto in ventas:
                    i = 0
                    for venta in lifestore_sales:
                        if producto[0] == venta[1] and venta[3][
                                3:5] == '08' and venta[4] == 0:
                            i += 1
                    if i > 0:
                        agosto_formato = [
                            producto[0], producto[1], i, producto[5],
                            i * producto[5]
                        ]
                        agosto.append(agosto_formato)

                agosto_ventas = 0
                agosto_ingresos = 0
                for venta in agosto:
                    agosto_ventas += venta[2]
                    agosto_ingresos += venta[4]

                meses = [['enero', enero_ventas, enero_ingresos],
                         ['febrero', febrero_ventas, febrero_ingresos],
                         ['marzo', marzo_ventas, marzo_ingresos],
                         ['abril', abril_ventas, abril_ingresos],
                         ['mayo', mayo_ventas, mayo_ingresos],
                         ['junio', junio_ventas, junio_ingresos],
                         ['julio', julio_ventas, julio_ingresos],
                         ['agosto', agosto_ventas, agosto_ingresos],
                         ['septiembre', 0, 0], ['octubre', 0, 0],
                         ['noviembr', 0, 0], ['diciembre', 0, 0]]

                if choice == '1':

                    print(
                        '\nVentas en enero, sin considerar las devoluciones (se descuentan).\nFormato de presentación de datos: id, Producto, #Ventas en el mes, Precio, Total\n'
                    )

                    i = 1
                    for venta in enero:
                        print(i, '.-', venta, '\n')
                        i += 1

                    print('Cantidad de ventas en enero:', enero_ventas,
                          '\nIngresos totales en enero: $', enero_ingresos,
                          '\n')

                if choice == '2':

                    print(
                        '\nVentas en febrero, sin considerar las devoluciones (se descuentan).\nFormato de presentación de datos: id, Producto, #Ventas en el mes, Precio, Total\n'
                    )

                    i = 1
                    for venta in febrero:
                        print(i, '.-', venta, '\n')
                        i += 1

                    print('Cantidad de ventas en febrero:', febrero_ventas,
                          '\nIngresos totales en febrero: $', febrero_ingresos,
                          '\n')

                if choice == '3':

                    print(
                        '\nVentas en marzo, sin considerar las devoluciones (se descuentan).\nFormato de presentación de datos: id, Producto, #Ventas en el mes, Precio, Total\n'
                    )

                    i = 1
                    for venta in marzo:
                        print(i, '.-', venta, '\n')
                        i += 1

                    print('Cantidad de ventas en marzo:', marzo_ventas,
                          '\nIngresos totales en marzo: $', marzo_ingresos,
                          '\n')

                if choice == '4':

                    print(
                        '\nVentas en abril sin considerar las devoluciones (se descuentan).\nFormato de presentación de datos: id, Producto, #Ventas en el mes, Precio, Total\n'
                    )

                    i = 1
                    for venta in abril:
                        print(i, '.-', venta, '\n')
                        i += 1

                    print('Cantidad de ventas en abril:', abril_ventas,
                          '\nIngresos totales en abril: $', abril_ingresos,
                          '\n')

                if choice == '5':

                    print(
                        '\nVentas en mayo, sin considerar las devoluciones (se descuentan).\nFormato de presentación de datos: id, Producto, #Ventas en el mes, Precio, Total\n'
                    )

                    i = 1
                    for venta in mayo:
                        print(i, '.-', venta, '\n')
                        i += 1

                    print('Cantidad de ventas en mayo:', mayo_ventas,
                          '\nIngresos totales en mayo: $', mayo_ingresos, '\n')

                if choice == '6':

                    print(
                        '\nVentas en junio, sin considerar las devoluciones (se descuentan).\nFormato de presentación de datos: id, Producto, #Ventas en el mes, Precio, Total\n'
                    )

                    i = 1
                    for venta in junio:
                        print(i, '.-', venta, '\n')
                        i += 1

                    print('Cantidad de ventas en junio:', junio_ventas,
                          '\nIngresos totales en junio: $', junio_ingresos,
                          '\n')

                if choice == '7':

                    print(
                        '\nVentas en julio, sin considerar las devoluciones (se descuentan).\nFormato de presentación de datos: id, Producto, #Ventas en el mes, Precio, Total\n'
                    )

                    i = 1
                    for venta in julio:
                        print(i, '.-', venta, '\n')
                        i += 1

                    print('Cantidad de ventas en julio:', julio_ventas,
                          '\nIngresos totales en julio: $', julio_ingresos,
                          '\n')

                if choice == '8':

                    print(
                        '\nVentas en agosto, sin considerar las devoluciones (se descuentan).\nFormato de presentación de datos: id, Producto, #Ventas en el mes, Precio, Total\n'
                    )

                    i = 1
                    for venta in agosto:
                        print(i, '.-', venta, '\n')
                        i += 1

                    print('Cantidad de ventas en agosto:', agosto_ventas,
                          '\nIngresos totales en agosto: $', agosto_ingresos,
                          '\n')

                if choice == '9':
                    print('No hubo ventas en este mes \n')

                if choice == '10':
                    print('No hubo ventas en este mes\n')

                if choice == '11':
                    print('No hubo ventas en este mes\n')

                if choice == '12':
                    print('No hubo ventas en este mes\n')

                if choice == '13':

                    total_ingresos = 0
                    total_ventas = 0
                    for ingreso in meses:
                        total_ingresos += ingreso[2]
                        total_ventas += ingreso[1]

                    promedio_ingresos = total_ingresos / 12
                    promedio_ventas = total_ventas / 12
                    promedio_ingresos2 = total_ingresos / 8
                    promedio_ventas2 = total_ventas / 8

                    print(
                        '\nIngresos anuales totales: $', total_ingresos,
                        '\nVentas totales anuales (devoluciones descontadas):',
                        total_ventas, '\n')
                    print(
                        '\nPromedio mensual de ingresos: $', promedio_ingresos,
                        '\nPromedio mensual de ventas:', promedio_ventas,
                        '\n\nSi se consideran sólo los meses donde hubo ventas registradas(8), entonces los mismos promedios quedan así: $',
                        promedio_ingresos2, ',', promedio_ventas2,
                        'ventas al mes\n')

                    meses_ordenados = []
                    while meses:
                        maximo = meses[0][2]
                        valor_actual = meses[0]
                        for mes in meses:
                            if mes[2] > maximo:
                                maximo = mes[2]
                                valor_actual = mes
                        meses_ordenados.append(valor_actual)
                        meses.remove(valor_actual)

                    print(
                        '\nMeses ordenados por mayores ingresos.\nFormato de datos: Mes, #Ventas mensuales, Ingresos al mes\n'
                    )
                    for mes in meses_ordenados:
                        print(mes, '\n')

            decis = input(
                '\nDesea realizar otra acción? ("Si" para volver al menú principal)\n'
            )

            if decis != 'Si':
                print("\nHasta luego gerente", admin)
                decis = 0
            else:
                decis = 1

#INGRESO FORMAL A B

        elif opcion == 'b':

            print('\nEste es el menú de búsquedas, elija una opción:')
            op_busca = input(
                '\nb1)Productos más buscados globales\nb2)Productos menos buscados globales\nb3)Búsquedas por categorías\n'
            )

            if op_busca != 'b1' and op_busca != 'b2' and op_busca != 'b3':
                print(
                    '\nNo ha seleccionado alguna opción válida, volverá al menú principal'
                )
                decis = 1

            elif op_busca == 'b1':

                busquedas_ordenadas_1 = []
                while busquedas:
                    maximo = busquedas[0][5]
                    valor_actual = busquedas[0]
                    for busqueda in busquedas:
                        if busqueda[5] > maximo:
                            maximo = busqueda[5]
                            valor_actual = busqueda
                    busquedas_ordenadas_1.append(valor_actual)
                    busquedas.remove(valor_actual)

                print(
                    '\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                )

                mayores_busquedas = []
                i = 1
                for busqueda in busquedas_ordenadas_1:
                    if busqueda[5] == 0:
                        continue
                    else:
                        mayores_busquedas.append(busqueda)
                        print(i, '.-', busqueda[0], ',', busqueda[1], ',',
                              busqueda[5], '\n')
                        i += 1

                print(
                    'Estos son los', i - 1,
                    'productos con mayores búsquedas globales.\nLos demás no registraron ninguna búsqueda.\n'
                )

            elif op_busca == 'b2':

                busquedas_ordenadas_2 = []
                while busquedas:
                    minimo = busquedas[0][5]
                    valor_actual = busquedas[0]
                    for busqueda in busquedas:
                        if busqueda[5] < minimo:
                            minimo = busqueda[5]
                            valor_actual = busqueda
                    busquedas_ordenadas_2.append(valor_actual)
                    busquedas.remove(valor_actual)
                print(
                    '\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                )

                menores_busquedas = []
                i = 1
                for busqueda in busquedas_ordenadas_2[0:50]:
                    if busqueda[5] == 0:
                        menores_busquedas.append(busqueda)
                        print(i, '.-', busqueda[0], ',', busqueda[1], ',',
                              busqueda[5], '\n')
                        i += 1

                print(
                    'Estos son los', i - 1,
                    'productos con menores búsquedas globales:\nno presentaron ninguna.\n'
                )

            elif op_busca == 'b3':

                choice = input(
                    "\n¿Qué categoría quieres consultar?\n1)Procesadores \n2)Tarjetas de video \n3)Tarjetas madre \n4)Discos duros \n5)USB \n6)Pantallas \n7)Bocinas \n8)Audífonos"
                )

                if choice == '1':
                    procesadores_ordenadas = []
                    while procesadores:
                        minimo = procesadores[0][3]
                        valor_actual = procesadores[0]
                        for proceso in procesadores:
                            if proceso[3] < minimo:
                                minimo = proceso[3]
                                valor_actual = proceso
                        procesadores_ordenadas.append(valor_actual)
                        procesadores.remove(valor_actual)

                    print(
                        '\nBúsquedas ascendentes de procesadores.\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                    )
                    for proceso in procesadores_ordenadas:
                        print(proceso[0], ',', proceso[1], ',', proceso[3],
                              '\n')

                elif choice == '2':
                    tarjetas_video_ordenadas = []
                    while tarjetas_video:
                        minimo = tarjetas_video[0][3]
                        valor_actual = tarjetas_video[0]
                        for tarjeta in tarjetas_video:
                            if tarjeta[3] < minimo:
                                minimo = tarjeta[3]
                                valor_actual = tarjeta
                        tarjetas_video_ordenadas.append(valor_actual)
                        tarjetas_video.remove(valor_actual)

                    print(
                        '\nBúsquedas en ascendente de Tarjetas de video.\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                    )
                    for tarjeta in tarjetas_video_ordenadas:
                        print(tarjeta[0], ',', tarjeta[1], ',', tarjeta[3],
                              '\n')

                elif choice == '3':
                    tarjetas_madre_ordenadas = []
                    while tarjetas_madre:
                        minimo = tarjetas_madre[0][3]
                        valor_actual = tarjetas_madre[0]
                        for tarjeta in tarjetas_madre:
                            if tarjeta[3] < minimo:
                                minimo = tarjeta[3]
                                valor_actual = tarjeta
                        tarjetas_madre_ordenadas.append(valor_actual)
                        tarjetas_madre.remove(valor_actual)

                    print(
                        '\nBúsquedas en ascendente de Trajetas madre.\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                    )
                    for tarjeta in tarjetas_madre_ordenadas:
                        print(tarjeta[0], ',', tarjeta[1], ',', tarjeta[3],
                              '\n')

                elif choice == '4':
                    discos_ordenadas = []
                    while discos:
                        minimo = discos[0][3]
                        valor_actual = discos[0]
                        for disco in discos:
                            if disco[3] < minimo:
                                minimo = disco[3]
                                valor_actual = disco
                        discos_ordenadas.append(valor_actual)
                        discos.remove(valor_actual)

                    print(
                        '\nBúsquedas en ascendente de Discos duros.\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                    )
                    for disco in discos_ordenadas:
                        print(disco[0], ',', disco[1], ',', disco[3], '\n')

                elif choice == '5':
                    usb_ordenadas = []
                    while usb:
                        minimo = usb[0][3]
                        valor_actual = usb[0]
                        for us in usb:
                            if us[3] < minimo:
                                minimo = us[3]
                                valor_actual = us
                        usb_ordenadas.append(valor_actual)
                        usb.remove(valor_actual)

                    print(
                        '\nBúsquedas en ascendente de USB.\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                    )
                    for us in usb_ordenadas:
                        print(us[0], ',', us[1], ',', us[3], '\n')

                elif choice == '6':
                    pantallas_ordenadas = []
                    while pantallas:
                        minimo = pantallas[0][3]
                        valor_actual = pantallas[0]
                        for pantalla in pantallas:
                            if pantalla[3] < minimo:
                                minimo = pantalla[3]
                                valor_actual = pantalla
                        pantallas_ordenadas.append(valor_actual)
                        pantallas.remove(valor_actual)

                    print(
                        '\nBúsquedas en ascendente de Pantallas.\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                    )
                    for pantalla in pantallas_ordenadas:
                        print(pantalla[0], ',', pantalla[1], ',', pantalla[3],
                              '\n')

                elif choice == '7':
                    bocinas_ordenadas = []
                    while bocinas:
                        minimo = bocinas[0][3]
                        valor_actual = bocinas[0]
                        for bocina in bocinas:
                            if bocina[3] < minimo:
                                minimo = bocina[3]
                                valor_actual = bocina
                        bocinas_ordenadas.append(valor_actual)
                        bocinas.remove(valor_actual)

                    print(
                        '\nBúsquedas en ascendente de Bocinas.\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                    )
                    for bocina in bocinas_ordenadas:
                        print(bocina[0], ',', bocina[1], ',', bocina[3], '\n')

                elif choice == '8':
                    audifonos_ordenadas = []
                    while audifonos:
                        minimo = audifonos[0][3]
                        valor_actual = audifonos[0]
                        for audifono in audifonos:
                            if audifono[3] < minimo:
                                minimo = audifono[3]
                                valor_actual = audifono
                        audifonos_ordenadas.append(valor_actual)
                        audifonos.remove(valor_actual)

                    print(
                        '\nBúsquedas en ascendente de Audífonos.\nFormato de presentación de datos: id, Producto, Búsquedas\n'
                    )
                    for audifono in audifonos_ordenadas:
                        print(audifono[0], ',', audifono[1], ',', audifono[3],
                              '\n')

            decis = input(
                '\nDesea realizar otra acción? ("Si" para volver al menú principal)\n'
            )
            if decis != 'Si':
                print("\nHasta luego gerente", admin)
                decis = 0

            else:
                decis = 1

#INGRESO FORMAL A C

        elif opcion == 'c':

            print(
                '\nEste es el menú de reseñas y devoluciones, elija una opción:'
            )
            op_resdev = input(
                '\nc1)Productos con mejores reseñas\nc2)Productos con peores reseñas\nc3)Productos devueltos\n'
            )

            if op_resdev != 'c1' and op_resdev != 'c2' and op_resdev != 'c3':
                print(
                    '\nNo ha seleccionado alguna opción válida, volverá al menú principal'
                )
                decis = 1

            elif op_resdev == 'c1':

                resenas_ordenadas_1 = []
                while resenas:
                    maximo = resenas[0][3]
                    valor_actual = resenas[0]
                    for resena in resenas:
                        if resena[3] > maximo:
                            maximo = resena[3]
                            valor_actual = resena
                    resenas_ordenadas_1.append(valor_actual)
                    resenas.remove(valor_actual)

                print(
                    '\nFormato de presentación de datos: id, Producto, #Reseñas, Reseña promedio (de 1 a 5)\n'
                )

                mayores_resenas = []
                i = 1
                for resena in resenas_ordenadas_1[0:20]:
                    mayores_resenas.append(resena)
                    print(i, '.-', resena, '\n')
                    i += 1

                print('Estos son los', i - 1,
                      'productos con mayores reseñas promedio.\n')

            elif op_resdev == 'c2':

                resenas_ordenadas_2 = []
                while resenas:
                    minimo = resenas[0][3]
                    valor_actual = resenas[0]
                    for resena in resenas:
                        if resena[3] < minimo:
                            minimo = resena[3]
                            valor_actual = resena
                    resenas_ordenadas_2.append(valor_actual)
                    resenas.remove(valor_actual)

                print(
                    '\nFormato de presentación de datos: id, Producto, #Reseñas, Reseña promedio (de 1 a 5)\n'
                )

                menores_resenas = []
                i = 1
                for resena in resenas_ordenadas_2:
                    if i == 21:
                        break
                    elif resena[2] == 0:
                        continue
                    else:
                        menores_resenas.append(resena)
                        i += 1

                i = 1
                for resena in menores_resenas:
                    print(i, '.-', resena, '\n')
                    i += 1

                print(
                    'Estos son los', i - 1,
                    'productos con menores reseñas promedio.\nNo se toman en cuenta aquellos que no se vendieron y que acumularon 0 reseñas.\n'
                )

            elif op_resdev == 'c3':

                print(
                    '\nFormato de presentación de datos: id, Producto, Reseña promedio (de 1 a 5), #Devoluciones, Reseña Promedio de devoluciones:\n'
                )

                i = 1
                for devuelto in devueltos:
                    print(i, '-', devuelto, '\n')
                    i += 1

                print(
                    'Estos son los', i - 1,
                    'productos devueltos con sus respectivas reseñas promedio (globales y de devoluciones).\n'
                )

            decis = input(
                '\nDesea realizar otra acción? ("Si" para volver al menú principal)\n'
            )
            if decis != 'Si':
                print("\nHasta luego gerente", admin)
                decis = 0

            else:
                decis = 1
