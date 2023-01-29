# What is DOM?
* Document Object Model
* Created by the browser when a page is loaded
* Looks like a tree of elements of nodes
* We can make JS read or change (manipulate) the DOM.
* Change/Remove elements in the DOM / page.
* Change and add CSS styles in the page.
* Change and add elements of the attributes (href, scr, alt, custom)
* Create new elements in the page and insert it into the dom.
* Attach event listeners to elements (click, keypress, submit).

# Code
* let idName = document.getElementById("id-name") // get from <div id="id-name"> </div> --> ids should preferrably be unique
* id -> just one element; class -> query for multiple elements (preferably)
* let classElements = document.getElementByClassName("class-name") // --> get an HTMLCollection; which can be indexed classElements[0];
* leg tagElements = tagsLi = document.getElementsByTagName("li") // --> get all elements by the same tag;
* Looping
```
for (i = 0; i< titles.length; i++){
    console.log(titles[i]);
}
```

# The query selector [CSS Selector](https://www.youtube.com/watch?v=BD24Yno0QeU&list=PLs2iKUAvtzYyuuc_2OYhH223guSW8e0c-)
* ``` const wrap = document.querySelector('#wrapper') ```
* const wrap = document.querySelector('#book-list li:nth-child(2) .name');  // '#' --> class;  '<li>' --> li;  '.' --> .class
* ``` const wrap = document.querySelectorAll('#book-list li .name');  ``` // receives all elements instead of one
* node.textContent // to get text content from a node or element.
* document.querySelector("#book-list").innerHTML = "<h2>hey</h2> // changing the html content
