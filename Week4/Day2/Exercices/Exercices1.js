const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

// Displaying the color choices
for (let i = 0; i < colors.length; i++) {
  console.log(`${i + 1}# choice is ${colors[i]}.`);
}

// Checking if "Violet" exists in the array
if (colors.includes("Violet")) {
  console.log("Yeah");
} else {
  console.log("No...");
}
