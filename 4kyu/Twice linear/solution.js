function dblLinear(n) {
    var u = [];
    u[0] = 1;
    var a = 0;
    var b = 0;
    while( u.length<n+1 ){
    
      var y = 2 * u[a]+1;
      var z = 3 * u[b]+1;
      if( y<z ){ u.push(y); a++; }
      else if( y>z ){ u.push(z); b++ }
      else{ u.push(z); a++; b++; } 
    } 
    return u[n];
}