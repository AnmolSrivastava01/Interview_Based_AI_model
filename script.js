// Assuming you have already declared and initialized 'resultDiv' and 'startButton' variables

// Check if the browser supports Speech Recognition
if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
    const recognition = new window.SpeechRecognition() || new window.webkitSpeechRecognition();
  
    // Event triggered when speech recognition starts
    recognition.onstart = () => {
      resultDiv.classList.remove('hidden');
      resultDiv.innerText = 'Listening...';
    };
  
    // Event triggered when speech recognition ends
    recognition.onend = () => {
      resultDiv.innerText = 'Speech recognition ended.';
    };
  
    // Event triggered when speech is recognized
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      resultDiv.innerText = `You said: ${transcript}`;
    };
  
    // Event triggered on error
    recognition.onerror = (event) => {
      resultDiv.innerText = `Error occurred: ${event.error}`;
    };
  
    // Event triggered when the startButton is clicked
    startButton.addEventListener('click', () => {
      recognition.start();
    });
  } else {
    // Speech Recognition not supported
    resultDiv.innerText = 'Speech recognition is not supported in your browser.';
  }
  