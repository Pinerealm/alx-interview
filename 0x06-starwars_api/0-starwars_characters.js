#!/usr/bin/node
// Prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    // Get the url of each character in the movie
    const characters = JSON.parse(body).characters;
    const charDict = {};

    for (const character of characters) {
      const charId = (character.split('/')[5]);
      request(character, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          charDict[charId] = JSON.parse(body).name;

          // This preserves the order of the characters
          if (Object.keys(charDict).length === characters.length) {
            for (const id in charDict) {
              console.log(charDict[id]);
            }
          }
        }
      });
    }
  }
});
