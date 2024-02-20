#!/usr/bin/node

// Import the fs module to work with the file system
const fs = require('fs');

// Check if a file path has been provided as an argument
if (process.argv.length < 3) {
  console.error('Please provide a file path.');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
