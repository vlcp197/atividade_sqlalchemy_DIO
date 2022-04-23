from models import Programador,Habilidades,Programador_Habilidade

def insere_programador():
    programador = Programador(nome='Vinicius',idade='25')
    print(programador)
    programador.save()

def consulta_programadores():
    programador = Programador.query.all()
    print(programador)
    programador = Programador.query.filter_by(nome='Vinicius').first()
    print(programador.idade)

def altera_programador():
    programador = Programador.query.filter_by(nome='Vinicius').first()
    programador.idade = 21
    programador.save()

def exclui_programadores():
    programador = Programador.query.filter_by(nome='Vinicius').first()
    programador.delete()
        

if __name__ == '__main__':
    #insere_programador()
    consulta_programadores()
    #altera_programador()
    #exclui_programadores()