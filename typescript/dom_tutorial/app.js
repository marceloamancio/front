let titles = document.getElementsByClassName('title');

// console.log('is array: ', Array.isArray(titles));
// console.log('is array: ', Array.isArray(Array.from(titles)));

Array.from(titles).forEach(function f(elem){
    console.log(elem);
});