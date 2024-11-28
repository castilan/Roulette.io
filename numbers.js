/**
 * Fetches the content of a text file and displays it in a specified element.
 * @param {string} filePath - The path to the text file.
 * @param {string} elementId - The ID of the element where the content will be displayed.
 */
function loadTextFile(filePath, elementId) {
    fetch(filePath)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.text();
        })
        .then(data => {
            // Insert the file content into the specified element
            document.getElementById(elementId).innerText = data;
            document.getElementById(elementId).style.fontSize = '60px';
        })
        .catch(error => {
            console.error(`Error fetching the file "${filePath}":`, error);
        });
}

function megaEnter(){
    let number = document.getElementById("newNumber").value;
    
    //console.log(number);
    
}

