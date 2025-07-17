document.addEventListener('DOMContentLoaded', function() {
  const expressionDisplay = document.querySelector('.expression');
  const resultDisplay = document.querySelector('.result');
  const buttons = document.querySelectorAll('.btn');

  let expression = '';
  let result = '';

  function updateDisplay() {
    expressionDisplay.textContent = expression;
    resultDisplay.textContent = result ? '=' + result : '';
  }

  function calculate(expr) {
    try {
      // Replace unicode division/multiplication if present
      expr = expr.replace(/÷/g, '/').replace(/×/g, '*');
      // Evaluate safely
      // eslint-disable-next-line no-eval
      let evalResult = eval(expr);
      if (typeof evalResult === 'number' && !isNaN(evalResult)) {
        return evalResult.toLocaleString();
      } else {
        return 'Error';
      }
    } catch {
      return 'Error';
    }
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', function() {
      const value = btn.textContent;
      if (btn.classList.contains('number')) {
        if (value === '.' && expression.endsWith('.')) return;
        expression += value;
      } else if (btn.classList.contains('operator')) {
        if (expression === '' || /[+\-*/]$/.test(expression)) return;
        expression += value;
      } else if (btn.classList.contains('equal')) {
        result = calculate(expression);
      } else if (btn.classList.contains('function')) {
        if (value === 'Ac') {
          expression = '';
          result = '';
        } else if (value === '←') {
          expression = expression.slice(0, -1);
        }
      }
      updateDisplay();
    });
  });

  updateDisplay();
});
