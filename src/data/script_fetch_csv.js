// URL to the external CSV file
const csvFileUrl = "./spotify_raw_dataset.csv";

// Fetch the CSV file and display its contents
fetch(csvFileUrl)
  .then((response) => response.text())
  .then((data) => {
    document.getElementById("output").textContent = data;
    console.log(data); // Also log the data to the console
  })
  .catch((error) => console.error("Error loading the CSV file:", error));
