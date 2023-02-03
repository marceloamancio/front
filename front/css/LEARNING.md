# CSS

* CSS is all about presentation
* CSS & CSS# are the same thing

# Intro
* All browsers have their own styles: margin, padding, font size, underlining links
 * so better to do css resets
* CSS is a collection of rules: each rule targets a specific tag or element in an html document.
 * rule which targets all 'p' tags on a page; or all tags with an #id; or all 'a' tags in the #nav

# Rule come in two parts
 ```
 SELECTOR DECLARATION
 #page-header {font-size: 10px; }

* Selectors: can target many things: ID's, classes, and so on.
* '#' id
* '.' class

* Declararion: In curly braces. It contains property and value;

# 3 ways to add css
* inline styling: for each element; not good
```         <h1 style="position: absolute; top: 0; width: 100%;">Selectors</h1>
```
* embedded style sheets: hard to maintain; 
```
<head>    
    <style>
        p {
            font-size: 100px;
        }
        
    </style>
</head>
```
* external style sheets  - This is the best

```
<head>
    <link rel="stylesheet" type="text/css" href="syntax.css">
</head>
```
* Comment /* */ or //

# Classes and ID's
* Classes: can be used multiple times in a page
* IDs: can be used only once per page - they are unique!

