// article: https://www.codeproject.com/Articles/5316027/100-Days-of-TypeScript-Day-1
var Addition = /** @class */ (function () {
    function Addition() {
        this.number1 = 1;
        this.number2 = 2;
    }
    Addition.prototype.Add = function () {
        return this.number1 + this.number2;
    };
    return Addition;
}());
function add(number1, number2) {
    return number1 + number2;
}
var message = 'Hello World!!';
console.log(message);
console.log(add(1, 2));
var additionInstance = new Addition();
additionInstance.number1 = 11;
additionInstance.number2 = 21;
console.log(additionInstance.Add());
