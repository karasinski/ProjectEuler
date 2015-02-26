function smallest() {
	var length = 20;
	var arr = [];

	for (var i = 1; i < length + 1; i++) {arr.push(i);}
	console.log(lcm_nums(arr));
}

function gcf(a, b) { 
	return ( b == 0 ) ? (a):( gcf(b, a % b) ); 
}

function lcm(a, b) { 
	return ( a / gcf(a,b) ) * b; 
}

function lcm_nums(ar) {
	if (ar.length > 1) {
		ar.push( lcm( ar.shift() , ar.shift() ) );
		return lcm_nums( ar );
	} else {
		return ar[0];
	}
}

smallest();

//Math.max.apply(Math, arr)