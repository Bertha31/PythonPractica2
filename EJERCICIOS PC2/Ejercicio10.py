meses = {
    "Enero": "01",
    "Febrero": "02",
    "Marzo": "03",
    "Abril": "04",
    "Mayo": "05",
    "Junio": "06",
    "Julio": "07",
    "Agosto": "08",
    "Septiembre": "09",
    "Octubre": "10",
    "Noviembre": "11",
    "Diciembre": "12"
}

fecha_input = input("Ingrese la fecha (en formato mes-día-año o mes día, año): ")

partes = fecha_input.split()
if len(partes) == 3:
    mes = partes[0]
    dia = partes[1][:-1] 
    ano = partes[2]
else:
    mes, dia, ano = fecha_input.split('-')
mes_numero = meses.get(mes, mes)

fecha_formateada = f"{ano}-{mes_numero:02}-{dia:02}"

print("Fecha formateada:", fecha_formateada)
