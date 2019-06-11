function likes(names) {
    var whoLikes = names;

    if( whoLikes.length == 0 ){
        return "no one likes this";
    }
    else if(whoLikes.length == 1){
        return whoLikes[0] + " likes this";
    }
    else if(whoLikes.length == 2){
        return whoLikes[0] + " and " + whoLikes[1] + " like this";
    }
    else if(whoLikes.length == 3){
        return whoLikes[0] + ", " + whoLikes[1] + " and " +  whoLikes[2] + " like this";
    }
    else if(whoLikes.length > 3){
        return whoLikes[0] + ", " + whoLikes[1] + " and " + (whoLikes.length - 2) + " others like this";
    }

}