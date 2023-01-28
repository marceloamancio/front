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

