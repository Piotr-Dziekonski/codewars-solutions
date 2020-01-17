function high(x){
	let arr = x.split(' ')
	//a = charcode-64
	let bestPoints = 0
	let bestWord = ''
	let points = 0
	for(let i = 0; i < arr.length; i++){
		for(let j = 0; j < arr[i].length; j++)
		{
			points += arr[i].charCodeAt(j) -96   
		}
		if(points > bestPoints){
			bestPoints = points
			bestWord = arr[i]
		}
		points = 0
	}
	return bestWord
}