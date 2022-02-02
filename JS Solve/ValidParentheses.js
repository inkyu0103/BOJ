var isValid = function(s) {
    const parentheseMacth = new Map([[')','('],['}','{'],[']','[']]);
    const openParenthese = ['(','[','{'];
    const stack =[];
    
    for(let char of s) {
        if(!stack.length) {stack.push(char);continue;}
        
        if(openParenthese.includes(char)){ stack.push(char); continue;} // 아 in이 그게 아니구나? includes
        
        if(!!stack.length && stack[stack.length-1] === parentheseMacth.get(char)) {stack.pop();continue;} 
        
        return false
        
    }

    return !stack.length ? true: false
}

