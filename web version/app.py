from flask import *

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "abc" 
def lexical(inputan):
    import string
    inputanString = inputan.lower()+'#'

    listAlphabet = list(string.ascii_lowercase)
    listState=[]
    for i in range(0,41):
        if (i != 26):
            listState.append(f'q{i}')
    tableTransition = {}

    for state in listState:
        for alphabet in listAlphabet:
            tableTransition[(state, alphabet)] = 'error'
        tableTransition[(state, '#')] = 'error'
        tableTransition[(state, ' ')] = 'error'

    # First State
    tableTransition['q0', ' '] = 'q0'

    # Final State
    tableTransition['q3', '#'] = 'accept'
    tableTransition['q3', ' '] = 'q8'
    tableTransition['q8', '#'] = 'accept'
    tableTransition['q8', ' '] = 'q8'

    # Word sie
    tableTransition['q0', 's'] = 'q1'
    tableTransition['q1', 'i'] = 'q2'
    tableTransition['q2', 'e'] = 'q3'
    tableTransition['q8', 's'] = 'q1'
    
    # Word schuhe
    tableTransition['q1', 'c'] = 'q4'
    tableTransition['q4', 'h'] = 'q5'
    tableTransition['q5', 'u'] = 'q6'
    tableTransition['q6', 'h'] = 'q7'
    tableTransition['q7', 'e'] = 'q3'

    # Word er
    tableTransition['q0', 'e'] = 'q9'
    tableTransition['q9', 'r'] = 'q3'
    tableTransition['q8', 'e'] = 'q9'

    # Word mutter
    tableTransition['q0', 'm'] = 'q11'
    tableTransition['q11', 'u'] = 'q12'
    tableTransition['q12', 't'] = 'q13'
    tableTransition['q13', 't'] = 'q14'
    tableTransition['q14', 'e'] = 'q9'
    tableTransition['q8', 'm'] = 'q11'

    # Word vatter
    tableTransition['q0', 'v'] = 'q15'
    tableTransition['q15', 'a'] = 'q16'
    tableTransition['q16', 't'] = 'q14'
    tableTransition['q8', 'v'] = 'q15'

    # Word wasser
    tableTransition['q0', 'w'] = 'q10'
    tableTransition['q10', 'a'] = 'q17'
    tableTransition['q17', 's'] = 'q18'
    tableTransition['q18', 's'] = 'q19'
    tableTransition['q19', 'e'] = 'q9'
    tableTransition['q8', 'w'] = 'q10'

    # Word isst
    tableTransition['q0', 'i'] = 'q20'
    tableTransition['q20', 's'] = 'q18'
    tableTransition['q19', 't'] = 'q3'
    tableTransition['q8', 'i'] = 'q20'

    # Word haehnchen
    tableTransition['q0', 'h'] = 'q33'
    tableTransition['q33', 'a'] = 'q34'
    tableTransition['q34', 'e'] = 'q35'
    tableTransition['q35', 'h'] = 'q36'
    tableTransition['q36', 'n'] = 'q37'
    tableTransition['q37', 'c'] = 'q38'
    tableTransition['q38', 'h'] = 'q39'
    tableTransition['q39', 'e'] = 'q40'
    tableTransition['q40', 'n'] = 'q3'
    tableTransition['q8', 'h'] = 'q33'

    # Word trinkt
    tableTransition['q0', 't'] = 'q21'
    tableTransition['q21', 'r'] = 'q22'
    tableTransition['q22', 'i'] = 'q23'
    tableTransition['q23', 'n'] = 'q24'
    tableTransition['q24', 'k'] = 'q25'
    tableTransition['q25', 't'] = 'q3'
    tableTransition['q8', 't'] = 'q21'

    # Word benutzt
    tableTransition['q0', 'b'] = 'q27'
    tableTransition['q27', 'e'] = 'q28'
    tableTransition['q28', 'n'] = 'q29'
    tableTransition['q29', 'u'] = 'q30'
    tableTransition['q30', 't'] = 'q31'
    tableTransition['q31', 'z'] = 'q32'
    tableTransition['q32', 't'] = 'q3'
    tableTransition['q8', 'b'] = 'q27'

    idx_char = 0
    state = 'q0'
    current_token = ' '
    while state != 'accept':
        current_char = inputanString[idx_char]
        current_token += current_char
        state = tableTransition[(state, current_char)]
        if state=='error':
            break;
        idx_char = idx_char + 1

    #simpulan
    if state == 'accept':
        return True
    else:
        return False

def parser(inputan):
    parser = False
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
                break
        elif top in non_terminals:
            print('top adalah symbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_push = parse_table[(top, symbol)]
                for i in range(len(symbol_push)-1, -1, -1):
                    stack.append(symbol_push[i])
            else:
                print('error')
                break
        else:
            print('error')
            break
        print('isi stack: ', stack)
        print()

    if symbol == 'EOS' and len(stack) == 0:
        print('input string = ', '"', inputan, '"', '<--diterima, sesuai grammar NN VB NN')
        output = f'Inputan valid, input string = ', '"', inputan, '"', '<--diterima, sesuai grammar NN VB NN'
    else:
        print('input string = ', '"', inputan, '"', ', tidak diterima, tidak sesuai grammar NN VB NN')  
        output = f'Inputan valid, input string = ', '"', inputan, '"', ', tidak diterima, tidak sesuai grammar NN VB NN'

    return output

@app.route("/")
def back_home():
	return redirect(url_for("home"))

@app.route("/home",methods = ["GET","POST"])
def home():
	error = None;
	if request.method == "GET":
		return render_template("home.html")
	data = request.form
	#Proses pertama pengecekan data
	if data["nama"] == "":
		error = "Inputan Kosong"
	else:
		inputan = data["nama"]
		text = lexical(inputan)
		if (text):
			flash(parser(inputan))
		else:
			flash("Inputan tidak sesuai dengan yang ada pada kamus, parser tidak dilakukan")

	return render_template("home.html", error = error)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)