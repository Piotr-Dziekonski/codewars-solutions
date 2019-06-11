function foldArray(array, runs){
  var array = array.slice();
  var odd, foldPoint;
 
  for( var x = 0; x < runs; x++ ){
  
    array.length % 2 == 0 ? odd = false : odd = true;
    odd ? foldPoint = ( array.length - 1 ) / 2 : foldPoint = array.length / 2;
  
    for ( var i = 0; i < foldPoint; i++ ){
      array[i] += array[array.length-1]; 
      array.pop();
    }    
  }
  return array;
}