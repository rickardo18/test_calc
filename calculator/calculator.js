// Basic calculator logic for UI

document.addEventListener('DOMContentLoaded', function() {
  const display = document.querySelector('.display');
  const buttons = document.querySelectorAll('.btn');
  let current = '';
  let operator = '';
  let operand = '';
  let resetNext = false;

  function updateDisplay(val) {
    display.textContent = val;
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', function() {
      const value = btn.textContent;
      if (btn.classList.contains('num')) {
        if (resetNext) {
          current = '';
          resetNext = false;
        }
        if (value === '.' && current.includes('.')) return;
        current += value;
        updateDisplay(current);
      } else if (btn.classList.contains('op')) {
        if (current === '') return;
        if (operand !== '') {
          current = operate(operand, operator, current);
          updateDisplay(current);
        }
        operator = value;
        operand = current;
        current = '';
      } else if (btn.classList.contains('eq')) {
        if (operator && operand !== '' && current !== '') {
          current = operate(operand, operator, current);
          updateDisplay(current);
          operator = '';
          operand = '';
          resetNext = true;
        }
      } else if (value === 'AC') {
        current = '';
        operator = '';
        operand = '';
        updateDisplay('0');
      } else if (value === 'DEL') {
        current = current.slice(0, -1);
        updateDisplay(current || '0');
      } else if (value === '%') {
        if (current !== '') {
          current = (parseFloat(current) / 100).toString();
          updateDisplay(current);
        }
      }
    });
  });

  function operate(a, op, b) {
    a = parseFloat(a);
    b = parseFloat(b);
    switch(op) {
      case '+': return (a + b).toString();
      case '-': return (a - b).toString();
      case '*': return (a * b).toString();
      case '/': return b === 0 ? 'Error' : (a / b).toString();
      default: return b.toString();
    }
  }

  // Export for testing
  if (typeof module !== 'undefined') {
    module.exports = { operate };
  }

  updateDisplay('0');
});
