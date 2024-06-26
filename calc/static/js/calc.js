let display = document.getElementById('display');
let operand1 = '';
let operand2 = '';
let operator = '';

function appendNumber(number) {
    if (operator === '') {
        operand1 += number;
        display.value = operand1;
    } else {
        operand2 += number;
        display.value = operand2;
    }
}

function appendOperator(op) {
    if (operator === '') {
        operator = op;
    } else {
        calculateResult();
        operand1 = display.value;
        operator = op;
        operand2 = '';
    }
}

function clearDisplay() {
    display.value = '';
    operand1 = '';
    operand2 = '';
    operator = '';
}

function calculateResult() {
    let result;
    switch (operator) {
        case '+':
            result = parseFloat(operand1) + parseFloat(operand2);
            break;
        case '-':
            result = parseFloat(operand1) - parseFloat(operand2);
            break;
        case '*':
            result = parseFloat(operand1) * parseFloat(operand2);
            break;
        case '/':
            result = parseFloat(operand1) / parseFloat(operand2);
            break;
        default:
            return;
    }
    display.value = result;
    operand1 = result.toString();
    operand2 = '';
    operator = '';
}
