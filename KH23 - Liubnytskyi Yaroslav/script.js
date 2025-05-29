document.addEventListener('DOMContentLoaded', () => {
    const amountInput = document.getElementById('amount');
    const fromCurrencySelect = document.getElementById('from-currency');
    const toCurrencySelect = document.getElementById('to-currency');
    const convertButton = document.getElementById('convert-button');
    const swapButton = document.getElementById('swap-currencies');
    const resultArea = document.getElementById('result-area');
    const errorArea = document.getElementById('error-area');
    const apiSourceElement = document.querySelector('.api-source'); 

    const apiUrl = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json";

    let exchangeRates = {};

    async function fetchRates() {
        clearError(); 
        resultArea.textContent = ''; 
        setLoadingState(true); 
        let fetchDate = new Date().toLocaleDateString(); 

        try {
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error(`Помилка HTTP: ${response.status}`);
            }
            const data = await response.json();

            exchangeRates = { "UAH": 1.0 }; 
            let foundDate = null; 

            data.forEach(item => {
                if (item.cc && item.rate) {
                    exchangeRates[item.cc] = parseFloat(item.rate);
                    if (!foundDate && item.exchangedate) {
                       foundDate = item.exchangedate;
                    }
                }
            });

            fetchDate = foundDate || fetchDate;


            if (!exchangeRates.USD || !exchangeRates.EUR) {
                 console.warn("USD або EUR не знайдено в сьогоднішніх курсах НБУ.");
                 if (Object.keys(exchangeRates).length <= 1) {
                    throw new Error("Не вдалося отримати курси валют з відповіді НБУ.");
                 }
            }

            populateCurrencyOptions(); 
            setError(`Офіційні курси НБУ на ${fetchDate} оновлено.`);
            if (apiSourceElement) {
                apiSourceElement.textContent = `Офіційні курси НБУ на ${fetchDate}`;
            }
            setTimeout(clearError, 4000); 

        } catch (error) {
            console.error("Помилка завантаження курсів НБУ:", error);
            setError(`Помилка завантаження курсів НБУ: ${error.message}.`);
            if (apiSourceElement) {
                 apiSourceElement.textContent = 'Не вдалося завантажити курси';
            }
            amountInput.disabled = true;
            fromCurrencySelect.disabled = true;
            toCurrencySelect.disabled = true;
            convertButton.disabled = true;
            swapButton.disabled = true;
        } finally {
            setLoadingState(false); 
        }
    }

    function populateCurrencyOptions() {
        const currencies = Object.keys(exchangeRates).sort(); 

        fromCurrencySelect.innerHTML = '';
        toCurrencySelect.innerHTML = '';

        currencies.forEach(currency => {
            const optionFrom = document.createElement('option');
            optionFrom.value = currency;
            optionFrom.textContent = currency; 
            fromCurrencySelect.appendChild(optionFrom);

            const optionTo = document.createElement('option');
            optionTo.value = currency;
            optionTo.textContent = currency;
            toCurrencySelect.appendChild(optionTo);
        });

        if (currencies.includes("USD")) fromCurrencySelect.value = "USD";
        if (currencies.includes("UAH")) toCurrencySelect.value = "UAH";

        amountInput.disabled = false;
        fromCurrencySelect.disabled = false;
        toCurrencySelect.disabled = false;
        convertButton.disabled = false;
        swapButton.disabled = false;
    }

    function performConversion() {
        clearError(); 
        resultArea.textContent = ''; 

        const amount = parseFloat(amountInput.value);
        const fromCurrency = fromCurrencySelect.value;
        const toCurrency = toCurrencySelect.value;

        if (isNaN(amount) || amount <= 0) {
            setError("Будь ласка, введіть коректну позитивну суму.");
            return;
        }
        if (!fromCurrency || !toCurrency) {
            setError("Будь ласка, виберіть обидві валюти.");
            return;
        }

        if (!exchangeRates[fromCurrency] || !exchangeRates[toCurrency]) {
             setError("Обрані валюти відсутні в завантажених курсах.");
             return;
        }

        if (fromCurrency === toCurrency) {
            resultArea.textContent = `${amount.toFixed(2)} ${toCurrency}`; 
            return;
        }

        try {
            let amountInUah;
            amountInUah = amount * exchangeRates[fromCurrency];

            let result;
            if (exchangeRates[toCurrency] === 0) {
                throw new Error(`Офіційний курс для ${toCurrency} дорівнює нулю.`);
            }
            result = amountInUah / exchangeRates[toCurrency];

            resultArea.textContent = `${result.toFixed(2)} ${toCurrency}`;

        } catch (error) {
             console.error("Помилка конвертації:", error);
             setError(`Помилка конвертації: ${error.message}`);
        }
    }

    function swapCurrencies() {
        const fromValue = fromCurrencySelect.value;
        const toValue = toCurrencySelect.value;

        if(fromValue && toValue) {
             fromCurrencySelect.value = toValue;
             toCurrencySelect.value = fromValue;
             performConversion(); 
        } else {
            setError("Спочатку завантажте курси валют.");
        }
    }

     function setError(message) {
        errorArea.textContent = message;
        errorArea.style.display = 'block'; 
    }
    function clearError() {
        errorArea.textContent = '';
        errorArea.style.display = 'none'; 
    }
    function setLoadingState(isLoading) {
        if (isLoading) {
            convertButton.textContent = 'Завантаження...';
            convertButton.disabled = true;
        } else {
            convertButton.textContent = 'Конвертувати';
             if(amountInput && !amountInput.disabled) {
                 convertButton.disabled = false;
             }
        }
    }

  
    convertButton.addEventListener('click', performConversion);
    swapButton.addEventListener('click', swapCurrencies);

    fetchRates();
});