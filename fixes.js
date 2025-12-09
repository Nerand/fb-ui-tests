(function () {
    function parseMoney(text) {
      if (!text) return 0;
      var digits = String(text).replace(/[^\d]/g, "");
      return digits ? parseInt(digits, 10) : 0;
    }
  
    function getAvailableRubs(root) {
      var sumSpan = root.querySelector("#rub-sum");
      var reservedSpan = root.querySelector("#rub-reserved");
      if (!sumSpan || !reservedSpan) return 0;
      var sum = parseMoney(sumSpan.textContent);
      var reserved = parseMoney(reservedSpan.textContent);
      return sum - reserved;
    }
  
    function updateButtonState(root, amount) {
      var realButton = root.querySelector("button.g-button");
      if (!realButton) return;
  
      var available = getAvailableRubs(root);
      var canTransfer = amount > 0 && amount <= available;
  
      if (canTransfer) {
        realButton.style.pointerEvents = "auto";
        realButton.style.opacity = "1";
      } else {
        realButton.style.pointerEvents = "none";
        realButton.style.opacity = "0.4";
      }
    }
  
    function updateCommission(root, amount) {
      var span = root.querySelector("#comission");
      if (span) span.textContent = String(Math.floor(amount * 0.1));
    }
  
    document.addEventListener("input", function (e) {
      var target = e.target;
      if (!(target instanceof HTMLInputElement)) return;
  
      var root = document.getElementById("root");
      if (!root) return;
  
      if (target.placeholder === "0000 0000 0000 0000") {
        var digits = target.value.replace(/\D/g, "").slice(0, 16);
        target.value = digits;
        return;
      }
  
      if (target.placeholder === "1000") {
        var clean = target.value.replace(/\D/g, "");
        target.value = clean;
  
        var amount = clean ? parseInt(clean, 10) : 0;
  
        updateCommission(root, amount);
        updateButtonState(root, amount);
      }
    });
  
    window.addEventListener("load", function () {
      var root = document.getElementById("root");
      if (!root) return;
  
      var amountInput = root.querySelector("input[placeholder='1000']");
      if (amountInput instanceof HTMLInputElement) {
        var clean = amountInput.value.replace(/\D/g, "");
        amountInput.value = clean;
  
        var amount = clean ? parseInt(clean, 10) : 0;
  
        updateCommission(root, amount);
        updateButtonState(root, amount);
      }
    });
  })();
  