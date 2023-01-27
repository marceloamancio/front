// article: https://www.codeproject.com/Articles/5316027/100-Days-of-TypeScript-Day-1

class Addition{
    number1: number = 1;
    number2: number = 2;

    public Add(): number{
        return this.number1 + this.number2;
    }

}

function add(number1: number, number2: number){
    return number1 + number2;
}

let message: string = 'Hello World!!';
console.log(message);
console.log(add(1,2))

const additionInstance = new Addition();
additionInstance.number1 = 11;
additionInstance.number2 = 21; 

console.log(additionInstance.Add());
