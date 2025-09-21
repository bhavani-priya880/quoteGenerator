async function fetchQuote() {
    try {
      const response = await fetch("https://quotegenerator-3.onrender.com/quote"); // ✅ correct port
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
  
