const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th", "st", "nd", "rd"];

// Loop through the colors array
for (let i = 0; i < colors.length; i++) {
  const pos = i + 1;

  // Use ternary operator to get the correct suffix
  const suffix = (pos === 1) ? ordinal[1] :
                 (pos === 2) ? ordinal[2] :
                 (pos === 3) ? ordinal[3] :
                 ordinal[0];

  console.log(`${pos}${suffix} choice is ${colors[i]}.`);
}
