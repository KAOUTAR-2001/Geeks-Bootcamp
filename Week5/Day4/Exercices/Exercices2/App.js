import people from './Data.js';

function calculateAverageAge(peopleArray) {
  const totalAge = peopleArray.reduce((sum, person) => sum + person.age, 0);
  const average = totalAge / peopleArray.length;
  console.log(` Âge moyen des personnes : ${average.toFixed(1)} ans`);
}

calculateAverageAge(people);