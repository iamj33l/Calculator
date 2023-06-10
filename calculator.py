from tkinter import *
import sympy
import math

def calculator():
    """This function creates a calculator"""

    # creating the window
    frame = Tk()
    frame.title("Calculator")
    frame.iconbitmap('calculator.ico')

    problem = Entry(frame, width=25, borderwidth=2, font='"IBM Plex Mono" 15')
    problem.grid(row=0, column=0, columnspan=4)

    solution = Entry(frame, width=15, borderwidth=2, font='"IBM Plex Mono" 25', justify=RIGHT)
    solution.insert(0, '0')
    solution.grid(row=1, column=0, columnspan=4)

    # creating Menu
    menubar = Menu(frame)
    frame.config(menu=menubar)

    # function for clicking buttons
    def clickButton(string):
        current = problem.get()
        problem.delete(0, END)
        problem.insert(0, current + string)

    # function to evaluate
    def equalsTo():
        question = problem.get()
        solution.delete(0, END)

        try:

            if '!' in question:
                question = question.replace('!', '')
                answer = sympy.factorial(int(question))

            elif 'e' in question:
                temp = question.split('e^')
                question = f'e raised to the power of {temp[1]}'
                answer = round(sympy.exp(float(temp[1])).n(), 4)

            elif '^' in question:
                temp = question.split('^')
                question = f'({temp[0]})**({temp[1]})'
                answer = eval(question)

            elif 'P' in question:
                temp = question.split('P')
                answer = sympy.factorial(int(temp[0])) / (
                    sympy.factorial(int(temp[0]) - int(temp[1])))

            elif 'C' in question:
                temp = question.split('C')
                answer = sympy.factorial(int(temp[0])) / (
                        sympy.factorial(int(temp[0]) - int(temp[1])) * sympy.factorial(int(temp[1])))

            elif '√' in question:
                temp = question.split('√')
                question = f'square root of {temp[1]}'
                answer = round(sympy.sqrt(int(temp[1])), 4)

            elif 'sin' in question:
                temp = question.split('sin')
                question = f'sin({temp[1]})'
                answer = round(sympy.sin(((float(temp[1]) * math.pi) / 180)).n(), 4)

            elif 'cos' in question:
                temp = question.split('cos')
                question = f'cos({temp[1]})'
                answer = round(sympy.cos(((float(temp[1]) * math.pi) / 180)).n(), 4)

            elif 'tan' in question:
                temp = question.split('tan')
                question = f'tan({temp[1]})'
                answer = round(sympy.tan(((float(temp[1]) * math.pi) / 180)).n(), 4)

            elif 'asin' in question:
                temp = question.split('asin')
                question = f'sin inverse of ({temp[1]})'
                answer = round(sympy.asin(float(temp[1])).n(), 4)

            elif 'acos' in question:
                temp = question.split('acos')
                question = f'cos inverse of ({temp[1]})'
                answer = round(sympy.acos(float(temp[1])).n(), 4)

            elif 'atan' in question:
                temp = question.split('atan')
                question = f'tan inverse of ({temp[1]})'
                answer = round(sympy.atan(float(temp[1])).n(), 4)

            elif 'ln' in question:
                temp = question.split('ln')
                question = f'ln({temp[1]})'
                answer = round(sympy.log(float(temp[1])).n(), 4)

            elif 'log' in question:
                temp = question.split('log')
                question = f'log({temp[1]})'
                answer = round(sympy.log(float(temp[1]), 10).n(), 4)

            elif 'π' in question:
                question = question.replace('π', 'pi')
                answer = round(sympy.pi.n(), 4)

            else:
                answer = eval(question)

        except SyntaxError:
            solution.insert(0, "Error")

        else:
            solution.insert(0, answer)
            with open('history.txt', 'r') as history:
                content = history.readline()
                if content == 'History has been cleared.':
                    with open('history.txt', 'w') as historyLine:
                        historyLine.write('')
            with open('history.txt', 'a') as history:
                history.write(f'{question} = {answer} \n\n')

    # function to add brackets
    def addBrackets():
        previous = problem.get()
        problem.delete(0, END)
        withBracket = f'({previous})'
        problem.insert(0, withBracket)

    # function to clear
    def clear():
        solution.delete(0, END)
        problem.delete(0, END)

    # function to add negative sign
    def negative():
        current = problem.get()
        problem.delete(0, END)
        problem.insert(0, "-(" + current + ")")

    # function to backspace
    def backspace():
        current = problem.get()
        problem.delete(0, END)
        problem.insert(0, current[:-1])

    # function to perform binary operations
    def binaryOperations():
        question = problem.get()
        solution.delete(0, END)

        try:
            if "AND" in question:
                temp = question.split(" AND ")
                answer = int(temp[0], 2) & int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

            elif "OR" in question:
                temp = question.split(" OR ")
                answer = int(temp[0], 2) | int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

            elif "NAND" in question:
                temp = question.split(" NAND ")
                answer = int(temp[0], 2) & int(temp[1], 2)
                solution.insert(0, not bin(answer)[2:])

            elif "NOR" in question:
                temp = question.split(" NOR ")
                answer = int(temp[0], 2) | int(temp[1], 2)
                solution.insert(0, not bin(answer)[2:])

            elif "XOR" in question:
                temp = question.split(" XOR ")
                answer = int(temp[0], 2) ^ int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

            elif "XNOR" in question:
                temp = question.split(" XNOR ")
                answer = int(temp[0], 2) ^ int(temp[1], 2)
                solution.insert(0, not bin(answer)[2:])

            elif "NOT" in question:
                temp = question.split(" NOT ")
                answer = int(temp[0], 2)
                solution.insert(0, not bin(answer)[2:])

            elif "+" in question:
                temp = question.split("+")
                answer = int(temp[0], 2) + int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

            elif "-" in question:
                temp = question.split("-")
                answer = int(temp[0], 2) - int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

            elif "*" in question:
                temp = question.split("*")
                answer = int(temp[0], 2) * int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

            elif "/" in question:
                temp = question.split("/")
                answer = int(temp[0], 2) / int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

            elif "<<" in question:
                temp = question.split("<<")
                answer = int(temp[0], 2) << int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

            elif ">>" in question:
                temp = question.split(">>")
                answer = int(temp[0], 2) >> int(temp[1], 2)
                solution.insert(0, bin(answer)[2:])

        except:
            solution.insert(0, "Invalid Input")

        with open('history.txt', 'r') as history:
            content = history.readline()
            if content == 'History has been cleared.':
                with open('history.txt', 'w') as historyLine:
                    historyLine.write('')
        with open('history.txt', 'a') as history:
            history.write(f'{question} = {answer} \n\n')

    # function to show history
    def showHistory():
        historyFrame = Tk()
        historyFrame.title("History")
        historyFrame.geometry('300x500')
        historyFrame.iconbitmap('History.ico')
        historyFrame.resizable(False, False)

        scrollbar = Scrollbar(historyFrame)
        scrollbar.pack(side=RIGHT, fill=Y)

        historyLines = ''
        with open('history.txt', 'r') as history:

            contents = history.readlines()

        for content in contents:
            if content == '\n':
                continue
            else:
                historyLines += f'- {content}'

        historyContent = Text(historyFrame, wrap=WORD, font='"IBM plex mono" 10', yscrollcommand=scrollbar.set)
        historyContent.pack(side=LEFT, fill=BOTH)
        historyContent.insert(END, historyLines)
        historyContent.config(state=DISABLED)

    # function to clear history
    def clearHistory():
        with open('history.txt', 'w') as history:
            history.write('History has been cleared.')

    # creating history menu
    historyMenu = Menu(menubar, tearoff=FALSE)
    historyMenu.add_command(label='Show History', command=showHistory)
    historyMenu.add_command(label='Clear History', command=clearHistory)
    menubar.add_cascade(label='History', menu=historyMenu)

    # creating buttons

    oneImage = PhotoImage(file='one.png')
    oneLabel = Label(frame, image=oneImage)
    oneButton = Button(frame, image=oneImage, command=lambda: clickButton('1'))
    oneButton.grid(row=5, column=0)

    twoImage = PhotoImage(file='two.png')
    twoLabel = Label(frame, image=twoImage)
    twoButton = Button(frame, image=twoImage, command=lambda: clickButton('2'))
    twoButton.grid(row=5, column=1)

    threeImage = PhotoImage(file='three.png')
    threeLabel = Label(frame, image=threeImage)
    threeButton = Button(frame, image=threeImage, command=lambda: clickButton('3'))
    threeButton.grid(row=5, column=2)

    fourImage = PhotoImage(file='four.png')
    fourLabel = Label(frame, image=fourImage)
    fourButton = Button(frame, image=fourImage, command=lambda: clickButton('4'))
    fourButton.grid(row=4, column=0)

    fiveImage = PhotoImage(file='five.png')
    fiveLabel = Label(frame, image=fiveImage)
    fiveButton = Button(frame, image=fiveImage, command=lambda: clickButton('5'))
    fiveButton.grid(row=4, column=1)

    sixImage = PhotoImage(file='six.png')
    sixLabel = Label(frame, image=sixImage)
    sixButton = Button(frame, image=sixImage, command=lambda: clickButton('6'))
    sixButton.grid(row=4, column=2)

    sevenImage = PhotoImage(file='seven.png')
    sevenLabel = Label(frame, image=sevenImage)
    sevenButton = Button(frame, image=sevenImage, command=lambda: clickButton('7'))
    sevenButton.grid(row=3, column=0)

    eightImage = PhotoImage(file='eight.png')
    eightLabel = Label(frame, image=eightImage)
    eightButton = Button(frame, image=eightImage, command=lambda: clickButton('8'))
    eightButton.grid(row=3, column=1)

    nineImage = PhotoImage(file='nine.png')
    nineLabel = Label(frame, image=nineImage)
    nineButton = Button(frame, image=nineImage, command=lambda: clickButton('9'))
    nineButton.grid(row=3, column=2)

    zeroImage = PhotoImage(file='zero.png')
    zeroLabel = Label(frame, image=zeroImage)
    zeroButton = Button(frame, image=zeroImage, command=lambda: clickButton('0'))
    zeroButton.grid(row=6, column=1)

    clearImage = PhotoImage(file='clear.png')
    clearLabel = Label(frame, image=clearImage)
    clearButton = Button(frame, image=clearImage, command=clear)
    clearButton.grid(row=2, column=0)

    backspaceImage = PhotoImage(file='backspace.png')
    backspaceLabel = Label(frame, image=backspaceImage)
    backspaceButton = Button(frame, image=backspaceImage, command=backspace)
    backspaceButton.grid(row=2, column=1)

    bracketImage = PhotoImage(file='brackets.png')
    bracketLabel = Label(frame, image=bracketImage)
    bracketButton = Button(frame, image=bracketImage, command=addBrackets)
    bracketButton.grid(row=2, column=2)

    negativeImage = PhotoImage(file='negative.png')
    negativeLabel = Label(frame, image=negativeImage)
    negativeButton = Button(frame, image=negativeImage, command=negative)
    negativeButton.grid(row=6, column=0)

    pointImage = PhotoImage(file='point.png')
    pointLabel = Label(frame, image=pointImage)
    pointButton = Button(frame, image=pointImage, command=lambda: clickButton('.'))
    pointButton.grid(row=6, column=2)

    equalImage = PhotoImage(file='equal.png')
    equalLabel = Label(frame, image=equalImage)
    equalButton = Button(frame, image=equalImage, command=equalsTo)
    equalButton.grid(row=6, column=3)

    plusImage = PhotoImage(file='plus.png')
    plusLabel = Label(frame, image=plusImage)
    plusButton = Button(frame, image=plusImage, command=lambda: clickButton('+'))
    plusButton.grid(row=5, column=3)

    minusImage = PhotoImage(file='minus.png')
    minusLabel = Label(frame, image=minusImage)
    minusButton = Button(frame, image=minusImage, command=lambda: clickButton('-'))
    minusButton.grid(row=4, column=3)

    multiplyImage = PhotoImage(file='multiplication.png')
    multiplyLabel = Label(frame, image=multiplyImage)
    multiplyButton = Button(frame, image=multiplyImage, command=lambda: clickButton('*'))
    multiplyButton.grid(row=3, column=3)

    divideImage = PhotoImage(file='division.png')
    divideLabel = Label(frame, image=divideImage)
    divideButton = Button(frame, image=divideImage, command=lambda: clickButton('/'))
    divideButton.grid(row=2, column=3)

    powerImage = PhotoImage(file='power.png')
    powerLabel = Label(frame, image=powerImage)
    powerButton = Button(frame, image=powerImage, command=lambda: clickButton('^'))

    squareRootImage = PhotoImage(file='root.png')
    squareRootLabel = Label(frame, image=squareRootImage)
    squareRootButton = Button(frame, image=squareRootImage, command=lambda: clickButton('√'))

    factorialImage = PhotoImage(file='factorial.png')
    factorialLabel = Label(frame, image=factorialImage)
    factorialButton = Button(frame, image=factorialImage, command=lambda: clickButton('!'))

    permutationImage = PhotoImage(file='permutation.png')
    permutationLabel = Label(frame, image=permutationImage)
    permutationButton = Button(frame, image=permutationImage, command=lambda: clickButton('P'))

    combinationImage = PhotoImage(file='combination.png')
    combinationLabel = Label(frame, image=combinationImage)
    combinationButton = Button(frame, image=combinationImage, command=lambda: clickButton('C'))

    sinImage = PhotoImage(file='sin.png')
    sinLabel = Label(frame, image=sinImage)
    sinButton = Button(frame, image=sinImage, command=lambda: clickButton('sin'))

    cosImage = PhotoImage(file='cos.png')
    cosLabel = Label(frame, image=cosImage)
    cosButton = Button(frame, image=cosImage, command=lambda: clickButton('cos'))

    tanImage = PhotoImage(file='tan.png')
    tanLabel = Label(frame, image=tanImage)
    tanButton = Button(frame, image=tanImage, command=lambda: clickButton('tan'))

    logImage = PhotoImage(file='log.png')
    logLabel = Label(frame, image=logImage)
    logButton = Button(frame, image=logImage, command=lambda: clickButton('log'))

    lnImage = PhotoImage(file='ln.png')
    lnLabel = Label(frame, image=lnImage)
    lnButton = Button(frame, image=lnImage, command=lambda: clickButton('ln'))

    asinImage = PhotoImage(file='asin.png')
    asinLabel = Label(frame, image=asinImage)
    asinButton = Button(frame, image=asinImage, command=lambda: clickButton('asin'))

    acosImage = PhotoImage(file='acos.png')
    acosLabel = Label(frame, image=acosImage)
    acosButton = Button(frame, image=acosImage, command=lambda: clickButton('acos'))

    atanImage = PhotoImage(file='atan.png')
    atanLabel = Label(frame, image=atanImage)
    atanButton = Button(frame, image=atanImage, command=lambda: clickButton('atan'))

    exponentialImage = PhotoImage(file='exponential.png')
    exponentialLabel = Label(frame, image=exponentialImage)
    exponentialButton = Button(frame, image=exponentialImage, command=lambda: clickButton('e'))

    piImage = PhotoImage(file='pi.png')
    piLabel = Label(frame, image=piImage)
    piButton = Button(frame, image=piImage, command=lambda: clickButton('π'))

    andImage = PhotoImage(file='and.png')
    andLabel = Label(frame, image=andImage)
    andButton = Button(frame, image=andImage, command=lambda: clickButton(' AND '))

    orImage = PhotoImage(file='or.png')
    orLabel = Label(frame, image=orImage)
    orButton = Button(frame, image=orImage, command=lambda: clickButton(' OR '))

    nandImage = PhotoImage(file='nand.png')
    nandLabel = Label(frame, image=nandImage)
    nandButton = Button(frame, image=nandImage, command=lambda: clickButton(' NAND '))

    norImage = PhotoImage(file='nor.png')
    norLabel = Label(frame, image=norImage)
    norButton = Button(frame, image=norImage, command=lambda: clickButton(' NOR '))

    xorImage = PhotoImage(file='xor.png')
    xorLabel = Label(frame, image=xorImage)
    xorButton = Button(frame, image=xorImage, command=lambda: clickButton(' XOR '))

    xnorImage = PhotoImage(file='xnor.png')
    xnorLabel = Label(frame, image=xnorImage)
    xnorButton = Button(frame, image=xnorImage, command=lambda: clickButton(' XNOR '))

    complementImage = PhotoImage(file='complement.png')
    complementLabel = Label(frame, image=complementImage)
    complementButton = Button(frame, image=complementImage, command=lambda: clickButton(' NOT '))

    leftShiftImage = PhotoImage(file='leftShift.png')
    leftShiftLabel = Label(frame, image=leftShiftImage)
    leftShiftButton = Button(frame, image=leftShiftImage, command=lambda: clickButton('<<'))

    rightShiftImage = PhotoImage(file='rightShift.png')
    rightShiftLabel = Label(frame, image=rightShiftImage)
    rightShiftButton = Button(frame, image=rightShiftImage, command=lambda: clickButton('>>'))

    binaryEqualImage = PhotoImage(file='binaryEqual.png')
    binaryEqualLabel = Label(frame, image=binaryEqualImage)
    binaryEqualButton = Button(frame, image=binaryEqualImage, command=binaryOperations)

    # creating mode menu
    modeMenu = Menu(menubar, tearoff=0)

    # function to convert to simple calculator
    def simpleCalculator():
        """Function to create simple calculator"""

        # changing the title of the window
        frame.title('Simple Calculator')

        # adjusting width and position of problem
        problem.config(width=25)
        problem.grid(row=0, column=0, columnspan=4)

        # adjusting width and position of solution
        solution.config(width=15)
        solution.grid(row=1, column=0, columnspan=4)

        # changing the state of menu
        modeMenu.entryconfig('Scientific Calculator', state=NORMAL)
        modeMenu.entryconfig('Binary Calculator', state=NORMAL)
        modeMenu.entryconfig('Simple Calculator', state=DISABLED)

        # removing scientific buttons
        powerButton.grid_forget()
        squareRootButton.grid_forget()
        factorialButton.grid_forget()
        permutationButton.grid_forget()
        combinationButton.grid_forget()
        sinButton.grid_forget()
        cosButton.grid_forget()
        tanButton.grid_forget()
        logButton.grid_forget()
        lnButton.grid_forget()
        asinButton.grid_forget()
        acosButton.grid_forget()
        atanButton.grid_forget()
        exponentialButton.grid_forget()
        piButton.grid_forget()

        # removing binary buttons
        andButton.grid_forget()
        orButton.grid_forget()
        nandButton.grid_forget()
        norButton.grid_forget()
        xorButton.grid_forget()
        xnorButton.grid_forget()
        complementButton.grid_forget()
        leftShiftButton.grid_forget()
        rightShiftButton.grid_forget()
        binaryEqualButton.grid_forget()

        # adding simple buttons
        oneButton.grid(row=5, column=0)
        twoButton.grid(row=5, column=1)
        threeButton.grid(row=5, column=2)
        fourButton.grid(row=4, column=0)
        fiveButton.grid(row=4, column=1)
        sixButton.grid(row=4, column=2)
        sevenButton.grid(row=3, column=0)
        eightButton.grid(row=3, column=1)
        nineButton.grid(row=3, column=2)
        zeroButton.grid(row=6, column=1)
        pointButton.grid(row=6, column=2)
        equalButton.grid(row=6, column=3)
        negativeButton.grid(row=6, column=0)
        plusButton.grid(row=5, column=3)
        minusButton.grid(row=4, column=3)
        multiplyButton.grid(row=3, column=3)
        divideButton.grid(row=2, column=3)
        bracketButton.grid(row=2, column=2)

    modeMenu.add_command(label='Simple Calculator', command=simpleCalculator, state=DISABLED)

    # function to convert into scientific calculator
    def scientificCalculator():
        """Function to create scientific calculator"""

        # changing the title of the window
        frame.title('Scientific Calculator')

        # adjusting width and position of problem
        problem.config(width=45)
        problem.grid(row=0, column=0, columnspan=7)

        # adjusting width and position of solution
        solution.config(width=27)
        solution.grid(row=1, column=0, columnspan=7)

        # changing the state of the menu
        modeMenu.entryconfig('Simple Calculator', state=NORMAL)
        modeMenu.entryconfig('Binary Calculator', state=NORMAL)
        modeMenu.entryconfig('Scientific Calculator', state=DISABLED)

        # removing binary buttons
        andButton.grid_forget()
        orButton.grid_forget()
        nandButton.grid_forget()
        norButton.grid_forget()
        xorButton.grid_forget()
        xnorButton.grid_forget()
        complementButton.grid_forget()
        leftShiftButton.grid_forget()
        rightShiftButton.grid_forget()
        binaryEqualButton.grid_forget()

        # adding simple buttons
        oneButton.grid(row=5, column=0)
        twoButton.grid(row=5, column=1)
        threeButton.grid(row=5, column=2)
        fourButton.grid(row=4, column=0)
        fiveButton.grid(row=4, column=1)
        sixButton.grid(row=4, column=2)
        sevenButton.grid(row=3, column=0)
        eightButton.grid(row=3, column=1)
        nineButton.grid(row=3, column=2)
        zeroButton.grid(row=6, column=1)
        pointButton.grid(row=6, column=2)
        equalButton.grid(row=6, column=3)
        negativeButton.grid(row=6, column=0)
        plusButton.grid(row=5, column=3)
        minusButton.grid(row=4, column=3)
        multiplyButton.grid(row=3, column=3)
        divideButton.grid(row=2, column=3)
        bracketButton.grid(row=2, column=2)

        # adding scientific buttons
        powerButton.grid(row=2, column=4)
        squareRootButton.grid(row=3, column=4)
        factorialButton.grid(row=4, column=4)
        permutationButton.grid(row=5, column=4)
        combinationButton.grid(row=6, column=4)
        sinButton.grid(row=2, column=5)
        cosButton.grid(row=3, column=5)
        tanButton.grid(row=4, column=5)
        logButton.grid(row=5, column=5)
        lnButton.grid(row=6, column=5)
        asinButton.grid(row=2, column=6)
        acosButton.grid(row=3, column=6)
        atanButton.grid(row=4, column=6)
        exponentialButton.grid(row=5, column=6)
        piButton.grid(row=6, column=6)

    modeMenu.add_command(label='Scientific Calculator', command=scientificCalculator, state=NORMAL)

    # function to convert into binary calculator
    def binaryCalculator():
        """Function to create binary calculator"""

        # changing the title of the window
        frame.title('Binary Calculator')

        # adjusting width and position of problem
        problem.config(width=25)
        problem.grid(row=0, column=0, columnspan=4)

        # adjusting width and position of solution
        solution.config(width=15)
        solution.grid(row=1, column=0, columnspan=4)

        # changing the state of the menu
        modeMenu.entryconfig('Simple Calculator', state=NORMAL)
        modeMenu.entryconfig('Scientific Calculator', state=NORMAL)
        modeMenu.entryconfig('Binary Calculator', state=DISABLED)

        # removing simple and Scientific buttons
        powerButton.grid_forget()
        squareRootButton.grid_forget()
        factorialButton.grid_forget()
        permutationButton.grid_forget()
        combinationButton.grid_forget()
        sinButton.grid_forget()
        cosButton.grid_forget()
        tanButton.grid_forget()
        logButton.grid_forget()
        lnButton.grid_forget()
        asinButton.grid_forget()
        acosButton.grid_forget()
        atanButton.grid_forget()
        exponentialButton.grid_forget()
        piButton.grid_forget()
        bracketButton.grid_forget()
        pointButton.grid_forget()
        negativeButton.grid_forget()
        twoButton.grid_forget()
        threeButton.grid_forget()
        fourButton.grid_forget()
        fiveButton.grid_forget()
        sixButton.grid_forget()
        sevenButton.grid_forget()
        eightButton.grid_forget()
        nineButton.grid_forget()

        # adding binary buttons
        zeroButton.grid(row=2, column=2)
        oneButton.grid(row=2, column=3)
        andButton.grid(row=3, column=0)
        orButton.grid(row=3, column=1)
        nandButton.grid(row=3, column=2)
        norButton.grid(row=3, column=3)
        xorButton.grid(row=4, column=0)
        xnorButton.grid(row=4, column=1)
        leftShiftButton.grid(row=4, column=2)
        rightShiftButton.grid(row=4, column=3)
        plusButton.grid(row=5, column=0)
        minusButton.grid(row=5, column=1)
        multiplyButton.grid(row=5, column=2)
        divideButton.grid(row=5, column=3)
        complementButton.grid(row=6, column=0)
        binaryEqualButton.grid(row=6, column=1, columnspan=3)

    modeMenu.add_command(label='Binary Calculator', command=binaryCalculator, state=NORMAL)

    # adding mode menu
    menubar.add_cascade(label='Mode', menu=modeMenu)

    # function to show help
    def showHelp():
        helpFrame = Tk()
        helpFrame.title("Help")
        helpFrame.geometry('400x500')
        helpFrame.iconbitmap('Help.ico')
        helpFrame.resizable(False, False)

        with open('Help.txt', 'r') as file:
            helpText = file.read()

        scrollBar = Scrollbar(helpFrame)
        scrollBar.pack(side=RIGHT, fill=Y)

        helpContent = Text(helpFrame, wrap=WORD, font='"IBM plex mono" 10', yscrollcommand=scrollBar.set)
        helpContent.insert(END, helpText)
        helpContent.config(state=DISABLED)
        helpContent.pack(side=LEFT, fill=BOTH)
        scrollBar.config(command=helpContent.yview)

    # creating help menu
    helpMenu = Menu(menubar, tearoff=FALSE)
    helpMenu.add_command(label='Show Help', command=showHelp)
    menubar.add_cascade(label='Help', menu=helpMenu)

    frame.resizable(False, False)

    frame.mainloop()


# driver function
def main():
    calculator()


if __name__ == '__main__':
    main()
