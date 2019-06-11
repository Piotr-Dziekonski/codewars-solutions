function productFib(prod){
  let fib = [0,1];
  let x = 2;
  while(true){
    let a = fib[x-1];
    let b = fib[x-2];
    fib.push(a + b);
    if (a * b == prod){
      return [b,a, true];
    }
    else if (a * b > prod){
      return [b,a, false];          
    }
    x+=1;
  }
}