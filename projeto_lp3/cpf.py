from validate_docbr import CPF

cpf =CPF()

print(cpf.generate(True)) ##True retorna cpf com máscara
print(cpf.generate(False)) ##False retorna cpf sem máscara

print(cpf.validate("546.823.258-84"))
print(cpf.validate("54682325884"))
print(cpf.validate("123321215555"))

cpfs = ["54682325884", "54cdvwrvev682325884"]
   
    
print(cpf.validate_list(cpfs))