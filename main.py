

def parser(inputan):
    tokens = inputan.lower().split()
    tokens.append('EOS')
    non_terminals = ['S', 'NN', 'VB']
    terminals = ['er', 'sie', 'mutter', 'vater', 'trinkt' , 'isst', 'benutzt', 'wasser', 'haehnchen', 'schuhe']

    parse_table = {}

    #Check Start
    parse_table[('S', 'er')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'sie')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'mutter')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'vater')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'wasser')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'haehnchen')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'schuhe')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'trinkt')] = ['error']
    parse_table[('S', 'isst')] = ['error']
    parse_table[('S', 'benutzt')] = ['error']
    parse_table[('S', 'EOS')] = ['error']

    #Check NN
    parse_table[('NN', 'er')] = ['er']
    parse_table[('NN', 'sie')] = ['sie']
    parse_table[('NN', 'mutter')] = ['mutter']
    parse_table[('NN', 'vater')] = ['vater']
    parse_table[('NN', 'wasser')] = ['wasser']
    parse_table[('NN', 'haehnchen')] = ['haehnchen']
    parse_table[('NN', 'schuhe')] = ['schuhe']
    parse_table[('NN', 'trinkt')] = ['error']
    parse_table[('NN', 'isst')] = ['error']
    parse_table[('NN', 'benutzt')] = ['error']
    parse_table[('NN', 'EOS')] = ['error']

    #Check VB
    parse_table[('VB', 'er')] = ['error']
    parse_table[('VB', 'sie')] = ['error']
    parse_table[('VB', 'mutter')] = ['error']
    parse_table[('VB', 'vater')] = ['error']
    parse_table[('VB', 'wasser')] = ['error']
    parse_table[('VB', 'haehnchen')] = ['error']
    parse_table[('VB', 'schuhe')] = ['error']
    parse_table[('VB', 'trinkt')] = ['trinkt']
    parse_table[('VB', 'isst')] = ['isst']
    parse_table[('VB', 'benutzt')] = ['benutzt']
    parse_table[('VB', 'EOS')] = ['error']

    stack = []
    stack.append('#')
    stack.append('S')

    index_token = 0
    symbol = tokens[index_token]

    while(len(stack) > 0):
        top = stack[ len(stack) - 1 ]
        print('top = ', top)
        print('symbol = ', symbol)
        if top in terminals:
            print('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                index_token = index_token + 1
                symbol = tokens[index_token]
                if symbol == 'EOS':
                    stack.pop()
                    print('isi stack:', stack)
            else:
                print('error')
                break;
        elif top in non_terminals:
            print('top adalah symbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_push = parse_table[(top, symbol)]
                for i in range(len(symbol_push)-1, -1, -1):
                    stack.append(symbol_push[i])
            else:
                print('error')
                break;
        else:
            print('error')
            break;
        print('isi stack: ', stack)
        print()

    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('input string = ', '"', inputan, '"', '<--diterima, sesuai grammar NN VB NN')
    else:
        print(' input string = ', '"', inputan, '"', ', tidak diterima, tidak sesuai grammar NN VB NN')  

    return parser



def main():
    print("Masukan kata-kata sesuai Kamus")
    print("Kamus: er, sie, mutter, vater, trinkt , isst, benutzt, wasser, haehnchen, schuhe")
    sentence = input('kalimat yang akan dimasukkan: ')
    print("program parser \n")
    parser(sentence)


if __name__ == '__main__':
    main()

