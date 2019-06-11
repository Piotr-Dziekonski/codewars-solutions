function validatePIN (pin) {
    if(pin.length != 6 && pin.length != 4){

        
        return false;
    }
    else{
        for(var i = 0; i < pin.length; i++){
        console.log(pin[i]);
        if( !(parseInt(pin[i]) >= 0) && !(parseInt(pin[i]) <= 9) ){
            return false;
        }
        }
        return true;
    }
}