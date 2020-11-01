import pandas as pd
import numpy as np

global aux
aux = {}
table = pd.read_csv("Compilers\\table.csv")
table = table.replace(to_replace = np.nan, value = 'NULL')
columns = list(table)

def get_error(token,err):
    aux[token] = err

def show_error(token):
    print (aux[token])

def nonterm(col):
    nonterminal = ['inicio','varinicio','varfim','int','real','lit','leia','escreva','literal','num','id','rcb','opm','se','entao','(',')','opr','fimse',';','fim','$']
    if col in nonterminal:
        return 1
    else:
        return 0

def term(col):
    terminal = ['P*','P','V','A','LV','D','TIPO','ES','ARG','CMD','LD','OPRD','COND','CABECALHO','CORPO','EXP_R']
    if col in terminal:
        return 1
    else:
        return 0

def rules(a,mode):
    if a == 1:
        if mode == 0:
            return 3
        elif mode == 1:
            return "P* → P"

    elif a == 2:
        if mode == 0:
            return 5
        elif mode == 1:
            return "P → inicio V A"

    elif a == 3:
        if mode == 0:
            return 4
        elif mode == 1:
            return "V → varinicio LV"

    elif a == 4:
        if mode == 0:
            return 4
        elif mode == 1:
            return "LV → D LV"

    elif a == 5:
        if mode == 0:
            return 4
        elif mode == 1:
            return "LV → varfim;"

    elif a == 6:
        if mode == 0:
            return 5
        elif mode == 1:
            return "D → id TIPO;"

    elif a == 7:
        if mode == 0:
            return 3
        elif mode == 1:
            return "TIPO → int"

    elif a == 8:
        if mode == 0:
            return 3
        elif mode == 1:
            return "TIPO → real"

    elif a == 9:
        if mode == 0:
            return 3
        elif mode == 1:
            return "TIPO → lit"

    elif a == 10:
        if mode == 0:
            return 4
        elif mode == 1:
            return "A → ES A"

    elif a == 11:
        if mode == 0:
            return 5
        elif mode == 1:
            return "ES → leia id;"

    elif a == 12:
        if mode == 0:
            return 5
        elif mode == 1:
            return "ES → escreva ARG;"

    elif a == 13:
        if mode == 0:
            return 3
        elif mode == 1:
            return "ARG → literal"

    elif a == 14:
        if mode == 0:
            return 3
        elif mode == 1:
            return "ARG → num"

    elif a == 15:
        if mode == 0:
            return 3
        elif mode == 1:
            return "ARG → id"

    elif a == 16:
        if mode == 0:
            return 4
        elif mode == 1:
            return "A → CMD A"

    elif a == 17:
        if mode == 0:
            return 6
        elif mode == 1:
            return "CMD → id rcb LD;"

    elif a == 18:
        if mode == 0:
            return 5
        elif mode == 1:
            return "LD → OPRD opm OPRD"

    elif a == 19:
        if mode == 0:
            return 3
        elif mode == 1:
            return "LD → OPRD"

    elif a == 20:
        if mode == 0:
            return 3
        elif mode == 1:
            return "OPRD → id"

    elif a == 21:
        if mode == 0:
            return 3
        elif mode == 1:
            return "OPRD → num"

    elif a == 22:
        if mode == 0:
            return 4
        elif mode == 1:
            return "A → COND A"

    elif a == 23:
        if mode == 0:
            return 4
        elif mode == 1:
            return "COND → CABECALHO CORPO"

    elif a == 24:
        if mode == 0:
            return 7
        elif mode == 1:
            return "CABECALHO → se (EXP_R) entao"

    elif a == 25:
        if mode == 0:
            return 5
        elif mode == 1:
            return "EXP_R → OPRD opr OPRD"

    elif a == 26:
        if mode == 0:
            return 4
        elif mode == 1:
            return "CORPO → ES CORPO"

    elif a == 27:
        if mode == 0:
            return 4
        elif mode == 1:
            return "CORPO → CMD CORPO"

    elif a == 28:
        if mode == 0:
            return 4
        elif mode == 1:
            return "CORPO → COND CORPO"

    elif a == 29:
        if mode == 0:
            return 3
        elif mode == 1:
            return "CORPO → fimse"

    elif a == 30:
        if mode == 0:
            return 3
        elif mode == 1:
            return "A → fim"

def retrieve(a,s):
    d = -1
    for i in columns:
        d += 1
        if (table[i][a] != 'NULL'):
            if table.columns[d] == 'Estado':
                state = table[i][a]
            elif table.columns[d] == s:
                return table[i][a]
    print ("No possible shift or reduce from the state " + str(state) + " with token " + s)
    return 'A'

def goto(a):
    word = rules(a,1)
    return word.split()[0]
