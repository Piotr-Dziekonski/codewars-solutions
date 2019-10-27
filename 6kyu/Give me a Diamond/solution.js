function diamond(n) {
    if (n % 2 == 0 || n < 0) {
        return null;
    }
    var diam = '';
    for (var i = n; i > 0; i = i - 2) {
        temp = '*'.repeat(i);
        temp = temp.concat('\n');
        let leer = ' '.repeat((n - i) / 2);
        temp = leer.concat(temp);
        diam = temp.concat(diam);
        if (i != n) diam = diam.concat(temp);
    }
    return diam;
};