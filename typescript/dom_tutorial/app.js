
function example01(){
    let titles = document.getElementsByClassName('title');

     console.log('is array: ', Array.isArray(titles));
     console.log('is array: ', Array.isArray(Array.from(titles)));
    
    Array.from(titles).forEach(function f(elem){
        //console.log(elem);
    });
}

function example02(){
    //const wrap = document.querySelector('#book-list li:nth-child(2) .name');
    //const wrap = document.querySelector('#book-list'); // li:nth-child(2) .name');
    const wrap = document.querySelectorAll('#book-list li .name'); // li:nth-child(2) .name');

    //node list - does not need Array wrapping.
    Array.from(wrap).forEach(function(elem){
        console.log(elem);
    });
    
}

function example03(){
    //const wrap = document.querySelector('#book-list li:nth-child(2) .name');
    //const wrap = document.querySelector('#book-list'); // li:nth-child(2) .name');
    const books = document.querySelectorAll('#book-list li .name'); // li:nth-child(2) .name');

    //node list
    books.forEach(function(book){
        //book.textContent = ':: ' +  book.textContent + ' ::';
        book.textContent += ' (book title)';
        //console.log(book.textContent);
    });
    
}

function example04(){
    const books = document.querySelector("#book-list");
    //books.innerHTML = "<h2>Booooks List</h2>";
    books.innerHTML += "<h2>Booooks List</h2>";

    console.log(books);
}



example04();