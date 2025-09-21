async function fetchQuote() {
    try {
      const response = await fetch("http://127.0.0.1:5001/quote"); // ✅ correct port
      const data = await response.json();
  
      document.getElementById("quote").innerText = `"${data.quote}"`;
      document.getElementById("author").innerText = `- ${data.author}`;
    } catch (error) {
      console.error("Error fetching quote:", error);
    }
  }
  
  document.getElementById("generateBtn").addEventListener("click", fetchQuote);
  
  // Load one quote on page start
  fetchQuote();
  
