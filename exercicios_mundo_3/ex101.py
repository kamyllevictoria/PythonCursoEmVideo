from datetime import date
def voto(year):
    today = date.today().year
    idade = today - year
    if idade < 16:
        return f"With {idade} years, voting is not mandatory." 
    elif 16 <= idade < 18 or idade > 65:
        return f"With {idade} years, voting is optional."
    else:
        return f"With {idade} years, voting is mandatory."  
    # quando usamos o return, precisamos colocalo em uma variavel no final para poder ser printado  
total = voto(1900) #como aqui:
print(total) #nao podemos so chamar a função, pois ela precisa ter um receptor do return, nao e como o print