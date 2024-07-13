const buttons = document.querySelectorAll('.gemini-button');

buttons.forEach(button => {
  button.addEventListener('click', () => {
    // Simulate an asynchronous process (e.g., API call)
    setTimeout(() => {
      // Example of using the extracted hex color code
      const hexColor = geminiApiClient.extractedHexColor;

      // Replace 'your_prompt' with the appropriate prompt
      const prompt = `Analyze skin tone for color code: ${hexColor}`;

      geminiApiClient.callGeminiAPI(prompt)
        .then(response => {
          // Handle the API response and update the UI
          console.log(response.data);
          // Update the UI based on the response
        })
        .catch(error => {
          console.error('Error calling Gemini API:', error);
        });
    }, 1000); // Adjust the delay as needed to ensure Python script output is available
  });
});
