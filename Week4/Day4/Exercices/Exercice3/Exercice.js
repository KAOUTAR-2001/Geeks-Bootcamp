const marioGame = {
    detail: "An amazing game!",
    characters: {
        mario: {
            description: "Small and jumpy. Likes princesses.",
            height: 10,
            weight: 3,
            speed: 12,
        },
        bowser: {
            description: "Big and green, Hates princesses.",
            height: 16,
            weight: 6,
            speed: 4,
        },
        princessPeach: {
            description: "Beautiful princess.",
            height: 12,
            weight: 2,
            speed: 2,
        }
    },
};

// Convertir l'objet JS en JSON string avec indentation
const jsonMario = JSON.stringify(marioGame, null, 2);

// Afficher dans la balise <pre> dans ton HTML
document.getElementById('jsonDisplay').textContent = jsonMario;

// Optionnel : tu peux aussi mettre un breakpoint ici pour voir `jsonMario` dans l'inspecteur
console.log(jsonMario);
