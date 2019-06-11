function findUniq(arr) {
  
  var a, b, c;
  
  a = arr[0];
  b = arr[1];
  c = arr[2];
  
  for ( var i = 2; i <= arr.length; i++ ){
  
    
    if ( a == c && b != a) { return b }
    if ( a != c && b == a) { return c }
    else if ( a != c && b != a ) { return a }
    
    
    c = arr[i];
  }
}