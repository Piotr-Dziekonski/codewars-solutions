function highAndLow(numbers){
    var highest = undefined;
    var lowest = undefined;

    var arr = numbers.split(" ");

    arr.forEach(function(number){
        if( parseInt(number) > highest || highest == undefined) { highest = number; }
        if( parseInt(number) < lowest || lowest == undefined) { lowest = number; }
    })
    return "" + highest + " " + lowest;
}