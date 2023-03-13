def valor_moneda(valor):
    valor = list(str(int(valor))[::-1])
    nuevo_valor = ""
    
    nuevo_valor = ''.join([valor[i] + ',' if (i+1) % 3 == 0 and i != len(valor)-1 else valor[i] for i in range(len(valor))])
    nuevo_valor = (nuevo_valor.replace(",", "", 1) if nuevo_valor.startswith(",") else nuevo_valor)

    return '$' + nuevo_valor[::-1]