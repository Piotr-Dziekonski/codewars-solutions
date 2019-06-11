function findEvenIndex(arr){
  for ( var i = 1; i < arr.length; i++ ){
    var sumLeft = 0; 
    var sumRight = 0;
    for ( var j = 0; j < i; j++ ){
      sumLeft += arr[j];
    }
    for ( var j = i+1; j < arr.length; j++ ){
      sumRight += arr[j];
      
    }
    if( sumLeft == sumRight ) { return i; }
  }
  return -1; 
}